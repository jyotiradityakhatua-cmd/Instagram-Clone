from app.database.collection import users_collection

def follow_user(current_username, target_username):
    if current_username == target_username:
        return {"error": "You cannot follow yourself."}

    result = users_collection.update_one(
        {"username": current_username,
        "following": {"$ne":target_username}
        },

        {
            "$addToSet": {"following": target_username},
            "$inc": {"following_count": 1}
        }
    )

    if result.modified_count == 0:
        return {"message": "You followed successfully."}
        
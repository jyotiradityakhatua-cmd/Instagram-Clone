user = {
"username": username,
"password": password,
"followers": [],
"following": [],
"follower_count": 0,
"following_count": 0,
"posts": [],
"created_at": datetime.utcnow()
}


user_collection.insert_one(user)
return user

def get_user(username: str):
    return user_collection.find_one({"username:": username})


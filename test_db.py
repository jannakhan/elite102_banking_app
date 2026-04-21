from db import create_user, get_users

create_user("Janna", 500)

users = get_users()
print(users)
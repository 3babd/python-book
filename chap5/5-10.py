current_users = ['rose', 'badb', 'narodnik', 'plato', 'bran']
new_users = ['bran', 'rose', 'krystal', 'ROSE', 'kitty', 'gainz']

for user in new_users:
    if (user.lower() in current_users) and (user.lower() in new_users):
        print("Sorry, the username", user, "has been taken")
    else:
        print("That username", user, "is available")

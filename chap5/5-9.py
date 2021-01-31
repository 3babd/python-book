username = []

if username:
    for user in username:
        if user == 'admin':
            print("Hello admin, would you like a status report?")
        else:
            print("Hello", user, "thank you for logging in again")
else:
    print("We need to find some users!")

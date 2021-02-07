responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your name?\n")
    response = input("\n Where in the world do you want to visit?\n")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)\n")
    if repeat == 'no':
        polling_active = False

    print("\n--- Poll Results---\n")
    for name, response in responses.items():
        print(name, "would like to visit", response)

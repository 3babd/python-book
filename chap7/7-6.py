prompt = "\nEnter toppings\n"

active = True

while active:
    pizza = input(prompt)

    if pizza == 'quit':
        active = False
    else:
        print(pizza, "added to pizza")

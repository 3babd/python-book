prompt = "\nEnter toppings\n"

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(pizza, "added to pizza")

prompt = "\nEnter pizza toppings\n"

start = 0
while start < 5:
    pizza = input(prompt)
    start += 1
    if pizza == 'quit':
        break
    else:
        print(pizza, "added to pizza")
        print("You have", 5 - start, "toppings remaining")

pizzas = ['cheese', 'meat', 'aubergine']

friends_pizzas = pizzas[:]

pizzas.append('tuna')
friends_pizzas.append('chorizo')

for pizza in pizzas:
    print("My favorite pizzas are", pizza)

for pizza in friends_pizzas:
    print("My friend's favourite pizzas are", pizza)

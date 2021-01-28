my_foods = ['pizza', 'pasta', 'kebab']
friend_foods = my_foods[:]

my_foods.append('cake')
friend_foods.append('chocolate')

my_foods.append('fruit')
friend_foods.append('nuts')

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)

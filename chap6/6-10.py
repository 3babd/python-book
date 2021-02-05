favorite_numbers = {
        'amir':['4', '101'],
        'nar':['101', '8'],
        'plato':['8', '3'],
        'rose':['5', '37'],
        'badb':['3', '7']
        }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(name.title() + "'s favourite numbers are:")
    else:
        print(name + "'s favourite number is:")
    for number in numbers:
        print(number)


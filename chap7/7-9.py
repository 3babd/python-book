sandwich_orders = [
        'pastrami sandwich',
        'egg sandwich',
        'pastrami sandwich',
        'cheese sandwich',
        'ham sandwich',
        'pastrami sandwich',
        'turkey sandwich',
        'peanut butter sandwich'
        ]

finished_sandwiches = []

print("Sorry, we have ran out of pastrami")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    print("Cancelled your pastrami order")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Making", current_sandwich)
    finished_sandwiches.append(current_sandwich)
    for sandwich in finished_sandwiches:
        print("Finished", sandwich)

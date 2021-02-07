sandwich_orders = ['egg sandwich','cheese sandwich','ham sandwich','turkey sandwich','peanut butter sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Making", current_sandwich)
    finished_sandwiches.append(current_sandwich)
    for sandwich in finished_sandwiches:
        print(sandwich, "is finished")

favorite_places = {
        'amir':['barcelona', 'thanet'],
        'rose':['donegal', 'howth'],
        'molly':['paris', 'glasgow'],
        'plato':['brazil']
        }

for name, places in favorite_places.items():
    if len(places) > 1:
        print(name.title() + "'s favourite places are:")
    else:
        print(name.title() + "'s favourite place is:")
    for place in places:
        print(place.title())

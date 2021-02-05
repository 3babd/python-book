cities = {
        'dublin':{
            'population':'2 million',
            'language':'Irish, English',
            'food':'chowder'
            },
        'barcelona':{
            'population':'2 million',
            'language':'Catalan, Spanish',
            'food':'tapas'
            },
        'new york':{
            'population':'10 million',
            'language':'English',
            'food':'pizza'
            }
        }

for city, city_info in cities.items():
    print("City:", city.title())
    print("Population:", city_info['population'])
    print("Language:", city_info['language'])
    print("Food:", city_info['food'].title())

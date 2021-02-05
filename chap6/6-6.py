favorite_languages = {'rose':'rust','amir':'python','plato':'lisp','janus':'lisp'}
participants = ['rose', 'cat', 'babd', 'amir', 'plato', 'xesan', 'janus']

for person in participants:
    if person in favorite_languages.keys():
        print("Thank you", person.title(), "for taking the poll")
    else:
        print(person.title(), "would you like to take the poll?")

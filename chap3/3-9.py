guests = ['amir,', 'pete,', 'cody,', 'land,', 'spinoza,']

print("There are", len(guests), "guests")

rejection = "cannot come to dinner."
print("Sorry,", guests.pop(2).title().rstrip(','), rejection)

print("There are", len(guests), "guests")

guests.insert(2, 'paul,')
guests.insert(0, 'Amy,')
guests.insert(2, 'Max,')
guests.append('Benoit,')

print("There are", len(guests), "guests")

uninvite = "you cannot come to the party. Sorry"

print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)

print("There are", len(guests), "guests")

del guests[1]
del guests[0]
print(guests)

print("There are", len(guests), "guests")

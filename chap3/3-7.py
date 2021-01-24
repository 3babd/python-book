guests = ['amy,', 'amir,', 'max,', 'pete,', 'paul,', 'land,', 'spinoza,', 'benoit,']
update = "I am so sorry. My table didn't arrive and I can only invite 2 people for dinner."

print("Dear", guests[0].title(), update)
print("Dear", guests[1].title(), update)
print("Dear", guests[2].title(), update)
print("Dear", guests[3].title(), update)
print("Dear", guests[4].title(), update)
print("Dear", guests[5].title(), update)
print("Dear", guests[6].title(), update)
print("Dear", guests[7].title(), update)

uninvite = "you cannot come to the party. Sorry"

print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)
print("Dear", guests.pop().title(), uninvite)

reinvite = "you are still invited. See you at the dinner"

print(guests[0].title(), reinvite)
print(guests[1].title(), reinvite)

del guests[1]
del guests[0]
print(guests)

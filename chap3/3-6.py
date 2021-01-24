guests = ['amir,', 'pete,', 'paul,', 'land,', 'spinoza,']
update = "I found a bigger table!"

print("Good news", guests[0].title(), update)
print("Good news", guests[1].title(), update)
print("Good news", guests[2].title(), update)
print("Good news", guests[3].title(), update)
print("Good news", guests[4].title(), update)

guests.insert(0, 'Amy,')
guests.insert(2, 'Max,')
guests.append('Benoit,')

invite = "I am having an even bigger dinner party, would you like to come?"

print("Dear", guests[0].title(), invite)
print("Dear", guests[1].title(), invite)
print("Dear", guests[2].title(), invite)
print("Dear", guests[3].title(), invite)
print("Dear", guests[4].title(), invite)
print("Dear", guests[5].title(), invite)
print("Dear", guests[6].title(), invite)
print("Dear", guests[7].title(), invite)


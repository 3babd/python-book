guests = ['amir,', 'pete,', 'cody,', 'land,', 'spinoza,']
invite = "I am having a dinner party, would you like to come?"

print("Dear", guests[0].title(), invite)
print("Dear", guests[1].title(), invite)
print("Dear", guests[2].title(), invite)
print("Dear", guests[3].title(), invite)
print("Dear", guests[4].title(), invite)

rejection = "cannot come to dinner."
print("Sorry,", guests.pop(2).title().rstrip(','), rejection)

guests.insert(2, 'paul,')

print("Dear", guests[0].title(), invite)
print("Dear", guests[1].title(), invite)
print("Dear", guests[2].title(), invite)
print("Dear", guests[3].title(), invite)
print("Dear", guests[4].title(), invite)

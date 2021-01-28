cubes = [value**3 for value in range(1, 11)]
message = "The first 3 items in this list are:"
print(message, cubes[0:3])

message = "3 items from the middle of in this list are:"
print(message, cubes[5:8])

message = "The last 3 items in this list are:"
print(message, cubes[-3:])

prompt = "What age are you?\n"

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free")
        break
    if age >= 3 and age <= 12:
        print("Your ticket is $10")
        break
    if age > 12:
        print("Your ticket is $15")
        break


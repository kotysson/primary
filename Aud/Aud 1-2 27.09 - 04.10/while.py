x = 1
while x <= 5:
    print(f"x equal to {x}")
    x += 1

count = 5
while count >= 0:
    print(count)
    count -= 1

n = 10
x = 0
while x < n:
    x += 2
    print(x)

while True:
    password = input("Enter reliable password\n")
    if len(password) < 8:
        print("Too short. Try again")
    else:
        print("Good password")
        break

# right
while True:
    string = input("Enter q\n")
    if string == "q":
        print("Great")
        break
    else:
        print("Try again")

experiment
string = input("Enter q\n")
while True:
    if string == "q":
        print("Great")
        break
    else:
        print("Try again")

while True:
    message = input("Enter message ")
    if message != "q":
        print(message.lower())
    else:
        print("goodbye")
        break
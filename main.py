
print("Welcome to Fizzbuzz!")
guess = int(input("please choose a number to start with\n"))

max_number = int(input("choose a maximum number\n"))
game_number = True
while game_number:
    for i in range(1, max_number):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
print("thank you for playing fizzbuzz!")

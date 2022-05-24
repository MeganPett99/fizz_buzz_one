
print("Welcome to Fizzbuzz!")


def fizzbuzz():
    max_number = int(input("choose a maximum number\n"))
    game_number = True
    while game_number:
        num = int(input("choose a number to start with\n"))
        for i in range(num, max_number):
            if i % 3 == 0 and i % 5 == 0:
             print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    return fizzbuzz()


print(fizzbuzz())
print("thank you for playing fizzbuzz!")

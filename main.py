output_list = ""


def divisible_by(fb_num, db_num):
    return True if(fb_num % db_num == 0) else False


def fizz_buzz():
    output_list = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            output_list += '"FizzBuzz", '
        elif i % 3 == 0:
            output_list += '"Fizz", '
        elif i % 5 == 0:
            output_list += '"Buzz", '
        else:
            output_list += f'"{str(i)}", '
    return output_list


print(fizz_buzz())

# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 10.
# Користувач намагається вгадати число. Програма може давати підказки тільки "More", "Less", "You won!"

from random import randint
rand_value = randint(1, 10)
go_loop = True
while go_loop:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        if int(user_input) > rand_value:
            print("Less")
        elif int(user_input) < rand_value:
            print("More")
        else:
            print("You won")
            go_loop = False

########################################

# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 12.
# Програма виводить на екран число, яке створено і назву місяця, який відповідає цьому числу.

rand_value = randint(1, 12)
match rand_value:
    case 1:
        print(rand_value, " - January")
    case 2:
        print(rand_value, " - February")
    case 3:
        print(rand_value, " - March")
    case 4:
        print(rand_value, " - April")
    case 5:
        print(rand_value, " - May")
    case 6:
        print(rand_value, " - June")
    case 7:
        print(rand_value, " - July")
    case 8:
        print(rand_value, " - August")
    case 9:
        print(rand_value, " - September")
    case 10:
        print(rand_value, " - October")
    case 11:
        print(rand_value, " - November")
    case 12:
        print(rand_value, " - December")

########################################

# Написати програму в якій користувач вводить два цілих числа.
# Програма виводить результат піднесення першого числа у степінь відповідний другому числу.
# Зробити обробку всіх можливих помилок.
# В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )

user_input1 = input("Enter a number: ")
user_input2 = input("Enter a number: ")
try:
    user_input1 = int(user_input1)
    user_input2 = int(user_input2)
    result = user_input1 ** user_input2
    print("Result: ", result)
except ValueError:
    print("Input is not a number")
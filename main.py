import random as r

def pypassword_generator(number_letters, number_symbols, number_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = []
    for i in range(number_letters):
        password.append(letters[r.randrange(len(letters))])
    for i in range(number_symbols):
        password.append(symbols[r.randrange(len(symbols))])
    for i in range(number_numbers):
        password.append(numbers[r.randrange(len(numbers))])
    r.shuffle(password)
    print(*password, sep="")

number_letters = int(input("How many letters would you like in password? \n"))
number_symbols = int(input("How many symbols would you like? \n"))
number_numbers = int(input("How many numbers would you like? \n"))

pypassword_generator(number_letters, number_symbols, number_numbers)
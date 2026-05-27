import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
letters_choice=[]
symbols_choice=[]
numbers_choice=[]
for i in range(nr_letters):
    letters_choice.append(random.choice(letters))
for i in range(nr_symbols):
    symbols_choice.append(random.choice(symbols))
for i in range(nr_numbers):
    numbers_choice.append(random.choice(numbers))
sequence = letters_choice + symbols_choice + numbers_choice
sequence_str = "".join(sequence)
print("Sequence Generated is", sequence_str,"\n")
shuffled_password_str= "".join(random.sample(sequence, len(sequence)))
print("Password Generated is", shuffled_password_str)

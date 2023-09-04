import random

length = int(input("Enter the desired length: "))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                    'Z']
SYMBOLS = ['@', '*', '(', ')', '<']

COMBINED_LIST = DIGITS + upper_case + lower_case + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(upper_case)
rand_lower = random.choice(lower_case)
rand_symbol = random.choice(SYMBOLS)

temp_password = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(length - 4):
    temp_password = temp_password + random.choice(COMBINED_LIST)

temp_password_list = list(temp_password)
random.shuffle(temp_password_list)

password = ""
for x in temp_password_list:
    password = password + x

print("Generated Password: ",password)

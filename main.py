import random
import string

#identifying characters for password
uppercase_chars = list(string.ascii_uppercase)
lowercase_chars = list(string.ascii_lowercase)
numbers = list(string.digits)
punctuation = list(string.punctuation)

usrinput = int(input("Number of Characters: "))

alphabet = (uppercase_chars + lowercase_chars + numbers + punctuation)

password = ""

#randomize alphabet and create the password
for i in range(usrinput):
    password += "".join(random.choice(alphabet))

print(password)
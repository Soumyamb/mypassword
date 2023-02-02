import random

characters="abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTY123456789!@#$%^&*"
while 1:
       password_length=int(input("What lenght of password do you want to generate: "))
       pw_count=int(input("How many passwords do you want to generate: "))
       for x in range(0,pw_count):
            password=""
            for x in range(0,password_length):
               password_char=random.choice(characters)
               password=password + password_char
            print('Here are the password:', password)
        
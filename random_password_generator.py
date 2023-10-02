#random password generator

#initializing arrays and importing libraries
import random

letters_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [1,2,3,4,5,6,7,8,9,0]
arrays = [letters_lowercase, letters_uppercase, numbers]

#asking for length of password
length = int(input("Enter length of password generated: "))
password = ""
print("--------------------------------------------------")

for i in range(length):
    random_array = random.choice(arrays)
    password += str(random.choice(random_array))

print("Password:",password)

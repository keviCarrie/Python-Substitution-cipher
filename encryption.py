
print("Welcome to my Substitution Cipher encryption program")
import random
import string



#create a string of characters, i will import constaints from string module
#i add a space character
characters = " " + string.punctuation + string.digits + string.ascii_letters


#create a list so that each character is an individual element

characters = list(characters)

#then create a key that will shuffle

key = characters.copy()

print(f"characters: {characters}")
print(f"key:{key}")
#rando.shuffle enable the string to shuffle in random order

random.shuffle(key)

#Encrypt
#lets ask for user input
#plain_text is the original message 
#cipher_text is the encrypted message

plain_text = input ("Enter the message to encrypt: ")
cipher_text = ""

# we iterate every letter in the plain_letter and create a variable index,then refer to our key to get whatever letter is that same index
for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encypted_message: {cipher_text}")    

#Decrypt

cipher_text = input("Enter a mesage to decypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters[index]

print(f"encypted message: {cipher_text}")
print(f"original meaaasge: {plain_text}")    
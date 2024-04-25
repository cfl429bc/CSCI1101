##+-----------------------------------------------------------------------
##
## Python Homework Assignment - (c) 2024 Chris Londal.  All Rights Reserved.
##
## File:        a11pA.py
##
## Description:
##
##   Homework 11 Problem A
##
## History:     April-24-2024     cfl429bc        Created
##
##------------------------------------------------------------------------

import sys
import string

def read_vigenere_table(filename):
    dictionary = {}
    with open(filename) as file:
        rows = file.readlines()
        for i, line in enumerate(rows):
            line = line.strip()
            dictionary[rows[0][i]] = {}
            for j, char in enumerate(line):
                dictionary[rows[0][i]][rows[0][j]] = char

    return dictionary

def extend_key(message, key):
    len_key = (len(message) // len(key)) + 1
    new_key = (key * len_key)[:len(message)]

    return new_key

def encrypt(message, key, dictionary):
    encrypted_message = []
    key_index = 0
    for char in message:
        if char in string.ascii_uppercase:
            row = key[key_index]
            col = char
            encrypted_message.append(dictionary[row][col])
            key_index += 1
        else:
            encrypted_message.append(char)

    return "".join(encrypted_message)

def decrypt(encrypted, key, dictionary):
    decrypted_message = []
    key_index = 0
    for char in encrypted:
        if char in string.ascii_uppercase:
            key_char = key[key_index]
            for col_char, encrypted_char in dictionary[key_char].items():
                if encrypted_char == char:
                    decrypted_message.append(col_char)
                    break
            key_index += 1
        else:
            decrypted_message.append(char)

    return "".join(decrypted_message)

def main():
    try:
        cipher_table = read_vigenere_table("cypher/cipher_table.txt")

        choice = input("Do you want to encrypt or decrypt? ").lower()
        if choice not in ["encrypt", "decrypt"]:
            print("Invalid answer!")
            sys.exit()
        
        if choice == "encrypt":
            message = input("Enter the message to be encrypted: ").upper()
            key = input("Enter the key: ").upper()
            extended_key = extend_key(message, key)
            encrypted_message = encrypt(message, extended_key, cipher_table)
            print(encrypted_message)
        else:
            encrypted = input("Enter the message to be decrypted: ").upper()
            key = input("Enter the key: ").upper()
            extended_key = extend_key(encrypted, key)
            decrypted_message = decrypt(encrypted, extended_key, cipher_table)
            print(decrypted_message)
    except Exception:
        print()
        print("An error occurred.")
        print("Please try again!")

main()
'''
Copyright (c) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#0001
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: ACTIVE
'''

import time

#function for the simple encryption process
def encryption_algorithm():
    user_input = input("Enter the message you want to encrypt: ").lower()
    encrypt_output = []

    #the conversion table is a dictionary that just moves the character to the next one in the english alphabet
    conversion_table = {
        "a" : "H", "b" : "I", "c" : "J", "d" : "K", "e" : "L", "f" : "M", "g" : "N", "h" : "O", "i" : "P", "j" : "Q", "k" : "R", "l" : "S", "m" : "T", "n" : "U", "o" : "V", "p" : "W", "q" : "X", "r" : "Y", "s" : "Z", "t" : "A", "u" : "B", "v" : "C", "w" : "D", "x" : "E", "y" : "F", "z" : "G", "0" : "7", "1" : "8", "2" : "9", "3" : "0", "4" : "1", "5" : "2", "6" : "3", "7" : "4", "8" : "5", "9" : "6", " " : " "
    }

    #for each character in the user message, it will find a corresponding letter in the dictionary and append it to the list
    for character in user_input: 
        character_output = str(conversion_table[str(character)])
        encrypt_output.append(character_output)

    #prints the final message
    print("".join(encrypt_output))


#function for the simple decryption process
def decryption_algorithm():
    user_input = input("Enter message you want to decrypt: ").upper()
    decrypt_output = []

    #the decrypt conversion table is a dictionary that just moves the character to the previous one in the english alphabet
    conversion_table = {
        "H" : "a", "I" : "b", "J" : "c", "K" : "d", "L" : "e", "M" : "f", "N" : "g", "O" : "h", "P" : "i", "Q" : "j", "R" : "k", "S" : "l", "T" : "m", "U" : "n", "V" : "o", "W" : "p", "X" : "q", "Y" : "r", "Z" : "s", "A" : "t", "B" : "u", "C" : "v", "D" : "w", "E" : "x", "F" : "y", "G" : "z", "7" : "0", "8" : "1", "9" : "2", "0" : "3", "1" : "4", "2" : "5", "3" : "6", "4" : "7", "5" : "8", "6" : "9", " " : " "
    }

    #same thing as before but decrypting
    for character in user_input:
        character_output = str(conversion_table[str(character)])
        decrypt_output.append(character_output)
    print("".join(decrypt_output))


#basically a forever loop that asks the user whether they want to use the encrypt or decrypt function
while True:
    encrypt_or_decrypt = input("Do you want to [1]encrypt or [2]decrypt a message? ").lower()

    if encrypt_or_decrypt == "1" or encrypt_or_decrypt == "encrypt":
        encryption_algorithm()
    elif encrypt_or_decrypt == "2" or encrypt_or_decrypt == "decrypt":
        decryption_algorithm()
    else:
        print("Input value error; exiting...")
        time.sleep(float(0.5))
        exit()

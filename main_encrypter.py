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
        "a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h" : "i", "i" : "j", "j" : "k", "k" : "l", "l" : "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a", "0" : "1", "1" : "2", "2" : "3", "3" : "4", "4" : "5", "5" : "6", "6" : "7", "7" : "8", "8" : "9", "9" : "0", " " : " "
    }

    #for each character in the user message, it will find a corresponding letter in the dictionary and append it to the list
    for character in user_input: 
        character_output = str(conversion_table[str(character)])
        encrypt_output.append(character_output)

    #prints the final message
    print("".join(encrypt_output))


#function for the simple decryption process
def decryption_algorithm():
    user_input = input("Enter message you want to decrypt: ").lower()
    decrypt_output = []

    #the decrypt conversion table is a dictionary that just moves the character to the previous one in the english alphabet
    conversion_table = {
        "b" : "a", "c" : "b", "d" : "c", "e" : "d", "f" : "e", "g" : "f", "h" : "g", "i" : "h", "j" : "i", "k" : "j", "l" : "k", "m" : "l", "n" : "m", "o" : "n", "p" : "o", "q" : "p", "r" : "q", "s" : "r", "t" : "s", "u" : "t", "v" : "u", "w" : "v", "x" : "w", "y" : "x", "z" : "y", "a" : "z", "1" : "0", "2" : "1", "3" : "2", "4" : "3", "5" : "4", "6" : "5", "7" : "6", "8" : "7", "9" : "8", "0" : "9", " " : " "
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

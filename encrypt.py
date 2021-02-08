#Vernam Cipher Encryption Code
#Created 27/12/20 by Rhiannon
#Last Edited 29/01/21 by Jeff

#For generating the random key
import random
import string

""" Changelog:
        - Made code, file references more general
        - Changed key generation to depend on user provided string
        ... therefore user does not need to know raw key string
        - Made Encrypt() return cyphertext instead of raw key
        - Made it so cyphertext is not saved on the system
"""

#This function opens the plain text file
#Input Variables: -
#Output Variables: PlainFile
def OpenFile(filename):
    PlainText = open(filename,"r")
    return PlainText

#This function gets the length of the file
#Input Variables: -
#Output Variables: Length
def GetFileLength(filename):
    Length = 0
    PlainText = OpenFile(filename)
    for line in PlainText:
        for letter in line:
            Length += 1
    PlainText.close()
    return Length
    
#This function generates the full length encryption key
#Input Variables: -
#Output Variables: key
def GetKey(Length, user_key):
    random.seed(a=user_key, version=2)
    key = ""
    for i in range(0, Length):
        key += random.choice(string.ascii_letters)
    return key

#This function encrypts the text, placing it in a new file
#Input Variables: -
#Output Variables: key
def Encrypt(filename, user_key):
    PlainText = OpenFile(filename)
    print(GetFileLength(filename))
    key = GetKey(GetFileLength(filename), user_key)
    #creates new file, ensure does not exist
    CipherText = ""
    i = 0
    #reads one char from text file
    char = PlainText.read(1)
    #loops through all chars in file
    while char:
        #Key XOR PlainText char for encryption
        newchar = ord(key[i]) ^ ord(char)
        #To avoid the first 32 ascii chars as they mess it up
        # if newchar<32:
        #     while newchar<32:
        #         key= key[:i] + random.choice(string.ascii_letters) + key[i+1:]
        #         newchar = ord(key[i]) ^ ord(char)
            
        CipherText += chr(newchar)
        i+=1       
        char = PlainText.read(1)
    print("File encrypted.\n")
    return CipherText


#This function decrypts the text, placing it in a new file
#Input Variables: Key
#Output Variables: -
def Decrypt(CipherText, user_key):
    DecodedText = ""
    print(len(CipherText))
    key = GetKey(len(CipherText), user_key)
    for i in range(len(CipherText)):
        newchar = ord(key[i]) ^ ord(CipherText[i])
        DecodedText += chr(newchar)
    print("File decrypted.\n")
    return DecodedText

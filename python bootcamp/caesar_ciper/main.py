from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#function to encrypt the message 
def encrypt(plane_text,shift_number):
    cipher_text=""
    for letter in plane_text:
        position=alphabet.index(letter)
        new_pos=position+shift_number
        new_letter=alphabet[new_pos]
        cipher_text +=new_letter
    print(f"The encoded text is {cipher_text}")

# calling the encrypt function


#function to decrypt the cipher text
def decrypt(cipher_text,shift_number):
    plane_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_pos=position -shift_number
        new_letter=alphabet[new_pos]
        plane_text +=new_letter
    print(f"The decoded text is {plane_text}")
    
if direction=="decode":
    decrypt(text,shift)
elif direction=="encode":
    encrypt(text,shift)
else:
    print("invaild input")


import string
alphabets = list(string.ascii_letters)
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        position=alphabets.index(char)
        new_postion = (position + shift_key) % 26
        cipher_text += alphabets[new_postion]
    print(f"Here is the text after encryption: \n")
    print(cipher_text)
def decryption(text2, shift_key2):
    cipher_text2 = ""
    for char2 in text2:
        position2 = alphabets.index(char2)
        new_pos = (position2-shift_key2) % 26
        cipher_text2 -= alphabets[new_pos]
    print(f"Here is the decrypted text, {cipher_text2}")
what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
text=input("Type your message:\n")
shift=int(input("Enter shift key:\n"))

if what_to_do == "encrypt":
    encryption(plain_text=text, shift_key=shift)

elif what_to_do == "decrypt":
    decryption(text2=text, shift_key2=shift)
def encrypt(text, index_shift):
    
    encrypted_char_list = []    

    for letter in alphabet:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index + index_shift

        if shifted_index <= alpha_letter_index:
            shifted_alphabet.append(alphabet[shifted_index])
        else:
            new_index = shifted_index - alpha_letter_index
            shifted_alphabet.append(alphabet[new_index])

    for character in text:
        if character.isalpha() == True:
            char_index = alphabet.index(character)
            encrypted_char_list.append(shifted_alphabet[char_index])

        else:
            encrypted_char_list.append(character)
            
    
    encrypted_message = "".join(encrypted_char_list)
    print("This is encrypted message", encrypted_message)
    cache = encrypted_message
    return encrypted_message

def decrypt(encrypted_message):
    decrypted_char_list = []
    
    for letter in encrypted_message:
        if letter.isalpha():
            letter_index = shifted_alphabet.index(letter)
            decrypted_char_list.append(alphabet[letter_index])
        else: 
            decrypted_char_list.append(letter)

    decrypted_message = "".join(decrypted_char_list)
    print("This is decrypted message", decrypted_message)
    return decrypted_message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_alphabet = []
alpha_letter_index = len(alphabet) - 1
cache = ""
end = False

while not end:
    encode_decode = input("Type 'encode' to encrypt or 'decode' to decrypt a message")
    
    if encode_decode == "encode":
        shift = int(input("Enter a number to shift te alphabet for cypher"))
        user_text = input("Enter a message to encrypt")
        encrypted_message =  encrypt(text = user_text, index_shift=shift)
        
    elif encode_decode == "decode" and len(cache) > 0:
        decrypted_message = decrypt(encrypted_message = encrypted_message)
    
    else :
        print("There is no message in cache to decrypt. Please encrypt a message first")
    
    next = input("Do you want to encode another message, or decode previous one ? (Y/N)").lower()
    
    if next == "y":
        continue
    else:
        end = True

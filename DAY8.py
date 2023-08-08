alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:").lower()
shift = int(input("Type the shift number:"))

# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print("The encoded text is ",  cipher_text)
        
# encrypt(plain_text=text, shift_amount=shift)


# def decrypt(cipher_text, shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position  - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print("The decoded text is ",  plain_text)

# decrypt(cipher_text=text, shift_amount=shift)

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)


# UPDATED VERSION

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
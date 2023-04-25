import base64
import string
from termcolor import colored

# Add header
print(colored("""
  ______  __    __   __  .__   __.   ___    __     __     ______     ___   
 /      ||  |  |  | /_ | |  \ |  |  / _ \  |  |   / /    /  __  \   / _ \  
|  ,----'|  |__|  |  | | |   \|  | | | | | |  |  / /_   |  |  |  | | (_) | 
|  |     |   __   |  | | |  . `  | | | | | |  | | '_ \  |  |  |  |  > _ <  
|  `----.|  |  |  |  | | |  |\   | | |_| | |__| | (_) | |  `--'  | | (_) | 
 \______||__|  |__|  |_| |__| \__|  \___/  (__)  \___/   \______/   \___/  
                                                                           
  BASE64 TO XOR - Created By Eyal Zabarsky
""", 'red'))

# Get encrypted message from user input
encrypted_message = input("Enter the encrypted message in base64: ")

# Decode message from base64
decoded_message = base64.b64decode(encrypted_message)

# Iterate over all possible XOR keys (0-255)
for xor_key in range(256):
    # Decrypt message using XOR
    decrypted_message = ''.join(chr(b ^ xor_key) for b in decoded_message)

    # Check if the decrypted message contains only ASCII characters
    if all(ord(char) < 128 for char in decrypted_message):
        # Split the decrypted message into words
        words = decrypted_message.split()

        # Check if all words are ASCII
        if all(word.isascii() for word in words):
            # Print the original message in green color
            print(colored(f"Decrypted message with XOR key {xor_key}: {decrypted_message}", 'green'))



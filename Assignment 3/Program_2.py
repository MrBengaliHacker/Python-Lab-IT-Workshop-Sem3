text = input("Enter a string: ")

# Create an empty string to store encrypted text
encrypted_text = ""

for char in text:
    if char.isalpha():   # Check if the character is a letter (A-Z or a-z)
        
        if char.isupper():  # If the character is UPPERCASE
            encrypted_text += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        
        else:  # If the character is LOWERCASE
            encrypted_text += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    
    else:
        # If it's not a letter (like number, space, symbol), keep it as it is
        encrypted_text += char  

print("Encrypted string:", encrypted_text)
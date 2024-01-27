alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
val = input("scrie: ")
original_message = val

word = [char.lower() for char in val]

# Create a list of tuples containing each letter and its corresponding position in the alphabet
original_positions = [(letter, alphabet.index(letter) + 1) for letter in word if letter in alphabet]

a, b, c = 1, 1, 1  # Initial values for a, b, c

# Encrypt the message
encrypted_letters = []
for letter, position in original_positions:
    position += a + b + c

    # Update variables a, b, and c and handle overflow
    a += 1
    if a > 26:
        a = 1
        b += 1
        if b > 26:
            b = 1
            c += 1
            if c > 26:
                c = 1

    # Change the letter to the one in the alphabet with the modified position
    modified_letter = alphabet[(position - 1) % 26]
    encrypted_letters.append(modified_letter)
    print(f"{letter}: {position} -> {modified_letter}")

# Display the encrypted message
encrypted_message = "".join(encrypted_letters)
print("\nEncrypted Message:")
print(encrypted_message)

# Reset variables a, b, c to their initial values for decryption
a, b, c = 1, 1, 1

# Display the original message
print("\nOriginal Message:")
print(original_message)




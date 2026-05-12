import string

# VIa class
def ceasar(text, shift, alphabets):

    def shift(alphabet):
        return alphabet[shift:] + alphabet[:shift]




# Start of plain code.

plain_text = input("Enter text: ").lower()
shift = int(input("Enter shift: "))
job = input("Encrypt or Decrypt? ").lower()

if job == "encrypt":
    # encrypt
    # shift = 5  # over 26 and the app wont work
    # shift = 80
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted)

    encrypted = plain_text.translate(table)

    print(encrypted)

elif job == "decrypt":
    # decrypt
    shift = 26 - shift
    shift %= 26

    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted)

    encrypted = plain_text.translate(table)

    print(encrypted)

else:
    print("Invalid input")

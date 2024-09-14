"""Here we're gonna code a Vigenere(?) cipher"""

text = 'Hello Zaira'
custom_key = 'python'


def vigenere(message, key, direction=1):
    """Encrypt in the vigenere ways"""
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resulting_text = ''
    for char in message.lower():
        # first manage the spaces
        if not char.isalpha():
            resulting_text += " "
        else:
            # pick the key character to use
            key_char = key[key_index % len(key)]
            key_index += 1
            # find the char index and calculate new with key offset
            char_index = alphabet.find(char)
            key_offset = alphabet.index(key_char)
            new_char_index = (char_index + key_offset *
                              direction) % len(alphabet)
            resulting_text += alphabet[new_char_index]

            # print(key_char, key_offset, char_index)
    print(resulting_text)


def encryption(message, key):
    """call vigenere with the default direction"""
    vigenere(message, key)


def decrypt(message, key):
    """call vigenere with direction value of -1"""
    vigenere(message, key, -1)


vigenere(text, custom_key)

decrypt("wcesc mpgkh", custom_key)

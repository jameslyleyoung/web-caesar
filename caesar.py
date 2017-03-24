def encrypt(text, rot):
    newtext = ''
    for letter in text:
        newletter = rotate_character(letter, rot)
        newtext = newtext + newletter
    return newtext

def alphabet_position(letter):
    import string
    if letter in string.ascii_lowercase:
        lcl = string.ascii_lowercase
        index = lcl.find(letter)
        return index
    if letter in string.ascii_uppercase:
        ucl = string.ascii_uppercase
        index = ucl.find(letter)
        return index

def rotate_character(char, rot):
    import string
    if char in string.digits or char in string.punctuation or char in string.whitespace:
        return char
    index = alphabet_position(char) + rot
    if index > 25:
        index = index % 26
    if char in string.ascii_lowercase:
        lcl = string.ascii_lowercase
        newchar = lcl[index]
        return newchar
    if char in string.ascii_uppercase:
        ucl = string.ascii_uppercase
        newchar = ucl[index]
        return newchar

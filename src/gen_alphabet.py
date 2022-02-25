def generate_alphabet(start, end):
    alphabet = {}
    for i in range(start, end+1):
        c = chr(i)
        alphabet[c] = i

    return alphabet
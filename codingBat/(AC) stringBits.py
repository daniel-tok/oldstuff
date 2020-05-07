def string_bits(str):
    p = 1
    word = ''
    for letter in str:
        if p % 2 != 0:
            word += letter
        p += 1
    return word

print(string_bits('words'))

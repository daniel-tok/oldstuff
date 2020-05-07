def string_splosion(str):
    x = 0
    limit = len(str) - (len(str) + x)
    start = 0
    word = ''
    string = ''
    for letter in str:
        word += letter
        start += 1
        if start == limit:
            string += word
            x += 1
            start = 0
    return string

print(string_splosion('chocolate'))


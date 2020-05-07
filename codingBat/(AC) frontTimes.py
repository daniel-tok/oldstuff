def front_times(str, n):
    p = 0
    word = ''
    for letter in str:
        word += letter
        p += 1
        if p >= 3:
            break
    return word * n

print(front_times('Chocolate', 5))
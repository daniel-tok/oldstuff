# error when last character is 'h' - because last character adds 1 to index counter, out of range

def count_hi(str):
    index = 0
    hiCounter = 0
    indexArray = []
    letters = []
    for letter in str:
        if letter == 'h':
            indexArray.append(index)
            index += 1
            letters.append(letter)
        else:
            index += 1
    for number in indexArray:
        try:
            if str[number + 1] == 'i':
                hiCounter += 1
        except IndexError:
            return hiCounter
    return hiCounter

def make_out_word(out, word):
    list =[]
    str = ''
    list += out.split()
    list.insert(2, word)
    for element in list:
        str += element
    return str

print(make_out_word('<<>>', 'yooo'))
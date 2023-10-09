def operator(a, b, c):
    return b if a else c

def operator_elif(a, b, c, d, e):
    return b if a else operator(c, d, e)


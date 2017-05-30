def transit(f):
    c = 5 / 9 * (f - 32)
    print(round(c, 2), end = ' ')

def printtable():
    for i in range(0, 300, 20):
        transit(i)

printtable()

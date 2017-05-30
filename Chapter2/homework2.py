def prime(num):
    flag = True
    if num == 1:
        flag = False
    k = num // 2 +1
    for i in range(2, k):
        if num % i == 0:
            flag = False
            break

    return flag


def monisen(no):
    p = 1
    count = 0
    while count < no:
        if prime(p):
            m = 2 ** p - 1
            if prime(m):
                count += 1
        p += 1
    return m

print(monisen(int(input())))

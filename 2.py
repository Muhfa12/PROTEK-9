#2
def bintang(n):
    a = 2 * n
    for i in range(n):
        print(("*"*(1 + 2 * i)).center(a))
bintang(4)

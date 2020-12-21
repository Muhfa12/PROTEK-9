#3
def bintang(n):
    a = n
    for i in range(n - 3):
        x = 1 + 2 * i
        print(("*" * x).center(a))
    for x in range(n):
        y = 5 - 2 * x
        print(("*" * y).center(a))
bintang(7)

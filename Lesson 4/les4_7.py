def my_fatc(n):
    j = 1
    for i in range(2, n+1):
        j*=i
    yield j

b = my_fatc(5)
print(next(b))

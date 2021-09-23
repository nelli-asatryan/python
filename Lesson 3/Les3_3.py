def func1 (a, b, c):
    sort1 = sum(sorted([a,b,c])[-2:])
    print(sort1)

print(func1(1,3,5))
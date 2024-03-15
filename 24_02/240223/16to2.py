def f(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return f(n//2) + str(n % 2)


x = input()
if x.isdigit():
    print(f(int(x)))
else:
    print(f(ord(x)-55))
a, b = map(int, input().split())
c = [0] * b
while a >= 2:

    for i in range(b):
        if i == a % b:
            c[i] += 1

    a = a // b

sum = 0
for j in range(len(c)):
    sum += c[j] ** 2

print(sum)
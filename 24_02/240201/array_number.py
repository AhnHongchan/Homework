def selectionsort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]


N = int(input())

for tc in range(1, N+1):
    length = int(input())
    lst = list(map(int, input().split()))

    selectionsort(lst, length)

    print(f"#{tc}", *lst)
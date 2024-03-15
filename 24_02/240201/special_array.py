def specialsort(a, N):
    for i in range(N-1):
        if i % 2 == 0:
            max_Idx = i
            for j in range(i+1, N):
                if a[max_Idx] < a[j]:
                    max_Idx = j
            a[max_Idx], a[i] = a[i], a[max_Idx]

        else:
            min_Idx = i
            for j in range(i+1,N):
                if a[min_Idx] > a[j]:
                    min_Idx = j
            a[min_Idx], a[i] = a[i], a[min_Idx]


T = int(input())
for tc in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))

    specialsort(lst, num)
    
    print(f"#{tc}", end = " ")

    for i in range(10):
        print(lst[i], end= " ")
    print()
    
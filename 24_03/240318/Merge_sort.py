# # 3월 18일 <병합정복, 백트래킹> 5205 병합 정렬
def m_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    L = m_sort(L)
    R = m_sort(R)
    global cnt
    if L[-1] > R[-1]:
        cnt += 1
    return merge(L, R)
 
 
def merge(L, R):
    result = [0] * (len(L) + len(R))
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result[i+j] = L[i]
            i += 1
        else:
            result[i+j] = R[j]
            j += 1
    while i < len(L):
        result[i+j] = L[i]
        i += 1
    while j < len(R):
        result[i+j] = R[j]
        j += 1
    return result
 
 
T = int(input())
for case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    cnt = 0
    arr = m_sort(arr)
 
    print(f'#{case}', arr[n // 2], cnt)
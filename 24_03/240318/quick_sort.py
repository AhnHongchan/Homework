def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 피벗은 리스트의 중간 원소로 선택합니다.
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 원소들을 모은 리스트
    equal = [x for x in arr if x == pivot]  # 피벗과 같은 원소들을 모은 리스트
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 원소들을 모은 리스트
    
    # 재귀 호출을 통해 왼쪽과 오른쪽 부분 리스트를 각각 정렬합니다.
    return quick_sort(left) + equal + quick_sort(right)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr)
    print(f'#{tc} {arr[n//2]}')
# 병합 정렬 함수
def msort(m):
    # 리스트의 길이가 1일 때, 즉 더 이상 분할할 수 없는 상태이면 해당 리스트를 반환
    if len(m) == 1:
        return m
    
    # 리스트를 반으로 나누기
    mid = len(m) // 2
    left = m[:mid]  # 왼쪽 반
    right = m[mid:]  # 오른쪽 반

    # 왼쪽 반과 오른쪽 반을 재귀적으로 병합 정렬하여 정렬된 리스트를 반환
    left = msort(left)
    right = msort(right)
    
    # 정렬된 왼쪽 반과 오른쪽 반을 병합
    return merge(left, right)

# 병합 함수
def merge(left, right):
    # 결과를 저장할 리스트 생성 (두 리스트의 길이의 합만큼)
    result = [0] * (len(left) + len(right))
    i = j = 0  # left와 right 리스트의 인덱스를 가리키는 변수
    
    # left와 right 리스트의 원소를 비교하며 작은 값을 result 리스트에 채움
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1
    
    # 남은 원소들을 result 리스트에 추가
    while i < len(left):
        result[i+j] = left[i]
        i += 1
    while j < len(right):
        result[i+j] = right[j]
        j += 1
    
    # 정렬된 결과 리스트 반환
    return result

# 입력을 받아서 리스트로 변환
m = list(map(int, input().split()))

# 병합 정렬을 수행하여 정렬된 리스트를 얻고, 그 중에서 50만 번째 숫자 출력
ans = msort(m)
print(ans[500000])



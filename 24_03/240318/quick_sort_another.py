def pivot(a,left,right):
 
    p = a[left]  # pivot= left
    i = left
    j = right
 
    while i<= j:
        while i <= j and a[i] <= p:
            i += 1
        while i<= j and a[j] >= p:
            j -= 1
 
        # p보다 큰수와 p보다 작은수 스왑
        if i < j:
            a[i], a[j] = a[j], a[i]
 
    a[left], a[j] = a[j], a[left]
    return j
 
def quick_sort(A, l, r):
 
    if l < r:
        s = pivot(A,l,r) # s 가 pivot
        quick_sort(A,l,s-1)
        quick_sort(A,s+1,r )
 
 
 
 
T= int(input())
for tc in range(1,T+1):
    N = int (input())
    lst = list(map(int, input().split()))
    left = 0
    right = N-1
    quick_sort(lst, left, right)
 
    print(f'#{tc} {lst[N//2]}')

'''
첫 번째 코드가 실행 시간이 더 짧게 나온 이유는 
주로 피벗을 기준으로 배열을 나누는 과정이 효율적으로 구현되어 있기 때문일 것입니다. 
두 코드 모두 퀵 정렬을 사용하고 있지만, 
첫 번째 코드에서는 피벗을 기준으로 배열을 나누는 과정에서 효율적인 방법을 사용했습니다.

피벗을 중심으로 작은 값들과 큰 값들을 나누는 과정에서 
두 번째 코드는 세 개의 리스트를 생성하고 값을 복사하는 작업이 필요합니다. 
이는 메모리 사용량과 시간을 더 소모하게 됩니다. 
반면에 첫 번째 코드에서는 입력 배열의 값들을 직접 바꾸는 방식을 사용하여 
메모리 사용량을 줄이고 불필요한 복사 작업을 피할 수 있습니다.

따라서 입력 크기가 큰 경우에는 더 효율적인 메모리 사용과 실행 시간을 보장하는 
첫 번째 코드가 더 우수한 결과를 보일 수 있습니다. 
하지만 이는 입력 데이터의 특성에 따라 달라질 수 있으므로 
항상 모든 상황에 대해 일반화하기는 어렵습니다. 
종합적으로 두 코드를 비교하고 선택할 때는 
입력 데이터의 크기와 특성을 고려하여 결정하는 것이 좋습니다.
'''
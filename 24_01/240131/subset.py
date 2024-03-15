lst = [i for i in range(1,13)]

num = int(input())


for test_case in range(1, num+1):
    N, K = map(int, input().split())
    # N = 부분집합 원소의 개수, K= 부분집합 원소들의 합
    length = len(lst) # lst 원소의 개수
    result = 0 # 일치하는 개수

    
    new_lst = []
    # 부분집합 list 생성
    for i in range(1 << length): # 1 << n: 부분 집합의 개수
        tmp = []
        for j in range(length):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j): # i의 j번 비트가 1인 경우
                tmp.append(lst[j])
        new_lst.append(tmp)

    # print(new_lst)

    for x in new_lst:
        if len(x) == N and sum(x) == K:
            result += 1
    
    print(f'#{test_case} {result}')



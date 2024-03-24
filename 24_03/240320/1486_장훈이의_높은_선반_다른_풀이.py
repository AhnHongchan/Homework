for tc in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    # 모든 탑의 길이를 담을 리스트
    sums_lst = [0]
    for i in range(N):
        # 현재 키에서 모든 탑의 길이를 담은 리스트를 다 더해주고 추가
        for j in range(len(sums_lst)):
            val = H[i] + sums_lst[j]
            sums_lst.append(val)

    # B를 넘지 않는 가장 큰 값
    print(f'#{tc+1}', min([x-B for x in sums_lst if x-B >= 0]))
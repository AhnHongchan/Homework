T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    case = [list(input()) for _ in range(N)]
    # 가로 회문 찾기
    for i in range(N):          # 행 단위로 반복
        for j in range(N-M+1):    # N개의 열에서 M개의 크기만큼 반복
            for k in range(M):      # 길이 M인 회문이 있나 찾음
                if case[i][j+k] != case[i][j+M-1-k]:
                    break           # 회문이 아닐결우 반복 취소
            else:
                ans = ''.join(case[i][j:j+M])
                print(f'#{tc} {ans}')
                break
 
    # 세로 회문 찾기
    for i in range(N):  # 열 단위로 반복
        for j in range(N-M+1):
            for k in range(M):
                if case[j+k][i] != case[j+M-k-1][i]:
                    break
            else:
                ans = []
                for a in range(M):
                    ans += list(case[j+a][i])
                ans =''.join(ans)
                print(f'#{tc} {ans}')
                break




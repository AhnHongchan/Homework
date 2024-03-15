T = int(input())
ans = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    cnt = min(B,D) - max(A,C)
    if cnt < 0:
        cnt = 0
    ans.append(cnt)

for tc in range(1, T+1):
    print(f'#{tc} {ans[tc-1]}')
K = 3
N = 6
arr = [0, 1, 0, 1, 1, 1]
ans = 0
cnt = 0
for i in range(N):
    if arr[i] == 0:
        if cnt == K:
            ans += 1
        cnt = 0
    else:
        cnt += 1
        if i == N-1:
            if cnt == K:
                ans += 1

print(ans)

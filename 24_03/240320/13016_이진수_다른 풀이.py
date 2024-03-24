T = int(input())
for tc in range(1, T + 1):
    N, H = input().split()
    HEX = int(H, 16)
    BIN = bin(HEX)
    ans = BIN[2:]
 
    if len(ans) == 4 * (int(N)):
        print(f"#{tc} {ans}")
    else:
        temp = '0' * ((4 * int(N)) - len(ans))
        ans = temp + ans
        print(f"#{tc} {ans}")
 
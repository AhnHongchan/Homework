T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    prime_cnt = [0] * 5

    
    for i in range(5):
        while N % prime[i] == 0:
            prime_cnt[i] += 1
            N //= prime[i]
    
    print(f"#{tc}", *prime_cnt)

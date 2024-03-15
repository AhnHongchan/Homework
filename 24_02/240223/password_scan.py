info = {'0001101': '0', 
        '0011001': '1', 
        '0010011': '2', 
        '0111101': '3', 
        '0100011': '4', 
        '0110001': '5', 
        '0101111': '6', 
        '0111011': '7', 
        '0110111': '8', 
        '0001011': '9'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f"#{tc}", end=' ')

    idx_x = 0
    idx_y = 0

    # Find the last occurrence of '1' in the matrix
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':  # Change to '1' (string) instead of 1 (integer)
                idx_x = i
                idx_y = j
                break

    password = ''
    for i in range(8):
        for key, value in info.items():  # Change to info.items() instead of info
            if key == arr[idx_x][idx_y-7*i-6:idx_y-7*i+1]:  # Adjust indexing
                password = value + password
                break  # Break when a match is found
        else:
            print(0)
            break

    else:  # This else corresponds to the inner for loop (no break occurred)
        sum_v = 0
        ans = 0
        for j in range(len(password)):
            if j % 2 == 0:
                sum_v += int(password[j]) * 3
                ans += int(password[j])
            else:
                sum_v += int(password[j])
                ans += int(password[j])
        if sum_v % 10 == 0:
            print(ans)
        else:
            print(0)
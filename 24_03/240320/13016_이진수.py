def hex_to_bin(hex_string):
    decimal_value = int(hex_string, 16)  # 16진수 문자열을 10진수로 변환
    binary_string = bin(decimal_value)[2:]  # '0b' 접두어 제거
    return binary_string.zfill(len(hex_string) * 4)  # 0으로 패딩하여 4의 배수 길이로 맞춤

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    N = int(N)
    ans = hex_to_bin(num)

    print(f'#{tc} {ans}')


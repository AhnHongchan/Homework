T = int(input())
for tc in range(1, T+1):
    word = input()
    long_word = input()

    if word in long_word:
        print(f"#{tc}", 1)
    else:
        print(f"#{tc}", 0)
    

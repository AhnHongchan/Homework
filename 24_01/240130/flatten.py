def solve():
    num = int(input())
    case = list(map(int, input().split()))

    for _ in range(num):
        max_val = case[0]
        min_val = case[0]
        max_index = 0
        min_index = 0
        for i in range(len(case)):
            if max_val <= case[i]:
                max_val = case[i]
                max_index = i

            if min_val >= case[i]:
                min_val = case[i]
                min_index = i

        case[min_index] += 1
        case[max_index] -= 1

    max_val = case[0]
    min_val = case[0]
    max_index = 0
    min_index = 0

    for j in range(len(case)):
        if max_val <= case[j]:
            max_val = case[j]
            max_index = j

        if min_val >= case[j]:
            min_val = case[j]
            min_index = j

    return case[max_index] - case[min_index]


for test_case in range(1, 11):
    print(f"#{test_case} {solve()}")

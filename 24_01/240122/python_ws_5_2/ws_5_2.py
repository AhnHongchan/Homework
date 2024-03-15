# 주어진 리스트에서 중복된 요소를 제거한 새로운 리스트를 반환하는 remove_duplicates 함수를 작성하시오.
# 리스트를 인자로 받아 중복이 제거된 새로운 리스트를 반환해야 한다.
def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
# [1, 2, 3, 4, 5]

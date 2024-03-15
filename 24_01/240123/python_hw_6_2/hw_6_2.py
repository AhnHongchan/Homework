# 아래 함수를 수정하시오.
def remove_duplicates_to_set(x):
    lst = []
    for i in x:
        if i not in lst:
            lst.append(i)
        my_set = set(lst)
    return my_set


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

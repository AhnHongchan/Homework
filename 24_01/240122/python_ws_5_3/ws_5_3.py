# 주어진 튜플을 정렬하여 새로운 튜플로 반환하는 sort_tuple 함수를 작성하시오.
# 튜플을 인자로 받아 정렬된 새로운 튜플을 반환해야 합니다.
def sort_tuple(x):
    new_tuple = ()
    a = list(x)
    a.sort()
    b = tuple(a)
    new_tuple = new_tuple + b


    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# 주어진 셋에서 두 개의 셋의 교집합을 반환하는 intersection_sets 함수를 작성하시오.
# 두 개의 셋을 인자로 받아 교집합을 반환해야 한다.
def intersection_sets(x, y):
    return x & y


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)

# 주어진 셋에서 두 개의 셋의 차집합을 반환하는 difference_sets 함수를 작성하시오.
# 두개의 셋을 인자로 받아 차집합을 반환해야 한다.
def difference_sets(set1, set2):
    return set1.difference(set2)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)

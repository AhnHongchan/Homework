# 주어진 딕셔너리에서 특정 키와 값을 이용하여 항목을 추가하는 add_item_to_dict 함수를 작성하시오
# 딕셔너리와 키, 값의 쌍을 인자로 받아 항목을 추가한 새로운 딕셔너리를 반환해야 한다.
import copy

def add_item_to_dict(x, y, z):
    new_dict = copy.copy(x)
    new_dict.setdefault(y, z)

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

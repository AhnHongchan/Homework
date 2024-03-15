# 주어진 딕셔너리에서 특정 키에 해당하는 값을 가져오는 get_value_from_dict 함수를 작성하시오
# 딕셔너리와 키를 인자로 받아 해당 키에 대응하는 값을 반환해야 한다.
def get_value_from_dict(x, y):
    if y in x:
        return x.get(y)
    


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

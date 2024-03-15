# 주어진 딕셔너리에서 모든 키를 리스트로 반환하는 get_keys_from_dict 함수를 작성하시오.
# 딕셔너리를 인자로 받아 모든 키를 담은 리스트를 반환해야 한다.

def get_keys_from_dict(dict_0):
    keys = my_dict.keys()
    return list(keys)
    


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

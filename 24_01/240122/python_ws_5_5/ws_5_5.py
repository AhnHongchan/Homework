# 주어진 리스트에서 홀수를 모두 제거하고, 짝수만을 남긴 리스트를 반환하는 even_elements 함수를 작성하시오.
# 단 extend와 pop을 활용하여 구현해야 한다.
def even_elements(lst):
    lst_even = []
    for i in my_list[:]:
        if i % 2 == 0:
            lst_even.extend([i])
        else:
            a = my_list.pop(int(i/2))
    
    
    return lst_even


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

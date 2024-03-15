data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
lst = []
for s in data_1:
    if s.isupper():
        lst.append(s)
    elif s.isspace():
        lst.append(s)
        
lst_1 = ''.join(lst)
print(lst_1)

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
for j in '내힘들다':
    a = data_2.find(j)
    arr.append(a)

print(arr) # [37, 29, 12, 5]

arr.sort()
print(arr) # [5, 12, 29, 37]
b = []
for i in arr:
    b.append(data_2[i])
c = ''.join(b)
print(c)
# 아래에 코드를 작성하시오.

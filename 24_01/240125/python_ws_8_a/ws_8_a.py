# 주어진 코드가 끝까지 실행될 수 있도록  try-except 문으로 수정하시오.

data = {'name': '홍길동'}
try:
    print(data['age'])
except KeyError:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)
# 아래에 코드를 작성하시오.

arr = ['반갑', '하세요', '안녕']
try:
    for i in range(4):
        print(arr.pop())
except IndexError:
    print(arr)
    print('더 이상 pop 할 수 없습니다.')
# 아래에 코드를 작성하시오.


try:
    word = '3.15'
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해주세요.')
# 아래에 코드를 작성하시오.
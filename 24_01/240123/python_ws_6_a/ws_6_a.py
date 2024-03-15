# 파이썬의 세트와 딕셔너리 데이터 타입의 특징을 이해하기 위해 코드 작성

my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

for i in my_set:
    print(my_dict.get(i))

var = (1, 2, 3,'A')
my_dict.setdefault(var, '변수로도 키 설정 가능')
print(my_dict)
# 아래에 코드를 작성하시오.
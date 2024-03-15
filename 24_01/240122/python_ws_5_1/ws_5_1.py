# 주어진 문자열을 역순으로 반환하는 reverse_string 함수를 작성하시오.
# 문자열을 인자로 받아 역순으로 된 문자열을 반환해야 한다.
# 슬라이싱을 사용할 수 없다. Builtin-Function reversed를 활용한다.
def reverse_string(i):
    i = i[::-1]
    return i


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

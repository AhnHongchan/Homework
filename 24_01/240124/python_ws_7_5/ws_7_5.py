# Shape 클래스에 __str__ 매직 메서드를 추가하여 인스턴스를 문자열로 표현할 수 있도록 코드를 작성하시오.
# 인스턴스를 생성하고 print 함수로 인스턴스를 출력한다.
class Shape:
    def __init__(self, wid, high):
        self.width = wid
        self.height = high

    def __str__(self):
        return f'Shape: width = {self.width}, height = {self.height}'

shape1 = Shape(5, 3)
print(shape1)

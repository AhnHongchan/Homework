# main.py


# Shape 클래스를 작성하시오. 이 클래스는 초기화 메서드를 가지며 가로와 세로 길이를 인자로 받아 속성으로 저장한다.
# 인스턴스를 생성하고 속성에 접근하여 값을 출력하시오.


class Shape():

    def __init__(self, wid, high):
        self.width = wid
        self.height = high
        


shape1 = Shape(5, 3)
print(shape1.width, shape1.height)

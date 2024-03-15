# Shape 클래스에 calculate_perimeter 메서드를 추가하여 사각형의 둘레를 계산하여 반환하시오.
# 인스턴스를 생성하고 calculate_perimeter 메서드를 호출하여 둘레를 출력한다.
class Shape:
    
    def __init__(self, wid, high):
        self.width = wid
        self.height = high
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)

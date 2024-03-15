# Shape 클래스에 calculate_area 메서드를 추가하여 사각형의 넓이를 계산하여 반환하시오
class Shape:

    def __init__(self, wid, high):
        self.width = wid
        self.height = high
    
    def calculate_area(self):
        return self.width * self.height


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)

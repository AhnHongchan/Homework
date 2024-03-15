# Shape 클래스에 print_info 메서드를 추가하여 사각형의 가로, 세로, 넓이, 둘레를 출력하시오.
# 인스턴스를 생성하고 print_info 메서드를 호출하여 정보를 출력한다.

class Shape:

    def __init__(self, wid, high):
        self.width = wid
        self.height = high

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def print_info(self):
        print(f'Width: {self.width} \nHeight: {self.height} \nArea: {self.width * self.height} \nPerimeter: {2 * (self.width + self.height)}')


shape1 = Shape(5, 3)
shape1.print_info()

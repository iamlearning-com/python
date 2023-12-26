'''
Viết một class Circle có một thuộc tính radius và hai property area và perimeter. 
Phương thức getter của area sẽ trả về diện tích của hình tròn, phương thức getter của perimeter sẽ trả về chu vi của hình tròn. 
Phương thức setter của area sẽ tính toán và gán giá trị cho radius dựa trên diện tích nhập vào, 
phương thức setter của perimeter sẽ tính toán và gán giá trị cho radius dựa trên chu vi nhập vào. 
Phương thức deleter của area và perimeter sẽ xóa thuộc tính radius và in ra một thông báo.
Test: 
    Tạo một đối tượng Circle với radius là 5
    In ra radius, area và perimeter của đối tượng c -> 5, 78.5398, 31.4159
    Thay đổi area của đối tượng c thành 50 -> 3.9899 50.0 25.0666
    Thay đổi perimeter của đối tượng c thành 20 -> 3.1830 31.8086 20.0
    Xóa area của đối tượng c -> AttributeError: 'Circle' object has no attribute 'radius'
'''
import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __str__(self):
        return f"Radius = {round(self.__radius, 4)}, Area = {round(self.area, 4)}, Perimeter = {round(self.perimeter, 4)}"

    @property
    def area(self):
        return math.pi * (self.__radius ** 2)

    @property
    def perimeter(self):
        return 2 * self.__radius * math.pi

    @area.setter
    def area(self, num_area):
        self.__radius = math.sqrt(num_area / math.pi)

    @perimeter.setter
    def perimeter(self, num_perimeter):
        self.__radius = num_perimeter / (2 * math.pi)

    @area.deleter
    def area(self):
        del self.__radius


if __name__ == "__main__":

    circle = Circle(5)
    print("Circle = 5:")
    print(circle)

    print("Area = 50:")
    circle.area = 50
    print(circle)

    print("Perimeter = 20:")
    circle.perimeter = 20
    print(circle)

    print("Delete Radius:")
    
    try:
        del circle.area
        print(circle.area)
        
    except AttributeError:
        print("AttributeError: 'Circle' object has no attribute 'radius'")

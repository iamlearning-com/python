'''
Viết một class Person có một thuộc tính name và một property age. 
Phương thức getter của age sẽ trả về giá trị của thuộc tính _age, 
phương thức setter của age sẽ kiểm tra xem giá trị nhập vào có phải là một số nguyên dương > không, 
nếu có thì gán cho thuộc tính _age, nếu không thì báo lỗi. 
Phương thức deleter của age sẽ xóa thuộc tính _age và in ra một thông báo.

Test: Tạo một đối tượng Person với name là "Alice" và age là 20
In ra name và age của đối tượng p -> Alice 20
Thay đổi age của đối tượng p thành 25 -> Alice 25
Xóa age của đối tượng p -> p.age (Alice AttributeError: 'Person' object has no attribute '_age')
'''
class Person:
    def __init__(self, name , age: int):
        self.__name = name
        self.__age = age
    
    @property
    def your_name(self):
        return self.__name
    
    @your_name.setter
    def your_name(self, name):
        self.__name = name

    @property
    def your_age(self):
        return self.__age
    
    @your_age.setter
    def your_age(self, age: int):
        if self.__age > 0:
            self.__age = age
        else:
            return "Invalid age"
    
    @your_age.deleter
    def your_age(self):
        del self.__age

if __name__ == "__main__":
    print("Testing programs\n", "-"*10)
    # Alice 20 tuoi
    peron = Person("Alice", 20)
    print(f"Name: {peron.your_name}, Age: {peron.your_age}")

    # Thay doi tuoi cua Alice thanh 25

    peron.your_age = 25
    print("Thay doi tuoi Alice thanh 25", end=" ")
    print(f"Name: {peron.your_name}, Age: {peron.your_age}")

    # Xoa tuoi cua Alice
    del peron.your_age
    try: 
        print(f"Xoa tuoi cua Alice {peron.your_age}")
    except AttributeError:
        print("Da xoa thanh cong tuoi cua Alice\n(Alice AttributeError: 'Person' object has no attribute)")
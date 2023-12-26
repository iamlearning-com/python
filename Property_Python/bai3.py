'''
Viết một class Employee có hai thuộc tính name và salary. Viết một property tax_rate có giá trị mặc định là 0.1
Viết một property tax_amount:
    phương thức getter của nó sẽ trả về số tiền thuế phải đóng dựa trên salary và tax_rate, 
    phương thức setter của nó sẽ tính toán và gán giá trị cho tax_rate dựa trên số tiền thuế nhập vào và salary, 
    phương thức deleter của nó sẽ xóa thuộc tính tax_rate và in ra một thông báo. 
Viết một property net_salary:
    phương thức getter của nó sẽ trả về số tiền lương sau khi trừ thuế, 
    phương thức setter của nó sẽ tính toán và gán giá trị cho salary dựa trên số tiền lương nhập vào và tax_rate, 
    phương thức deleter của nó sẽ xóa thuộc tính salary và in ra một thông báo.

Test:
    Tạo một đối tượng Employee với name là "Bob" và salary là 10000
    In ra name, salary, tax_rate, tax_amount và net_salary của đối tượng e -> Bob 10000 0.1 1000.0 9000.0
    Thay đổi tax_amount của đối tượng e thành 1500 -> Bob 10000 0.15 1500.0 8500.0
    Thay đổi net_salary của đối tượng e thành 8000 -> Bob 9411.764705882353 0.15 1411.764705882353 8000.0
    Xóa tax_amount của đối tượng e -> Bob 9411.764705882353 AttributeError: 'Employee' object has no attribute 'tax_rate'
'''

from a import tax_amount


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__tax_rate = 0.1

    @property
    def tax_rate(self):
        return self.__tax_rate

    @property
    def tax_amount(self):
        return self.__salary * self.__tax_rate

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_rate = value / self.__salary

    @tax_amount.deleter
    def tax_amount(self):
        del self.__tax_rate

    @property
    def net_salary(self):
        return self.__salary - self.tax_amount

    @net_salary.setter
    def net_salary(self, value):
        self.__salary = value / (1 - self.__tax_rate)

    @net_salary.deleter
    def net_salary(self):
        del self.__salary

    def __str__(self):
        return f"Name:{self.__name}, salary:{self.__salary}, tax_rate:{self.__tax_rate}, tax_amount:{self.tax_amount}, net_salary:{self.net_salary}"

e = Employee("Huy", 10000)
print(e)

e.tax_amount = 1500
print(e)

e.net_salary = 8000
print(e)

del e.tax_amount

del e.net_salary
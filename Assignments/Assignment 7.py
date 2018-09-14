#Qn 1
'''
class Employee:
    def __init__(self,name,number):
        self.name = name
        self.number = number

class ProductionWorker(Employee):
    def __init__(self,name,number,shift,pay):
        super().__init__(name,number)
        self.shift = shift
        self.pay = pay
    
    def set_name(self):
        self.name = name

    def set_number(self):
        self.number = number

    def set_shift(self):
        self.shift = shift

    def set_pay(self):
        self.pay = pay

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
    
    def get_shift(self):
        return self.shift
    
    def get_pay(self):
        return self.pay

def main():
    name = input('Name: ')
    number = input('Employee number: ')
    shift = int(input('Shift: '))
    pay = int(input('Pay: '))
    worker = ProductionWorker(name,number,shift,pay)
    print('worker name: {0}, employee number: {1}, shift: {2}, age: {3}'.format(worker.get_name(),worker.get_number(),worker.get_shift(),worker.get_pay()))

main()
'''

#Qn 2
'''
class Employee:
    def __init__(self,name,number):
        self.name = name
        self.number = number
class ShiftSupervisor(Employee):
    def __init__(self,name,number,salary,bonus):
        super().__init__(name,number)
        self.salary = salary
        self.bonus = bonus
'''

#Qn 3
'''
class Person:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

class Customer(Person):
    def __init__(self, name, address, number, mail = True):
        super().__init__(name, address, number)
        self.mail = mail

def main():
    mail = input("Be on a mailing list? True/False?")
    Customer = Customer('name','address','number',mail)
main()
'''

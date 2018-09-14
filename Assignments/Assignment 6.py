#Qn 1
'''
class Pet:
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = input('Enter name: ')
    Type = input('Enter animal type: ')
    age = input('Enter age: ')
    obj = Pet(name,Type,age) 
    print(obj.get_name(), 'is a', obj.get_animal_type(), 'and is', obj.get_age(),'years old.')

main()
'''

#Qn 2
'''
class Car:
    def __init__(self,model,make,speed=0):
        self.__year_model = model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    car = Car('Tesla','makeyourrmother')
    for x in range(5):
        car.accelerate()
        print(car.get_speed())
    
    for x in range(5):
        car.brake()
        print(car.get_speed())

main()
'''

#Qn 3
'''
class Data:
    def __init__(self,name,address,age,number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number

    def set_name(self,name):
        self.__name = name

    def set_address(self,address):
        self.__address = address

    def set_age(self,age):
        self.__age = age

    def set_number(self,age):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_number(self):
        return self.__number

def main():
    A = Data('Wei Hong','hci',99,12345678)
    B = Data('Rosie','trashbin',999,912831)
    C = Data('Yu peng','near taylor',1,1233445)
main()
'''

#Qn 4
'''
class RetailItem:
    def __init__(self,item,units,price):
        self.__item = item
        self.__units = units
        self.__price = price

def main():
    Item1 = RetailItem('Jacket',12,59.95)
    Item2 = RetailItem('Designer Jeans',40,34.95)
    Item3 = RetailItem('Shirt',20,24.95)

main()
'''
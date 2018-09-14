'''
class Beverage:
    def  __init__(self, bev_name):
        self.__bev_name = bev_name
        
    def __str__(self):
        return(self.__bev_name)

class Cola(Beverage):
    def __init__(self, bev_name):
        super().__init__(bev_name)

def main():
    coke = Cola('cola')
    print(coke.__str__())

main()
'''
'''
class Plant:
    def __init__(self,plant_type):
        self.__plant_type = plant_type

    def message(self):
        print("I'm a Plant")

class Tree(Plant):
    def __init__(Self):
        Plant.__init__(self,'tree')

    def message(self):
        print("I'm a tree")

def main():
    p=Plant('sapling')
    t = Tree()
main()
'''

class A:
    def __init__(self,name,gender):
        self.gender = gender
        self.name = name
    
    def __str__(self):
        return(self.name)

class B(A):
    def __init__(self,name,gender,age):
        super().__init___(name,gender)    # line 50 & line 51 is the same thing
        A.__init__(self,name,gender)      #making use of A's __init__
        #self.name=name, self.gender = gender (done by using super)
        self.__age = age
                                            

    def __str__(self):
        return('Age: '+str(self.__age) + ' Name: ' + self.name)    
    #def __str__(self):
    #    return(self.__age)
    #   return(self.gender)
    #    return(self.name)

def main():
    obj=B('abc','M',16)
    print(obj)
    # print(obj.__str__())
    
main()


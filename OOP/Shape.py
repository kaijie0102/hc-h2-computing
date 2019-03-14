import math
pi = math.pi
class Shape:
    def __init__(self,name):
        self.name = name
        
    def myname(self):                  #! Use __str__ when you want to return a string when printing an object
        return('I am '+ self.name)    
    
class Quadrilateral(Shape):
    def __init__(self,name,length,breadth):
        self.length = length
        self.breadth = breadth
        super().__init__(name)
        #self.name = name        #self.name = name replaced by super() 
                                 #there may be more than one arguement in __init__of Shape.
        
    def area(self):
        area = self.length * self.breadth
        return area

    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        return perimeter

class Circle(Shape):
    def __init__(self,,name,radius):
        self.radius = radius
        super().__init__(name)
    def __str__(self):
        area = pi * (self.radius**2)
        return('The area is {0}, my name is{1} '.format(str(area),self.name))
         

def main():
    # rect = Quadrilateral(3,4,'rectangle')
    # print(rect.__str__())       #using method of superclass 

#   print(rect.area())
#   print(rect.perimeter())
#    circle = Circle(1)
#    print(circle)
#    print(Shape('abc'))
    #print(shape)
    #print(Circle(1))

    shape = Shape('triangle')
    print(shape)
    

main()
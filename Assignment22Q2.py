
class circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circum=0.0


    def Accept(self):
        self.Radius=int(input("Enter radius of circle"))
        

    def CalculateArea(self):
        self.Area=circle.PI*self.Radius*self.Radius

        
    def CalculateCircumference(self):
        self.Circum=2*circle.PI*self.Radius

        
    def Display(self):
        print("Radius of Circle is ",self.Radius)
        print("Area of circle is :",self.Area)
        print("Circumference of circle is :",self.Circum)



def main():

    cobj1=circle()
    cobj1.Accept()
    cobj1.CalculateArea()
    cobj1.CalculateCircumference()
    cobj1.Display()


    cobj2=circle()
    cobj2.Accept()
    cobj2.CalculateArea()
    cobj2.CalculateCircumference()
    cobj2.Display()


    cobj3=circle()
    cobj3.Accept()
    cobj3.CalculateArea()
    cobj3.CalculateCircumference()
    cobj3.Display()

if __name__ =="__main__":
    main()


class circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circum=0.0


    def Accept(self,No):
        self.Radius=No
        

    def CalculateArea(self):
        self.Area=circle.PI*self.Radius*self.Radius

        
    def CalculateCircumference(self):
        self.Circum=2*circle.PI*self.Radius

        
    def Display(self):
        print("Radius of Circle is ",self.Radius)
        print("Area of circle is :",self.Area)
        print("Circumference of circle is :",self.Circum)



def main():

    print("Enter Radius of Circle :")
    Radi=int(input())

    cobj1=circle()
    cobj1.Accept(Radi)
    cobj1.CalculateArea()
    cobj1.CalculateCircumference()
    cobj1.Display()


    cobj2=circle()
    cobj2.Accept(Radi)
    cobj2.CalculateArea()
    cobj2.CalculateCircumference()
    cobj2.Display()


    cobj3=circle()
    cobj3.Accept(Radi)
    cobj3.CalculateArea()
    cobj3.CalculateCircumference()
    cobj3.Display()


    cobj4=circle()
    cobj4.Accept(Radi)
    cobj4.CalculateArea()
    cobj4.CalculateCircumference()
    cobj4.Display()



    

if __name__ =="__main__":
    main()
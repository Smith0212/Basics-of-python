class calculater :
    def __init__(self, num):
        self.num = num
        
    def square(self):
        print(f"The square of the {self.num} is {self.num **2}")

    def cube(self):
        print(f"The cube of the {self.num} is {self.num **3}")

    def squareRoot(self):
        print(f"The square of the {self.num} is {self.num **0.5}")

    @staticmethod
    def greet():
        print("hello, wlecome to my calculater :)")

a= int(input("Enter the number :"))

x = calculater(a)
x.greet()
x.square()
x.cube() 
x.squareRoot()



    
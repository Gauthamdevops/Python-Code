class Rectangle:
    def __init__(self,l,w):
        self.len=l
        self.wid=w
    def area(self):
        area=self.len*self.wid
        print("Area of rectangle %.2f"%area)
    def perimeter(self):
        p=2*(self.len+self.wid)
        print(p)
class Box(Rectangle):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.ht=h
    def volume(self):
        v=self.len*self.wid*self.ht
        print(v)
    def perimeter(self):
        p=4*(self.len+self.wid+self.ht)
        print(p)
a,b,c=[float(x) for x in input("enter 3 numbers: ").split()]
r1=Rectangle(a,b)
r1.area()
r1.perimeter()
b1=Box(a,b,c)
b1.volume()
b1.perimeter()

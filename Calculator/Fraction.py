import math
class Fraction:
    def __init__ (self, num=0,denum =1):
        assert denum != 0, "Denomunator cannot be 0"
        self.num = num
        self.denum = denum
        self.reduce()
    def reduce(self):
        gcd = math.gcd(self.num,self.denum) 
        self.num = int(self.num / gcd)
        self.denum = int(self.denum / gcd)
    def __repr__(self):
        return str(self.num) +'/'+str(self.denum)
    def __add__(self,other):
        return Fraction(self.num * other.denum + self.denum * other.num,\
            self.denum * other.denum)
    def __sub__(self,other):
        return Fraction(self.num * other.denum - self.denum * other.num,\
            self.denum * other.denum)
    def __mul__(self,other):
        return Fraction(self.num * other.num, self.denum * other.denum)
    def __div__(self,other):
        return Fraction(self.num*other.denum, self.denum * other.num)

a = Fraction(1,2)
b = Fraction(2,4)
c = Fraction(2,3)
d = Fraction(3,4)
    
    
class Polymonial:
    def __init__ (self,coefficient):
        """ 
        Initilazation object 
        @coefficience : list (int)
        """
        self.coefficient = coefficient
    def __doc__ (self):
        pass
    def __len__(self):
        """ get the highest power of polymonial"""
        return len(self.coefficient) - 1
    def __repr__ (self):
        ans = ''
        power = len(self)
        for co in self.coefficient:
            if co == 1:
                ans += '+ X^' +str(power)
            elif co != 0:
                ans += '+ '+str(co) + 'X^' +str(power)
            power -= 1
        return ans [2:]
    
    def __add__ (self,other):
        return Polymonial(list(map(lambda x,y: x+y,self.coefficient, other.coefficient)))
    def __sub__ (self,other):
        return Polymonial(list(map(lambda x,y: x-y,self.coefficient, other.coefficient)))
    def __eq__ (self,other):
        return self.coefficient == other.coefficient
if __name__ == "__main__":
    a = Polymonial([2,-2,2]) # 2x^2 + -2x + 2
    b = Polymonial([1,0,1]) # x^2 + 1
    c = a + b

import sys
sys.path.insert(0,'../classD')
print(sys.path)
from classD import D
class B:
    def __init__ (self):
        self.name = "B"
    def __str__ (self):
        return "This is a B class"

if __name__ == "__main__":
    d = D.D()
    b = B()
    print(str(b))
    print(str(d))
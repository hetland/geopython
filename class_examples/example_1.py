
from math import sqrt

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)

        
        
p1 = Point(1.0, 3.0)
p2 = Point(3.0, 4.0)

print 'p1 = ', p1.x, p1.y
print 'p2 = ', p2.x, p2.y

print 'p2.norm() = ', p2.norm()

p3 = p1 + p2
print 'p1 + p2 = ', p3
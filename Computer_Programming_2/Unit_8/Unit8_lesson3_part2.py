class Point:
    x = 0
    y = 0

    def __init__(self):
        pass


p1 = Point()
p2 = Point()
p1.x = 10
print(p1.x)
Point.x = 3
print(p1.x)
print(p2.x)
# p1 = Point() # (0,0)
# p2 = Point() # (0, 0)
#print(p2.x)
#print(p1.y)
class Point:
    
    num_points_created = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        Point.num_points_created += 1 # now If i print this it will print how many points I have created. To access
        #num_points_created I have to say .Point

p1 = Point()
p2 = Point()
p1.x = 3
p1.y = 4
print(p1.num_points_created) # One way of accessing the num_points_created that belongs to the class
print(Point.num_points_created) # Another way of accessing the num_points_created that belongs to the class
print(p2.num_points_created) # Another way of accessing the num_points_created that belongs to the class

# we don't have a variable x that belongs to the class, only to instances print(Point.x) causes an error

# x values across instances
print(p1.x) # should be 3
print(p2.x) # should be 0
print(Point.x) # should be error

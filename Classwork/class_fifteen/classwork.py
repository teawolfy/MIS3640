class Point:
    """Represents a point in 2-D space.
 
   attributes: x, y
   """
 
 
def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))
 
 
def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
 
   p1: Point
   p2: Point
 
   returns: float
   """
    import math
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    pass
 
 
class Rectangle:
    """Represents a rectangle.
 
   attributes: width, height, corner (bottom left corner of rectangle)
   """
 
 
def find_center(rect):
    """Returns a Point at the center of a Rectangle.
 
   rect: Rectangle
 
   returns: new Point
   """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p
 
 
def print_rectangle(rect):
    """Prints the width, height, and corner of a Rectangle object."""
    print('width: %d, height: %d' %(rect.width, rect.height))
    print('the lower-left corner is', rect.corner.x, rect.corner.y)
 
 
def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
 
   rect: Rectangle object.
   dwidth: change in width (can be negative).
   dheight: change in height (can be negative).
   """
    rect.width += dwidth
    rect.height += dheight
 
 
def get_corner(rect, corn):
    """Returns a corner of a rectangle as a Point object
   
   rect: Rectangle object
   corn: string describing location of desired corner
   """
    import copy
    my_corn = Point()
    my_corn = copy.copy(rect.corner)  
    if corn == 'botright':
        my_corn.x += rect.width
    if corn == 'topleft':
        my_corn.y += rect.height
    if corn == 'topright':
        my_corn.x += rect.width
        my_corn.y += rect.height
    return my_corn
 
 
class Circle:
    """Represents a circle.
 
   attributes: center, radius
   """
 
def point_in_circle(circ, checkpoint):
    """Checks if a point is within or on the boundary of a circle.
 
   circ: Circle object
   checkpoint: Point object to be checked
   """
    import math
    return distance_between_points(circ.center, checkpoint) <= circ.radius
 
 
def rect_in_circle(circ, rect):
    """Checks if a rectangle lies entirely in or on the boundary of a circle.
 
   circ: Circle object
   rect: Rectangle object
   """
    corner2 = Point()
    corner2 = get_corner(rect, 'botright')
    corner3 = Point()
    corner3 = get_corner(rect, 'topright')
    corner4 = Point()
    corner4 = get_corner(rect, 'topleft')
    return point_in_circle(circ, rect.corner) and point_in_circle(circ, corner2) and point_in_circle(circ, corner3) and point_in_circle(circ, corner4)
 
 
def rect_circle_overlap(circ, rect):
    """Checks if any corner of a rectangle lies in or on the boundary of a circle.
 
   circ: Circle object
   rect: Rectangle object
   """
    corner2 = Point()
    corner2 = get_corner(rect, 'botright')
    corner3 = Point()
    corner3 = get_corner(rect, 'topright')
    corner4 = Point()
    corner4 = get_corner(rect, 'topleft')
    return point_in_circle(circ, rect.corner) or point_in_circle(circ, corner2) or point_in_circle(circ, corner3) or point_in_circle(circ, corner4)
 
 
def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)
 
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
 
    center = find_center(box)
    print('center', end=' ')
    print_point(center)
 
    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)
 
    my_circle = Circle()
    my_circle.center = Point()
    my_circle.center.x = 150
    my_circle.center.y = 100
    my_circle.radius = 75
    my_checkpoint = Point()
    my_checkpoint.x = 150
    my_checkpoint.y = 175
    print(point_in_circle(my_circle, my_checkpoint))
 
    square = Rectangle()
    square.width = 75
    square.height = 75
    square.corner = Point()
    square.corner.x = 150
    square.corner.y = 100
    print(rect_in_circle(my_circle, square))
    print(rect_circle_overlap(my_circle, square))
 
 
if __name__ == '__main__':
    main()
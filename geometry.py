import math
#------------------------------------------------------------------
def square_area_perimeter() -> tuple[float, float]:
    """
    computes area and perimeter of square
    """
    side = float(input('\nEnter the side: '))

    area = side ** 2
    perimeter = side * 4

    return area, perimeter
#end def
#-------------------------------------------------------------------
def rectangle_area_perimeter() -> tuple[float, float]:
    """
    computes area and perimeter of rectangle
    """

    side1 = float(input('\nEnter side 1: '))
    side2 = float(input('Enter side 2: '))

    area = side1 * side2
    perimeter = (side1 + side2) * 2

    return area, perimeter
#end def
#-------------------------------------------------------------------
def triangle_area_perimeter() -> tuple[float, float]:
    """
    computes area and perimeter of triangle
      
    """
    side1 = float(input('\nEnter side 1: '))
    side2 = float(input('Enter side 2: '))
    side3 = float(input('Enter side 3: '))
    
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    try:
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    except ValueError:
        area = 0
    return area, perimeter
#end def
#------------------------------------------------------------------
def circle_area_perimeter() -> tuple[float, float]:
    """
    computes area and perimeter of circle
    """

    radius = float(input('\nEnter radius: '))

    area = math.pi * radius * radius
    perimeter = math.pi * radius * 2

    return area, perimeter
#end def
#-------------------------------------------------------------------
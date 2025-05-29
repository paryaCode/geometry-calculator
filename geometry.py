import math
#----------------------------------------------------------------------
def print_result(shape: str, value_type: str, value: float) -> None:
    """
    Prints the result (area or perimeter) for a given shape
    parameters: 
        - shape: 'square', 'circle', etc
        - value_type: 'area' or ;perimeter'
        - value: the numeric result
    """
    print('\n-------------------------------')
    print(f'{value_type.capitalize()} of {shape} is: {round(value, 2)}')
    print('-------------------------------')
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
    height = float(input('Enter height: '))

    area = (side1 * height) / 2
    perimeter = side1 + side2 + side3

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
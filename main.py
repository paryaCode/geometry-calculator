"""
    Area and Perimeter of geometric shapes 
"""
#------------------------------------------------------------------
from geometry import (
    square_area_perimeter,
    rectangle_area_perimeter,
    triangle_area_perimeter,
    circle_area_perimeter)
#------------------------------------------------------------------
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
#----------------------------------------------------------------------
def menu() -> int:  
    """
    Start menu
    """
    while True:
        print('\n-----< Start Menu >-----')
        print('1: Square')
        print('2: Rectangle')
        print('3: Triangle')
        print('4: Circle')
        print('5: Exit\n')

        selective_option = int(input('Select 1...5: '))

        if selective_option >= 1 and selective_option <= 5:
            return selective_option
#end def
#--------------------------------------------------------------------
def area_or_perimeter() -> int:
    while True: 
        print('\n-----< Menu selection >-----')
        print('1: area')
        print('2: perimeter')

        selective_option = int(input('\nSelect 1 or 2: '))

        if selective_option >= 1 and selective_option <=2:
            return selective_option
#--------------------------------------------------------------------
def main() -> None:
    while True:
        selective_option = menu()

        if selective_option == 5:
            print('\nThe End!')
            print('****************************************************************')
            break

        elif selective_option == 1:
            area, perimeter = square_area_perimeter()
            if area_or_perimeter() == 1:
                print_result('square', 'area', area)
            else:
                print_result('square', 'perimeter', perimeter)

        elif selective_option == 2:
            area, perimeter = rectangle_area_perimeter()
            if area_or_perimeter() == 1:
                print_result('rectangle', 'area', area)
            else:
                print_result('rectangle', 'perimeter', perimeter)
           
        elif selective_option == 3:
            area, perimeter = triangle_area_perimeter()
            if area_or_perimeter() == 1:
                print_result('triangle', 'area', area)
            else:
                print_result('triangle', 'perimeter', perimeter)

        elif selective_option == 4:
            area, perimeter = circle_area_perimeter()
            if area_or_perimeter() == 1:
                print_result('circle', 'area', area)
            else:
                print_result('circle', 'perimeter', perimeter)
#-------------------------------------------------------------------
if __name__ == "__main__":
    main()
#-------------------------------------------------------------------
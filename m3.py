"""
Final Examination, Winter 2013-2014.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Philip Ross.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import zellegraphics as zg


def main():
    """ Calls the   TEST   functions in this module. """
    test_rectangle_below_circle()
    test_many_rectangles_below_circles()


def test_rectangle_below_circle():
    """ Tests the   rectangle_below_circle   function. """
    #-------------------------------------------------------------------
    # DONE: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests on at least 2 windows.
    #   You might want to use the same tests as in picture_3a.pdf.
    #-------------------------------------------------------------------
    print()
    print('---------------------------------------------------------')
    print('Testing the   rectangle_below_circle   function.')
    print('See the graphics windows that pop up.')
    print('---------------------------------------------------------')
    window = zg.GraphWin('rectangle below circle', 600 , 600)
    circle = zg.Circle(zg.Point(300,300), 50)
    rectangle_below_circle(window, circle)
    
    window.closeOnMouseClick()

    window = zg.GraphWin('rectangle below circle', 600 , 600)
    circle = zg.Circle(zg.Point(200,400), 50)
    circle.setFill('hotpink')
    rectangle_below_circle(window, circle)
   
    window.closeOnMouseClick()

def rectangle_below_circle(window, circle):
    """
    See  picture_3a.pdf  in this project for pictures
    that may help you better understand the following specification:

    1.  Draws the given zg.Circle on the given zg.GraphWin (window).
    2.  Then draws a square directly below the zg.Circle,
          with the width and height of the square equaling the
          diameter of the zg.Circle.
          Furthermore, the fill color of the square should be the
          same as the fill color of the given zg.Circle.
    Preconditions: The first argument is a zg.GraphWin, and the second
         argument is a zg.Circle that fits inside the zg.GraphWin.
    """
    # DONE: 2b. Implement and test this function.
    circle.draw(window)
    radius = circle.radius
    p1 = zg.Point(circle.getP1().x, circle.getP1().y + 2 * radius)
    p2 = zg.Point(circle.getP2().x, circle.getP2().y + 2 * radius)
    
    rectangle = zg.Rectangle(p1,p2)
    rectangle.setFill(circle.getFill())
    rectangle.draw(window)

def test_many_rectangles_below_circles():
    """ Tests the   many_rectangles_below_circles  function. """
    #-------------------------------------------------------------------
    # DO NOT MODIFY the code in this function.  See the
    #     picture_3b.pdf   in this project
    # for pictures that show what these tests should produce.
    #-------------------------------------------------------------------
    print()
    print('---------------------------------------------------------')
    print('Testing the   many_rectangles_below_circles   function.')
    print('See the graphics windows that pop up.')
    print('---------------------------------------------------------')
    window1 = zg.GraphWin('many_rectangles_below_circles, test 1',
                          500, 300)

    point1 = zg.Point(250, 200)
    many_rectangles_below_circles(window1, point1, 20, 'red', 5)

    window1.closeOnMouseClick()

    window2 = zg.GraphWin('many_rectangles_below_circles, tests 2 and 3',
                          600, 400)

    point2 = zg.Point(150, 200)
    many_rectangles_below_circles(window2, point2, 25, 'blue', 3)

    point3 = zg.Point(400, 330)
    many_rectangles_below_circles(window2, point3, 10, 'yellow', 8)

    window2.closeOnMouseClick()


def many_rectangles_below_circles(window, point, radius, color, n):
    """
    See  picture_3b.pdf  in this project for pictures
    that may help you better understand the following specification:

    In the given zg.GraphWin (window), draws a circle centered
    at the given point, with the given radius and given fill color.
    Also draws a square directly below it, per
      the rectangle_below_circle
    function above.

    Then repeats this process to make a total of 2n-1 such
    circle/rectangle pairs in a "V" shape, as shown in the attached pdf.
    The original circle/rectangle pair is at the bottom of the "V".

    Preconditions: The first argument is a zg.GraphWin (window),
      the second argument is a zg.Point that fits reasonably in the
      given window, the third argument is a positive integer,
      the fourth argument is a color appropriate for zellegraphics,
      and the fifth argument is a positive integer.
    """
    # DONE: 3. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT: You must CALL your
    #    rectangle_below_circle   function above appropriately
    # in solving this problem.
    circle = zg.Circle(point, radius)
    circle.setFill(color)
    rectangle_below_circle(window, circle)
    for k in range(1,n):
        new_x_left = circle.getCenter().getX() - 2 * radius * k
        new_x_right = circle.getCenter().getX() + 2 * radius * k
        new_y = circle.getCenter().getY() - 2 * radius * k
        left_point = zg.Point(new_x_left, new_y)
        right_point = zg.Point(new_x_right, new_y)
        circle_left = zg.Circle(left_point, radius)
        circle_right = zg.Circle(right_point, radius)
        circle_left.setFill(color)
        circle_right.setFill(color)
        rectangle_below_circle(window, circle_left)
        rectangle_below_circle(window, circle_right)
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

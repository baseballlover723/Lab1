"""
Final Examination, Winter 2013-2014.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Philip Ross.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_shape()


def test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: (5, 8)')
    shape(5, 8)

    print()
    print('Test 2 of shape: (4, 6)')
    shape(4, 6)

    print()
    print('Test 3 of shape: (7, 7)')
    shape(7, 7)


def shape(r, m):
    """
    Prints a shape with r rows that looks like this example
    in which r = 5 and m = 8:
    +++++12345678
     ++++7654321
      +++123456
       ++54321
        +1234
    Note that the numbers in rows 1, 3, 5, ... always start at 1 and
    INCREASE, while the numbers in rows 2, 4, 6, ... DECREASE and always
    END at 1.

    Here is another example in which r = 4 and m = 6
    ++++123456
     +++54321
      ++1234
       +321

    Yet one more example, in which r=7 and m=7:
    +++++++1234567
     ++++++654321
      +++++12345
       ++++4321
        +++123
         ++21
          +1

    Preconditions:  r and m are positive integers with r <= m.
    For purposes of "lining up", assume m and n are single digits.
    """
    # DONE: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    for k in range(r):
        for i in range(k):
            print(' ', end='')
        for i in range(r-k):
            print('+', end='')
        if k % 2 == 0:
            for i in range(1,m+1-k):
                print(i, end='')
        else:
            for i in range(m-k, 0, -1):
                print(i, end= '')    
        
        print()
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

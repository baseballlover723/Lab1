"""
Final Examination, Winter 2013-2014.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Philip Ross.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the    test     functions in this module. """
    test_string_ends()


def test_string_ends():
    """ Tests the   string_ends   function. """
    print()
    print('------------------------------------------------------')
    print('Testing the   string_ends   function:')
    print('------------------------------------------------------')

    print()
    print("Test 1: Given ['one', 'two', 'three', 'four']")

    s1 = ['one', 'two', 'three', 'four']
    answer = string_ends(s1)

    print('   Answer returned was:', answer)

    correct_answer = 'eoer'
    if answer == correct_answer:
        print('   Answer returned is CORRECT.')
    else:
        print('   FAILED TEST. Answer should have been', correct_answer)

    print()
    print("Test 2: Given ('abc', 'xyz', 's', 'ttt', 'fifth')")

    s2 = ('abc', 'xyz', 's', 'ttt', 'fifth')
    answer = string_ends(s2)

    print('   Answer returned was:', answer)

    correct_answer = 'czsth'
    if answer == correct_answer:
        print('   Answer returned is CORRECT.')
    else:
        print('   FAILED TEST. Answer should have been', correct_answer)

    print()
    print("Test 3: []")

    s3 = []
    answer = string_ends(s3)

    print('   Answer returned was:', answer)

    correct_answer = ''
    if answer == correct_answer:
        print('   Answer returned is CORRECT.')
    else:
        print('   FAILED TEST. Answer should have been', correct_answer)


def string_ends(sequence_of_strings):
    """
    Given a sequence of strings, for example:
      ['one', 'two', 'three', 'four']
    returns a string that consists of the LAST character of each
    of the strings in the sequence, so 'eoer' in the above example.

    Another example:  Given ('abc', 'xyz', 's', 'ttt', 'fifth'),
    this function should return 'czsth'.

    Precondition: The argument is a sequence of non-empty strings.
    """
    # DONE: 2. Implement and test this function.
    last_string = ''
    for string in sequence_of_strings:
        last_string += string[-1]
    return last_string
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

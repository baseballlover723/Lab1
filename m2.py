"""
Final Examination, Winter 2013-2014.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Philip Ross.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement the Elevator class below
#          (i.e., replace each "pass" by relevant code).
#          Test your methods by writing code in main that calls them.


def main():
    elevator = Elevator()
    print(elevator.people)
    
    elevator.people_enter(10)
    print(elevator.people)
    
    elevator.people_exit(6)
    print(elevator.people)
    
    print('correct answer =', 4 * 150, 'my answer =', elevator.total_weight())
    
    elevator2 = Elevator()
    elevator2.people_enter(10)
    
    print(elevator.fuller_elevator(elevator2).people)
    
    elevator3 = Elevator()
    
    elevator4 = Elevator()
    elevator4.people_enter(2)
    
    elevators = [elevator2, elevator3, elevator4]
    
    print(elevator.total_people(elevators))
class Elevator():
    def __init__(self):
        """ An Elevator starts out with no people in it. """
        self.people = 0

    def people_enter(self, m):
        """
        The given number of people enter this Elevator.
        Precondition: The argument m is a positive integer.
        """
        self.people += m

    def people_exit(self, n):
        """
        The given number of people exit this Elevator.
        Precondition: The argument n is a positive integer that is
        not more than the current number of people in this Elevator.
        """
        self.people -= n

    def total_weight(self):
        """
        Returns the total weight of the people in this Elevator,
        assuming that each person weights 150 pounds.
        For example, if there are 6 people in this Elevator,
        this method returns 6 x 150, which is 900.
        """
        return (self.people * 150)

    def fuller_elevator(self, other_elevator):
        """
        Returns this Elevator or the other_elevator, whichever has
        more people in it.  If tied, you can return either Elevator
        (your choice).
        Precondition: The argument  other_elevator  is an Elevator.
        """
        if other_elevator.people > self.people:
            return other_elevator
        else:
            return self

    def total_people(self, elevators):
        """
        Returns the total number of people in this Elevator and in
        the given LIST of elevators.  For example, if this Elevator
        contains 4 people, and the given list of Elevators has three
        Elevators that contain 10, 0 and 2 people, respectively,
        then this function returns 4 + 10 + 0 + 2, which is 16.
        Precondition: the argument  elevators  is a LIST of Elevators.
        """
        total_people = self.people
        for elevator in elevators:
            total_people += elevator.people
        return total_people

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

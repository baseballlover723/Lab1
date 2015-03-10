"""
Final Examination, Winter 2013-2014.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Philip Ros.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """
    See   m1.mov   in this project for a short video that may
    help you better understand the following specification:

    Using tkinter/ttk (NOT zellegraphics), displays a window with a
    frame on it.  On the frame there appears:
      -- 1 Entry box
      -- 4 Buttons, labeled REMEMBER, SHOW REMEMBERED,
                            SHOW ENTRY, and SHOW MAX
      -- 1 Label which begins blank.

    Pressing the:
      -- REMEMBER Button causes whatever is in the Entry box
           to be "remembered".  (The user should enter only numbers
           in the Entry box.)
      -- SHOW REMEMBERED button makes the Label display whatever
           was most recently remembered.
      -- SHOW ENTRY button makes the Label display whatever
           is currently in the Entry box.
      -- SHOW MAX button makes the Label display the largest number
           ever remembered.
    If the SHOW REMEMBERED or SHOW MAX buttons are pressed before the
    REMEMBER button is pressed, then the Label should display the
    empty string.
    """
    # DONE: 2. Implement and test this function.
    # You can (and should!) define additional functions and classes
    # as appropriate.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=(30, 10), relief='raised')
    main_frame.grid()
    
    numbers = []
    
    entry = ttk.Entry(main_frame)
    entry.grid(pady = 5)
    
    remember_button = ttk.Button(main_frame, text = 'Remember')
    remember_button.grid(pady = 5)
    remember_button['command'] = lambda: remember(entry, numbers)
    
    show_remember_button = ttk.Button(main_frame, text = 'Show Remembered')
    show_remember_button.grid(pady = 5)
    show_remember_button['command'] = lambda: show_remembered(numbers, label)
    
    show_entry_button = ttk.Button(main_frame, text = 'Show Entry')
    show_entry_button.grid(pady = 5)
    show_entry_button['command'] = lambda: show_entry(entry, label)
    
    show_max_button = ttk.Button(main_frame, text = 'Show Max')
    show_max_button.grid(pady = 5)
    show_max_button['command'] = lambda: show_max(numbers, label)
    
    label = ttk.Label(main_frame, text = '')
    label.grid(pady = 5)
    
    root.mainloop()
    
def remember(entry, numbers):
    numbers.append(float(entry.get()))
    
def show_remembered(numbers, label):
    if numbers != []:
        label['text'] = numbers[-1]
    else:
        label['text'] = ''
    
def show_entry(entry, label):
    if entry.get() != '':
        label['text'] = float(entry.get())
    else:
        label['text'] = ''
def show_max(numbers, label):
    if numbers != []:
        max_number = numbers[0]
        for k in range(1,len(numbers)):
            number = numbers[k]
            if number > max_number:
                max_number = number
        label['text'] = max_number
    else:
        label['text'] = ''
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

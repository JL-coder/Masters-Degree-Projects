from tkinter import *

def main():
    root = Tk()
    root.title("CS 5007")
    root.resizable(width=True, height=False)

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(menu = file_menu, label="File") # It is part of a series of waterfalls
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label = "Exit", command = root.quit)

    root.configure(menu = menu_bar)

    # By default, the frame is resizable.
    # Create a Menu widget and add it to the root window right at the top of the window

    # create a pull-down menu, and add it to the menu bar

    # The first position (position 0) in the list of choices is occupied by the tear-off element,
    # and the additional choices are added starting at position 1. If you set tearoff=0,
    # the menu will not have a tear-off feature, and choices will be added starting at position 0.

    # Creates a new hierarchical menu by associating a given menu to a parent menu

    # Configuration Operations control how the widget is displayed

    root.mainloop()

if __name__ == "__main__":
    main()
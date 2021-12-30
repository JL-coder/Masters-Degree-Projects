from tkinter import * # Only the direct functions and classes under the tkinter module.
from tkinter import ttk # Use the functions and classes in the sub-module, need to the explict import.

def main():
    root = Tk()

    # Try to add same button twice, doesn't work
    # side − Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.

    button1 = ttk.Button(root)
    button1.configure(text="Button 1")
    button1.pack(side=LEFT)
    # button1.pack(side=RIGHT)

    # correct way to add the same button twice (make another button - two different button objects)

    button2 = ttk.Button(root)
    button2.configure(text="Button 2")
    button2.pack(side=RIGHT)

    # The pack command tells your widgets to pack themselves into the window frame.
    # Notice that the window frame shrinks to the size needed to accommodate the two buttons.

    root.mainloop()

if __name__ == "__main__":
    main()
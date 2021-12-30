from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # The geometry() method defines the width, height and coordinates of top left corner of the frame
    # as below (all values are in pixels): top.geometry("widthxheight+XPOS+YPOS")

    # create a two check buttons (check boxes)
    # neither selected nor deselected
    check_button1 = ttk.Checkbutton(root, text="Check button 1")
    check_button2 = ttk.Checkbutton(root, text="Check button 2")

    # deselected
    control3 = IntVar()
    control3.set(0)

    # selected
    control4 = IntVar()
    control4.set(1)

    # create two check buttons that are mutually exclusive
    check_button3 = ttk.Checkbutton(root, variable=control3, text="Check Button 3")
    check_button4 = ttk.Checkbutton(root, variable=control4, text="Check Button 4")

    # display the check buttons
    check_button1.pack(side=TOP)
    check_button2.pack(side=TOP)
    check_button4.pack(side=BOTTOM)
    check_button3.pack(side=BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
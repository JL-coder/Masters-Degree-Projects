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
    # as below (all values are in pixels): top.geometry("+XPOS+YPOS")

    # control group for buttons 1, 2, 3, 4
    control = IntVar()
    # If the control variable is an IntVar, give each radiobutton in the group a different integer value option.
    # If the control variable is a StringVar, give each radiobutton a different string value option.
    control.set(2) # initializing the choice, i.e., Radio button 2, that is pre-selected first, as its value = 2

    # create a four radio buttons that are in the same button group (same control variable)
    # 4 buttons will function as separate buttons (different values)
    radio_button1 = ttk.Radiobutton(root, value=1, variable=control, text="Radio button 1")
    radio_button2 = ttk.Radiobutton(root, value=2, variable=control, text="Radio button 2")
    radio_button3 = ttk.Radiobutton(root, value=3, variable=control, text="Radio Button 3")
    radio_button4 = ttk.Radiobutton(root, value=4, variable=control, text="Radio Button 4")

    # display the radio buttons
    radio_button1.pack(side=TOP)
    radio_button2.pack(side=TOP)
    radio_button4.pack(side=BOTTOM)
    radio_button3.pack(side=BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
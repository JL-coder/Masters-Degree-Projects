from tkinter import *
from tkinter import ttk
from tkinter import font

def main():

    root = Tk()

    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # The geometry() method defines the width, height and coordinates of top left corner of the frame
    # as below (all values are in pixels): top.geometry("widthxheight+XPOS+YPOS")

    # default text with is 20
    text_field1 = ttk.Entry(root)

    # 50 characters long
    text_field2 = ttk.Entry(root)
    text_field2["width"] = 50

    # disabled
    text_field3 = ttk.Entry(root)
    text_field3.state(["disabled"])

    # default text
    text_field4 = ttk.Entry(root)
    text_control = StringVar()
    text_control.set("ENTER TEXT HERE")
    text_field4["textvariable"] = text_control
    # x = StringVar() Holds a string; default value ""
    # x = IntVar() Holds an integer; default value 0
    # x = DoubleVar() Holds a float; default value 0.0
    # x = BooleanVar() Holds a boolean, returns 0 for False and 1 for True

    # different font
    # https://www.delftstack.com/howto/python-tkinter/how-to-set-font-of-tkinter-text-widget/
    text_field5_font = font.Font(family="Times New Roman", size=20, weight="bold")
    text_field5 = ttk.Entry(root, font=text_field5_font) # Allow you to type

    text_field1.grid(row=0, column=0)
    text_field2.grid(row=1, column=0)
    text_field3.grid(row=2, column=0)
    text_field4.grid(row=3, column=0)
    text_field5.grid(row=4, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()
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

    root.rowconfigure(0)
    root.columnconfigure(0)
    root.columnconfigure(1)

    # sticky -> means widget can be places or stretched within the limits of its bounding area
    # highlightcolor − Foreground color of the highlight region
    # highlightbackground − Background color of the highlight region

    left = Frame(root, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)

    # place frame on left on root
    left.grid(row=0, column=0, sticky=N+S+E+W)

    # give equal weight to all four rows on left frame
    left.rowconfigure(0, weight=1)
    left.rowconfigure(1, weight=1)
    left.rowconfigure(2, weight=1)
    left.rowconfigure(3, weight=1)

    # one column
    left.columnconfigure(0)

    button1 = ttk.Button(left, text="Button 1")
    button2 = ttk.Button(left, text="Button 2")
    button3 = ttk.Button(left, text="Button 3")
    button4 = ttk.Button(left, text="Button 4")

    # place on left
    button1.grid(row=0, column=0, sticky=N+S+E+W)
    button2.grid(row=1, column=0, sticky=N+S+E+W)
    button3.grid(row=2, column=0, sticky=N+S+E+W)
    button4.grid(row=3, column=0, sticky=N+S+E+W)

    right = Frame(root, highlightcolor="red", highlightbackground="red",  highlightthickness=5)

    # place frame on right of root
    right.grid(row=0, column=1, sticky=N+S+E+W)

    # give equal weight to the two rows (each row will contain another frame)
    right.rowconfigure(0, weight=1)
    right.rowconfigure(1, weight=1)

    # one column
    right.columnconfigure(0)

    # attached right_sub_top to right, give a huge border to demonstrate
    right_sub_top = Frame(right, highlightcolor="blue", highlightbackground="blue",  highlightthickness=5)

    # place frame on top of right frame
    right_sub_top.grid(row=0, column=0, sticky=N+S+E+W)

    # give equal weight to both rows and columns
    right_sub_top.rowconfigure(0)
    right_sub_top.rowconfigure(1)
    right_sub_top.columnconfigure(0)
    right_sub_top.columnconfigure(1)

    button5 = ttk.Button(right_sub_top, text="Button 5")
    button6 = ttk.Button(right_sub_top, text="Button 6")
    button7 = ttk.Button(right_sub_top, text="Button 7")
    button8 = ttk.Button(right_sub_top, text="Button 8")

    # place on top right
    button5.grid(row=0, column=0, sticky=N+S+E+W)
    button6.grid(row=0, column=1, sticky=N+S+E+W)
    button7.grid(row=1, column=0, sticky=N+S+E+W)
    button8.grid(row=1, column=1, sticky=N+S+E+W)

    # attached right_sub_bottom, give a huge border to demonstrate
    right_sub_bottom = Frame(right, highlightcolor="green", highlightbackground="green", highlightthickness=5)

    # place frame on bottom of right frame
    right_sub_bottom.grid(row=1, column=0, sticky=N+S+E+W)

    # place frame on bottom of right frame
    right_sub_bottom.rowconfigure(0)
    right_sub_bottom.rowconfigure(1)
    right_sub_bottom.columnconfigure(0)
    right_sub_bottom.columnconfigure(1)

    button9 = ttk.Button(right_sub_bottom, text="Button 9")
    button10 = ttk.Button(right_sub_bottom, text="Button 10")
    button11 = ttk.Button(right_sub_bottom, text="Button 11")
    button12 = ttk.Button(right_sub_bottom, text="Button 12")

    # place on bottom right
    button9.grid(row=0, column=0, sticky=N+S+E+W)
    button10.grid(row=0, column=1, sticky=N+S+E+W)
    button11.grid(row=1, column=0, sticky=N+S+E+W)
    button12.grid(row=1, column=1, sticky=N+S+E+W)

    root.mainloop()

if __name__ == "__main__":
    main()
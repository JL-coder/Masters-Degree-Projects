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
    root.rowconfigure(1)
    root.rowconfigure(2)
    root.columnconfigure(0)
    root.columnconfigure(1)
    root.columnconfigure(2)

    button1 = ttk.Button(root, text="Button 1")
    button2 = ttk.Button(root, text="Button 2")
    button3 = ttk.Button(root, text="Button 3")
    button4 = ttk.Button(root, text="Button 4")
    button5 = ttk.Button(root, text="Button 5")
    button6 = ttk.Button(root, text="Button 6")
    button7 = ttk.Button(root, text="Button 7")
    button8 = ttk.Button(root, text="Button 8")
    button9 = ttk.Button(root, text="Button 9")

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    root.mainloop()

if __name__ == "__main__":
    main()
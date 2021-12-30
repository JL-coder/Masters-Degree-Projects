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

    # attach label to root window
    label1 = ttk.Label(root)

    # set the text of the label1
    label1["text"] = "My Label 1"

    # create a style for the label1
    label1_style = ttk.Style()

    # configure a style for label1
    label1_style.configure("label1.TLabel", background="blue", foreground="yellow",
                           font=("Times New Roman", 40))
    label1.configure(style="label1.TLabel")

    # create second label with text and font specified
    label2 = ttk.Label(root, text="My Label 2", background="blue", foreground="yellow",
                       font=font.Font(family="Times New Roman", size=40))

    # display the label using pack layout
    label1.pack(side=TOP)
    label2.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
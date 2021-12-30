from tkinter import *
from tkinter import ttk

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

    # create a text area
    # words will wrap onto the next line (instead of horizontally scrolling until a return character is reached)
    # height = 10 = number of lines to display at a time
    # width = 50 = number of characters per line
    text1 = Text(root, wrap=WORD, height=10, width=50)

    # create a vertical scrollbar
    # text.yview will be called when scrollbar changes
    # set text yscrollcommand option to scrollbar set method, set method will be called when text view changes
    y_scrollbar = ttk.Scrollbar(root, command=text1.yview, orient=VERTICAL) # yview moves when scrollbar moves
    text1["yscrollcommand"] = y_scrollbar.set # scroll bar updated when text is added/removed

    # column − The column to put widget in; default 0 (leftmost column).
    # row − The row to put widget in; default the first row that is still empty.
    # By default, with sticky='', widget is centered in its cell.
    y_scrollbar.grid(row=0, column=1, sticky=N+S)
    text1.grid(row=0, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()
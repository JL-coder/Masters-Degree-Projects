from tkinter import *
from tkinter import ttk

# The "1.0" here represents where to insert the text, and can be read as "line 1, character 0".
# This refers to the first character of the first line
def enter_release_text_handler(event):
    print("Text entered = \n" + event.widget.get("1.0", END))

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

    text1 = Text(root, wrap=WORD, height=10, width=50)
    y_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text1.yview)
    text1["yscrollcommand"] = y_scrollbar.set

    text1.grid(row=0, column=0)
    y_scrollbar.grid(row=0, column=1, sticky=N+S) #N+S: fill the arrow vertically in both north and south direction

    # Return: Press the <Enter> key and Release to call the event handler
    text1.bind("<KeyRelease-Return>", enter_release_text_handler)

    root.mainloop()

if __name__ == "__main__":
    main()
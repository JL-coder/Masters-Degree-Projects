from tkinter import *
from tkinter import ttk

# char: To print the single character when the key is released.
def key_release_handler(event):
    print("Character released = " + event.char)

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

    text_field1 = ttk.Entry(root)
    text_field1.grid(row=0, column=0)
    text_field1.bind("<KeyRelease>", key_release_handler) # Release the key to call the event handler.

    root.mainloop()

if __name__ == "__main__":
    main()
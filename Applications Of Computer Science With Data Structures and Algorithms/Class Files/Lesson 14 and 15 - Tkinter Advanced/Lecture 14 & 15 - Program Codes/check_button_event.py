from tkinter import *
from tkinter import ttk

def button1_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.instate(statespec=["selected"])))

def button2_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.instate(statespec=["selected"])))

def button_lambda_handler(widget):
    print(widget["text"] + " Selected = " + str(widget.instate(statespec=["selected"])))
    print()

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

    control1 = IntVar()
    control1.set(0)

    control2 = IntVar()
    control2.set(0)

    check_button1 = ttk.Checkbutton(root, variable=control1, text="Check Button 1",
                                    command=lambda : button_lambda_handler(check_button1)) # After
    check_button1.bind("<Button-1>", button1_handler) # Before and During

    check_button2 = ttk.Checkbutton(root, variable=control2, text="Check Button 2",
                                    command=lambda : button_lambda_handler(check_button2)) # After
    check_button2.bind("<Button-1>", button2_handler) # Before and During

    check_button1.pack(side=TOP)
    check_button2.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
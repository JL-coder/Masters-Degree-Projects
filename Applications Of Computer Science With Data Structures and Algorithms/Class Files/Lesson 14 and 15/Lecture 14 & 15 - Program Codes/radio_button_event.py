from tkinter import *
from tkinter import ttk

# prints out the state of the radio button
# instate: Test the widget’s state BEFORE AND DURING the state changes by the event(BEFORE and
# DURING selecting the radio button)
def button1_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.instate(statespec=["selected"])))

def button2_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.instate(statespec=["selected"])))

# Prints state AFTER Radio button state changes
def button_lambda_handler(widget):
    print("Lambda: " + widget["text"] + " Selected = " + str(widget.instate(statespec=["selected"])))
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

    control = IntVar()
    control.set(2) #Radio Button 2 is pre-selected because value=2

    # The lambda is assigned to the command parameter.
    # This particular lambda is a method that calls another method, i.e., button_lambda_handler() in our example.
    radio_button1 = ttk.Radiobutton(root, value=1, variable=control, text="Radio Button 1",
                                    command=lambda : button_lambda_handler(radio_button1)) # After
    radio_button1.bind("<Button-1>", button1_handler) # Before and During

    radio_button2 = ttk.Radiobutton(root, value=2, variable=control, text="Radio Button 2",
                                    command=lambda : button_lambda_handler(radio_button2)) # After
    radio_button2.bind("<Button-1>", button2_handler) # Before and During

    radio_button1.pack(side=TOP)
    radio_button2.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
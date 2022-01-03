from tkinter import *
from tkinter import ttk

def button_handler(event): # Handler for all the widget objects of All Classes
    print("Button Clicked")

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

    # attach button2 to root window
    button1 = ttk.Button(root, text="Button 1")
    button2 = ttk.Button(root, text="Button 2")

    control = IntVar()
    control.set(1)

    # create two radio buttons that are mutually exclusive (different value)
    # also create a separate group for these buttons (same variable)
    radio_button1 = ttk.Radiobutton(root, value=1, variable=control, text="Radio Button 1")
    radio_button2 = ttk.Radiobutton(root, value=2, variable=control, text="Radio Button 2")

    # create a style for the button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()

    # configure button styles called button1 and button2
    button_style1.configure('button1.TButton', font=("Times New Roman", 20))
    button_style2.configure('button2.TButton', font=("Times New Roman", 20))

    # set button1 and button2 to have the "button1" and "button2" styles
    button1.configure(style='button1.TButton')
    button2.configure(style='button2.TButton')

    button1.bind_all("<Button-1>", button_handler) # <Button-3> also works because of button2
    button2.bind_all("<Button-3>", button_handler) # <Button-1> also works because of button1
    # button1, button2, radio_button1, and radio_button2 all are bound to <Button-1> and <Button-3>

    # display the buttons using pack layout
    button1.pack(side=TOP)
    button2.pack(side=TOP)
    radio_button1.pack(side=TOP)
    radio_button2.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
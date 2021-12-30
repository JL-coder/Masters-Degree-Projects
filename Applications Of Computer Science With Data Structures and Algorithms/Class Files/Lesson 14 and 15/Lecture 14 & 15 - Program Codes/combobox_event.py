from tkinter import *
from tkinter import ttk

# get(): To fetch the current selected value.
def combobox_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.get()))

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

    combo_box1 = ttk.Combobox(root, text="Combo Box")
    combo_box1.state(["readonly"])
    combo_box1["values"] = ["Choice 1", "Choice 2", "Choice 3", "Choice 4", "Choice 5"]
    combo_box1.current(0)

    # The combobox widgets generates a <<ComboboxSelected>> virtual event
    # WHEN the user selects an element from the list of values.
    combo_box1.bind("<<ComboboxSelected>>", combobox_handler) # Select one of the choices to call the handler

    combo_box1.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
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

    # create a two combo boxes
    combo_box1 = ttk.Combobox(root)
    combo_box2 = ttk.Combobox(root)

    # combo boxes are typically not editable
    # One of (), “readonly”, or “disabled”.
    # In the “readonly” state, the value may not be edited directly, and the user can only selection of the values from the dropdown list.
    # In the () state, the text field is directly editable.
    # In the “disabled” state, no interaction is possible.
    # combo_box1.state()
    # combo_box1.state(["disabled"])
    combo_box1.state(["readonly"])
    combo_box2.state(["readonly"])

    combo_box1["values"] = ["11", "2", "3", "4", "5"]

    # set current selected index. 2 is the ** index value ** not the actual value.
    combo_box1.current(2)

    # get and print the value at a given index (ex: 0)
    print(combo_box1["values"]) # Tuple
    print(combo_box1["values"][0])
    print()

    # get and print value at currently selected index
    print(combo_box1.get())
    print()

    # get and print value at given index (all)
    for i in combo_box1["values"]:
        print(i)

    print()
    # set initial text
    combo_box2.set("Initial Text") # Heading

    # add list of strings to combo box
    c2_list = []
    for i in range(100):
        c2_list.append(str(i))

    combo_box2["values"] = c2_list

    # how many elements to display at once
    combo_box2["height"] = 5

    # display the combo boxes
    combo_box1.pack(side=TOP)
    combo_box2.pack(side=BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
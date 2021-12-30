from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    # attach button2 to root window
    button1 = ttk.Button(root)
    button2 = ttk.Button(root)

    # set the text of the button
    button1["text"] = "Button 1"
    button2["text"] = "Button 2"

    # create a style for the button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()

    # configure button styles called button1 and button2. widgetName.TButton is the standard.
    button_style1.configure("button1.TButton", foreground="red", font=("Times New Roman", 20))
    button_style2.configure("button2.TButton", foreground="blue", font=("Times New Roman", 20))

    # set button1 and button2 to have the "button1" and "button2" styles
    button1.configure(style="button1.TButton")
    button2.configure(style="button2.TButton")

    # display the buttons using pack layout
    button1.pack(side=BOTTOM)
    button2.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
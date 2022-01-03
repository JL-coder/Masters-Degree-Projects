from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    # attach button to root window
    button1 = ttk.Button(root)

    # set the text of the button
    button1["text"] = "Button 1"

    # create a style for the button
    button_style = ttk.Style()

    # configure a style for ALL buttons. TButton is the standard style name.
    button_style.configure("TButton", foreground="red", font=("Times New Roman", 20))

    # set button1 to have the "TButton" styles. Other names do not work
    button1.configure(style="TButton")

    # display the button using pack layout
    button1.pack(side=BOTTOM) # TOP, LEFT, RIGHT, and BOTTOM

    root.mainloop()

if __name__ == "__main__":
    main()
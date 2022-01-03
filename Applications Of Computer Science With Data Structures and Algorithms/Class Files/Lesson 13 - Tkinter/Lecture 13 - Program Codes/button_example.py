from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    # attach button2 to root window
    button1 = ttk.Button(root)
    button2 = ttk.Button(root)
    button3 = ttk.Button(root)
    button4 = ttk.Button(root)
    button5 = ttk.Button(root)

    # set the text of the button
    button1["text"] = "Python"
    button2["text"] = "Perl"
    button3["text"] = "C++"
    button4["text"] = "Java"
    button5["text"] = "C#"

    # create a style for the button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()
    button_style3 = ttk.Style()
    button_style4 = ttk.Style()
    button_style5 = ttk.Style()

    # configure button styles called button1 and button2
    button_style1.configure("button1.TButton", foreground="red", font=("Times New Roman", 20))
    button_style2.configure("button2.TButton", foreground="blue", font=("Times New Roman", 20))
    button_style3.configure("button3.TButton", foreground="red", font=("Times New Roman", 20))
    button_style4.configure("button4.TButton", foreground="blue", font=("Times New Roman", 20))
    button_style5.configure("button5.TButton", foreground="red", font=("Times New Roman", 20))

    # set button1 and button2 to have the "button1" and "button2" styles
    button1.configure(style="button1.TButton")
    button2.configure(style="button2.TButton")
    button3.configure(style="button3.TButton")
    button4.configure(style="button4.TButton")
    button5.configure(style="button5.TButton")

    # display the buttons using pack layout
    button1.pack(side=TOP)
    button2.pack(side=TOP)
    button3.pack(side=TOP)
    button4.pack(side=TOP)
    button5.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
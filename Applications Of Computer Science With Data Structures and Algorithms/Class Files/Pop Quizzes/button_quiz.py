from tkinter import *
from tkinter import ttk

# Please implement
def button_pressed_handler(event):
    print(event.widget["text"] + " Button pressed")

# Please implement
def button_released_handler(event):
    print(event.widget["text"] + " Button released")

def main():
    root = Tk()

    # position the GUI at the center of your screen
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    root.geometry("+{}+{}".format(positionRight, positionDown))

    # attach buttons to the root window
    python_button = ttk.Button(root, text="Python")
    perl_button = ttk.Button(root, text="Perl")
    Cplus_button = ttk.Button(root, text="C++")
    Java_button = ttk.Button(root, text="Java")
    Chash_button = ttk.Button(root, text="C#")
    # set the text of the buttons

    # create a style for each button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()
    button_style3 = ttk.Style()
    button_style4 = ttk.Style()
    button_style5 = ttk.Style()
    # configure a button style for each button, e.g., "Times New Roman", 20
    button_style1.configure("python_button.TButton", foreground="red", font=("Times New Roman", 20))
    button_style3.configure("Cplus_button.TButton", foreground="red", font=("Times New Roman", 20))
    button_style5.configure("Chash_button.TButton", foreground="red", font=("Times New Roman", 20))
    button_style2.configure("perl_button.TButton", foreground="blue", font=("Times New Roman", 20))
    button_style4.configure("Java_button.TButton", foreground="blue", font=("Times New Roman", 20))
    # set buttons to have their own styles
    python_button.configure(style = "python_button.TButton")
    Cplus_button.configure(style = "Cplus_button.TButton")
    Chash_button.configure(style = "Chash_button.TButton")
    perl_button.configure(style="perl_button.TButton")
    Java_button.configure(style ="Java_button.TButton")

    # bind all the buttons to the event handlers, including "<Button-1>", "<Button-3>", "<ButtonRelease-1>", and "<ButtonRelease-3>"
    python_button.bind("<Button-1>", button_pressed_handler)
    Cplus_button.bind("<Button-1>", button_pressed_handler)
    Chash_button.bind("<Button-1>", button_pressed_handler)
    perl_button.bind("<Button-1>", button_pressed_handler)
    Java_button.bind("<Button-1>", button_pressed_handler)
    python_button.bind("<ButtonRelease-1>", button_released_handler)
    Cplus_button.bind("<ButtonRelease-1>", button_released_handler)
    Chash_button.bind("<ButtonRelease-1>", button_released_handler)
    perl_button.bind("<ButtonRelease-1>", button_released_handler)
    Java_button.bind("<ButtonRelease-1>", button_released_handler)

    # display the buttons using pack layout
    Chash_button.pack(side=BOTTOM)
    Java_button.pack(side=BOTTOM)
    Cplus_button.pack(side=BOTTOM)
    perl_button.pack(side=BOTTOM)
    python_button.pack(side=BOTTOM)




    root.mainloop()

if __name__ == "__main__":
    main()
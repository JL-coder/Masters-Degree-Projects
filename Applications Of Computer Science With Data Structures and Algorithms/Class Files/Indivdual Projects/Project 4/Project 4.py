#Todo:
from tkinter import *
from tkinter import ttk
from tkinter import font

#Handler function. Prints contents of entry boxes to console when "enter" key is pressed.
def entry_key_release_handler(event):
    print("Text Entered = " + str(event.widget.get()))

#Handler function. Prints selected item from combobox to console
def combobox_handler(event):
    print(event.widget["text"] + "Selected = " + str(event.widget.get()))

#Handler function. Prints contents of text box to console when "enter" key is pressed.
def enter_release_text_handler(event):
    print("Text entered = " + event.widget.get("1.0", END))

#Handler function. Only when a checkbox is clicked (and turned on) the option within it will be printed to the console.
def check_button_handler(event):
    if event.widget.instate(statespec=["selected"]) == False:
        print(event.widget["text"] + " is selected")

#Handler function. When the radio button is clicked the option it represents will be printed to the console.
# This particular function handles the "update" button
def update_radio_button_handler(event):
    print("Receive updates = " + event.widget["text"])

#Handler function. When the radio button is clicked the option it represents will be printed to the console.
# This particular function handles the "email" button
def email_radio_button_handler(event):
        print("Receive emails = " + event.widget["text"])

#Handler function. Handles events related to the "submit" and "cancel" buttons. When button is clicked sends a message
# to the console that it was clicked with the name of the button
def bottom_buttons_handler(event):
    if event.widget["text"] == "Submit":
        print(event.widget["text"] + " clicked")
    else:
        print(event.widget["text"] + " clicked")


def main():

#Create root for the window, title the window "tk", and make the window resizeable.
    root = Tk()
    root.title("tk")
    root.resizable(width = True, height = True)

    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    #Request height/width of the window
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    #Requestion the height/width of the screen itself
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth)
    positionDown = int(root.winfo_screenheight() / 3 - windowHeight / 3)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Total of 6 frames. 2 widgets/frames are within one frame.
    #Top frame, colored pink, stickied to the center of its grid location.
    top_frame = Frame(root, highlightcolor="pink", highlightbackground="pink",  highlightthickness=5)
    top_frame.grid(row = 0, column = 0, sticky = 'news')

    #Middle frame, colored cyan, stickied to the center of its grid location
    mid_frame = Frame(root, highlightcolor="cyan", highlightbackground="cyan",  highlightthickness=5)
    mid_frame.grid(row = 1, column = 0, sticky = 'news')

    #Sub frame located on the left side of the middle frame, colored orange, stickied to the west of its grid location
    left_sub_frame = Frame(mid_frame, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)
    left_sub_frame.grid(row = 1, column = 0, sticky = W)

    #Sub frame located on the right side of the middle frame, colored green, stickied to the east of its grid location
    right_sub_frame = Frame(mid_frame, highlightcolor="green", highlightbackground="green",  highlightthickness=5)
    right_sub_frame.grid(row = 1, column = 1, sticky = E)

    #Text frame located directly beneath the middle frame, colored red, stickied to the center of its grid location
    text_frame = Frame(root, highlightcolor="red", highlightbackground="red",  highlightthickness=5)
    text_frame.grid(row = 2, column = 0, sticky = 'news')

    #Bottom frame located beneath the text frame, colored blue, stickied to the center of its grid location
    bottom_button_frame = Frame(root, highlightcolor="blue", highlightbackground="blue",  highlightthickness=5)
    bottom_button_frame.grid(row = 3, column = 0, sticky = 'news')

    #Configure the weight of widgets within the rows/cols.
    #Configures the weight of the root's rows/cols to be 1. Allows all the frames to stretch with the window.
    root.rowconfigure(0, weight = 1)
    root.columnconfigure(0, weight = 1)

    #Configures the weight of the top frame (containing all the entry boxes). Allows the entry boxes to stretch within
    # the frame. Used a ranged tuple to configure the boxes along the grid rows.
    top_frame.rowconfigure(tuple(range(6)), weight = 1)
    top_frame.columnconfigure(1, weight = 1)

    #Configures the weight of the middle frame. Keeps the subframes within it seperate.
    mid_frame.columnconfigure(0, weight = 1)

    #Configures the weight of the text frame. Allows it to stretch within the frame.
    text_frame.rowconfigure(0, weight = 1)
    text_frame.columnconfigure(0, weight=1)

    #Configures the weight of the bottom frame. Allows the buttons to stretch within the frame.
    bottom_button_frame.columnconfigure(0, weight = 1)
    bottom_button_frame.columnconfigure(1, weight = 1)

    # Labels for set of text entry boxes. Created sequentially along the grid. Default font style is Times New Roman.
    # Labels above the combobox are stickied to the north + west side of the frame.
    user_label = ttk.Label(top_frame, text = "User Name: ", font = ("Times New Roman", 12))
    user_label.grid(row = 0, sticky = N + W)

    first_name_label = ttk.Label(top_frame, text = "First Name: ", font = ("Times New Roman", 12))
    first_name_label.grid(row = 1, sticky = N + W)

    last_name_label = ttk.Label(top_frame, text = "Last Name: ", font = ("Times New Roman", 12))
    last_name_label.grid(row = 2, sticky = N + W)

    password_label = ttk.Label(top_frame, text = "Password: ", font = ("Times New Roman", 12))
    password_label.grid(row = 3, sticky = N + W)

    favorite_color_label = ttk.Label(top_frame, text = "Favorite Color: ", font = ("Times New Roman", 12))
    favorite_color_label.grid(row = 4, sticky = N + W)

    #Labels below the combobox. These are stickied to the South-West and South-East respectively.
    account_label = ttk.Label(top_frame, text = "Account Options: ", font = ("Times New Roman", 12))
    account_label.grid(row = 5, column = 0, sticky = SW)

    sports_label = ttk.Label(top_frame, text = "Sports (like to watch):", font = ("Times New Roman", 12))
    sports_label.grid(row = 5, column = 1, sticky = SE)

    #Second set of labels for email and updates. No need to sticky these labels. Font size is 10 instead of 12.
    updates_label = ttk.Label(left_sub_frame, text = "Updates: ", font = ("Times New Roman", 10))
    updates_label.grid(row = 6, column = 0)

    email_label = ttk.Label(left_sub_frame, text = "Notification Emails: ", font = ("Times New Roman", 10))
    email_label.grid(row = 6, column = 1)

    #Text entry boxes corresponding to each label. Stickied to the center and bound to a handler which will activate
    # when the entry key is pressed.
    entry1 = Entry(top_frame)
    entry1.grid(row = 0, column = 1, sticky = N+S+E+W)
    entry1.bind("<Return>", entry_key_release_handler)  # Press the enter key to call the event handler.

    entry2 = Entry(top_frame)
    entry2.grid(row = 1, column = 1, sticky = N+S+E+W)
    entry2.bind("<Return>", entry_key_release_handler)

    entry3 = Entry(top_frame)
    entry3.grid(row = 2, column = 1, sticky = N+S+E+W)
    entry3.bind("<Return>", entry_key_release_handler)

    entry4 = Entry(top_frame)
    entry4.grid(row = 3, column = 1, sticky = N+S+E+W)
    entry4.bind("<Return>", entry_key_release_handler)

    #Combo box, set the values in the combobox as a list, stickied the box to the center of the frame, set it to
    # read-only so user can't change anything. Box is bound to handler and will activate whenever the user selects an
    # item from the combobox
    color_combo_box = ttk.Combobox(top_frame, values = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Pink",
                                                        "White", "Black"])
    color_combo_box.grid(row = 4, column = 1, sticky = N+S+E+W)
    color_combo_box.current(0)
    color_combo_box.state(["readonly"])
    color_combo_box.bind("<<ComboboxSelected>>", combobox_handler)

    #Controls for radio buttons. Set to int value
    update_button_control = IntVar()
    email_button_control = IntVar()

    #Update Radio Buttons
    #Yes-update button set to its respective frame/control, given its text name and value. Assigned to its handler and
    # grid space
    yes_update_button = ttk.Radiobutton(left_sub_frame, variable = update_button_control, text = "Yes", value = "Yes")
    yes_update_button.bind("<Button-1>", update_radio_button_handler)
    yes_update_button.grid(row = 7)
    #No-update button set to its respective frame/control, given its text name and value. Assigned to its handler
    # and grid space
    no_update_button = ttk.Radiobutton(left_sub_frame, variable = update_button_control, text = "No", value = "No")
    no_update_button.bind("<Button-1>", update_radio_button_handler)
    no_update_button.grid(row = 8)
    #Email Radio Buttons
    #Yes email buttons set to its respective frame/control, given its text name and value. Assigned to its handler and
    # grid space
    yes_email_button = ttk.Radiobutton(left_sub_frame, variable = email_button_control, text="Yes", value="Yes")
    yes_email_button.grid(row=7, column = 1)
    yes_email_button.bind("<Button-1>", email_radio_button_handler)
    #No update button set to its respective frame/control, given its text name and value. Assigned to its handler and
    # grid space
    no_email_button = ttk.Radiobutton(left_sub_frame, variable = email_button_control, text="No", value="No")
    no_email_button.bind("<Button-1>", email_radio_button_handler)
    no_email_button.grid(row=8, column = 1)

    #Controls for check buttons
    #Deselects set as int variables
    deselected_baseball = IntVar()
    deselected_basketball = IntVar()
    deselected_football = IntVar()
    deselected_hockey = IntVar()

    #Selections were set to off using intvariables (0 = off)
    deselected_baseball.set(0)
    deselected_basketball.set(0)
    deselected_football.set(0)
    deselected_hockey.set(0)

    #Check buttons set into the right sub frame, set to a deselected checkbox variable, stickied to the center, and
    # bound to the handler
    check_button_baseball = ttk.Checkbutton(right_sub_frame, variable = deselected_baseball, text="Baseball")
    check_button_baseball.grid(row = 0, column = 0, sticky = N+E+W+S, pady = 10)
    check_button_baseball.bind("<Button-1>", check_button_handler)

    check_button_basketball = ttk.Checkbutton(right_sub_frame, variable = deselected_basketball, text="Basketball")
    check_button_basketball.grid(row = 0, column = 1, sticky = E + N + W + S)
    check_button_basketball.bind("<Button-1>", check_button_handler)

    check_button_football = ttk.Checkbutton(right_sub_frame, variable = deselected_football, text="Football")
    check_button_football.grid(row = 1, column = 0, sticky = E + N + W + S)
    check_button_football.bind("<Button-1>", check_button_handler)

    check_button_hockey = ttk.Checkbutton(right_sub_frame, variable = deselected_hockey, text="Hockey")
    check_button_hockey.grid(row = 1, column = 1, sticky = E + N + W + S)
    check_button_hockey.bind("<Button-1>", check_button_handler)

    #Giant text entry comments box.
    #Label for text entry comments box. Stickied to the west and font of Times New Roman 12pt.
    comments_label = ttk.Label(text_frame, text="Other Comments: ", font = ("Times New Roman", 12))
    comments_label.grid(row=0, sticky = W)
    #Text box - words wrap around to new line, set heght/width, stickied to the center, bound so that when enter key is
    # pressed text is outputted to the console
    text_box = Text(text_frame, wrap = WORD, height = 10, width = 50)
    text_box.grid(row = 1, sticky = 'news')
    text_box.bind("<Return>", enter_release_text_handler)
    #Scrollbar for text entry box. Set to be vertical and stickied to the north and south
    scrollbar = ttk.Scrollbar(text_frame, command = text_box.yview, orient = VERTICAL)
    scrollbar.grid(row = 1, column = 1, sticky = N + S)
    text_box["yscrollcommand"] = scrollbar.set

    #Bottom Buttons
    #Submit button - stickied to the east and west, set in the bottom frame, and bound to the event handler.
    submit_button = ttk.Button(bottom_button_frame, text = "Submit")
    submit_button.grid(row = 0, column = 0, sticky = E + W)
    submit_button.bind("<Button-1>", bottom_buttons_handler)
    #Cancel button - stickied to the east and west, set in the bottom frame, and bound to the event handler.
    cancel_button = ttk.Button(bottom_button_frame, text = "Cancel")
    cancel_button.grid(row = 0, column = 1, sticky = E + W)
    cancel_button.bind("<Button-1>", bottom_buttons_handler)

    root.mainloop()

if __name__ == "__main__":
    main()
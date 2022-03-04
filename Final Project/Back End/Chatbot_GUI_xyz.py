#Author Joshua L, Sreejani C, Xueying Z

#Note: That the GUI was created on a Mac platform and as such there are a few minor graphical issues that need to be resolved on Windows. 
#The startup window for some reason creates two window on Windows Pcs but does not on Mac. PLan to fix in future iterations.


#Import needed libraries. If the program is not running properly check the README for information on what libraries might need to be installed.
#In future iterations we should add try/except blocks here
import gui_integration
from tkinter import *
from scrolled_win import ScrolledWindow
import emoji
import webbrowser
from functools import partial

#Variables for holding URL statements and related responses
resp_2 = None
yt_url_resp = None
url_resp = ""

# emoji resource: https://www.geeksforgeeks.org/python-program-to-print-emojis/
# emoji resource: https://unicode.org/emoji/charts/full-emoji-list.html

#Emoji list for the emoji button
emoji_list = [":smiling_face:", ":grinning_face_with_big_eyes:", ":beaming_face_with_smiling_eyes:",
              ":smiling_face_with_halo:", ":winking_face:", ":star-struck:", ":face_blowing_a_kiss:",
              ":face_with_tongue:", ":zany_face:", ":face_with_hand_over_mouth:", ":lying_face:",
              ":pensive_face:", ":face_with_medical_mask:", ":face_with_thermometer:", ":sleepy_face:",
              ":loudly_crying_face:", ":crying_face:", ":pleading_face:", ":nauseated_face:", ":broken_heart:",
              ":weary_face:", ":pouting_face:", ":face_with_steam_from_nose:", ":face_with_symbols_on_mouth:",
              ":angry_face_with_horns:", ":face_screaming_in_fear:", ":confounded_face:", ":disappointed_face:",
              ":persevering_face:", ":anxious_face_with_sweat:"]

#Functon centers the chat window to the center of the screen
def position_to_center(win):
    #Requests the users screen width/height
    width = win.winfo_reqwidth()
    height = win.winfo_reqheight()
    #Does the math for calculating screen center
    right = int(win.winfo_screenwidth() / 2 - width / 2)
    down = int(win.winfo_screenheight() / 2 - height / 2)
    #Centers the window
    win.geometry("+{}+{}".format(right, down))

#Class for managing the chatbot gui
class ChatBotGUI:
    #Deine all the objects and variables being used includes window where the conversation takes places, scrollbars, userinput windows, and emoji buttons
    def __init__(self):
        self.user_name = ""
        self.conversation_win = None
        self.scrolled_win = None
        #The whole conversation between user and ChatBot is saved in a member self.all_conversations of class ChatBotGUI.
        self.all_conversations = []
        self.user_input = None
        self.emoji_button = None
        self.bottom_frame = None
        self.input_scrollbar = None
        self.root = Tk()
        position_to_center(win=self.root)

    #Function handles the initial start window where the user can type in their screen name. 
    #On windows Pcs there are two windows that get created on Mac there is one. Plan to fix in future iterations. 
    def start(self):
        #Creation of window including resizing options and color.
        welcome_win = Toplevel()
        welcome_win.title("Mental Health ChatBot")
        welcome_win.resizable(width=False, height=False)
        welcome_win.configure(width=300, height=200, highlightbackground = '#2165db', 	highlightcolor = '#2165db', highlightthickness = 5, bg = '#dde3ed')
        #Window's text labels
        name_label = Label(welcome_win,
                           text="Please enter your name:",
                           justify=CENTER, bg = '#dde3ed')
        name_label.place(relx=0.2, rely=0.2)
        #Entry box for window
        name_entry = Entry(welcome_win)
        name_entry.place(relx=0.2, rely=0.3)
        name_entry.focus()
        #Start button for the window. After user presses this move onto main chat window.
        start_button = Button(welcome_win, text="Start",
                              command=lambda: self.open_chat_win(welcome_win, name_entry.get()))
        start_button.place(relx=0.3, rely=0.45)
        position_to_center(win=welcome_win)

        self.root.mainloop()

    #Fuction handles the creation of text by both the bot and the user. This text will appear in the main chat window.
    def new_text(self, name, text, align):
        #Appends the user's entered screen name above the text window that is created.
        name_widget = Label(self.scrolled_win.scrollwindow, text=name, anchor=align, font=("Bree Serif", 12), foreground="orange")
        name_widget.pack(side=TOP, fill=X)
        self.all_conversations.append(name_widget)
        #Creates dynamic text_frame to store each dialog. Resizes based off the the size of the text that gets inputted into it. 
        #Text box changes color depending on if it comes from the user or the bot.
        text_frame = Frame(self.scrolled_win.scrollwindow)
        text_frame.pack(side=TOP, fill=X)
        text_len = int(emoji.demojize(text).count(":") / 2) + len(text) + 1
        text_bg = "#2165db" if name.startswith("ChatBot") else "#04cc65"
        if text_len < 30:
            text_widget = Text(text_frame, wrap=WORD, background=text_bg, width=text_len, height=1, font=("Bree Serif", 12),
                               relief=GROOVE, fg = 'white')
        elif 30 <= text_len < 210:
            text_widget = Text(text_frame, wrap=WORD, background=text_bg, width=30, height=text_len/30, font=("Bree Serif", 12),
                               relief=GROOVE, fg = 'white')
        else:
            text_widget = Text(text_frame, wrap=WORD, background=text_bg, width=30, height=text_len/20, font=("Bree Serif", 12),
                               relief=GROOVE, fg = 'white')
        text_widget.pack(side=LEFT if align == "nw" else RIGHT)
        text_widget.insert(END, text)
        text_widget.config(state=DISABLED)
        self.all_conversations.append(text_widget)

        self.scrolled_win.canv.update_idletasks()
        self.scrolled_win.canv.yview_moveto("1.0")
    
    #Main chat window for conversations between the user and the bot.
    def open_chat_win(self, welcome_win, name, action=None):
        #The main chat window is layered this is the bottom layer.
        self.user_name = name
        welcome_win.destroy()
        self.root.deiconify()
        self.root.title("Mental Health ChatBot")
        self.root.resizable(width=False, height=False)
        self.root.configure(width=400, height=400)
        #Top layer for the chat window. Handles where it was placed and the color.
        self.conversation_win = Frame(self.root, highlightbackground = '#2165db', 	highlightcolor = '#2165db', highlightthickness = 5)
        self.conversation_win.place(relheight=0.90, relwidth=1, rely=0, relx=0)
        self.scrolled_win = ScrolledWindow(parent=self.conversation_win)
        # Opening message from the bot. The number represents the text position
        # which had to be changed from 95 because there was a problem with sizing when transitioning from Mac to Windows.
        self.new_text(name="ChatBot" + " " * 78,
                      text="Hi, I am Anton. Nice to meet you " + self.user_name + ". What can I do for you today?",
                      align="nw")
        #Handles the positioning of the botton frame, location of the emoji button. 
        self.bottom_frame = Frame(self.root, highlightbackground = '#2165db', 	highlightcolor = '#2165db', highlightthickness = 5)
        self.bottom_frame.place(relheight=0.1, relwidth=1, rely=0.9, relx=0)
        self.emoji_button = Button(self.bottom_frame, command=self.__open_emoji_dialog, text=emoji.emojize(":grinning_face:"),
                                   width=1, height=2)
        self.emoji_button.pack(side=LEFT, fill=X)
        #Handles the location of the user input box along with the scrollbar,keybinding, and location
        self.user_input = Text(self.bottom_frame, width=60, height=3, wrap=WORD, highlightbackground="#2165db", highlightcolor="#2165db", highlightthickness=5)
        self.input_scrollbar = Scrollbar(self.bottom_frame, orient=VERTICAL, command=self.user_input.yview)
        self.input_scrollbar.pack(side=RIGHT, fill=Y)
        self.user_input["yscrollcommand"] = self.input_scrollbar.set
        self.user_input.pack(side=LEFT, fill=X)
        self.user_input.focus()
        self.user_input.bind("<KeyRelease-Return>", self.__send_message)
        position_to_center(win=self.root)
    
    #Handles creation of new buttons the chat window. Buttons are used to handle URLs.
    def new_button(self, name, text, align):
        #Creation of the button in a frame
        button_frame = Frame(self.scrolled_win.scrollwindow)
        button_frame.pack(side=TOP, fill=X)
        button_len = int(emoji.demojize(text).count(":") / 2) + len(text) + 1
        #Creates dynamic button_frame to store each url. Resizes based off the the size of the url that gets inputted into it. 
        #Text box changes color depending on if it comes from the user or the bot.
        text_bg = "#2165db" if name.startswith("ChatBot") else "#04cc65"
        if button_len < 30:
            button_widget = Button(button_frame, background=text_bg, width=button_len, height=1, font=("Bree Serif", 12),
                                   fg = 'white', text = text)
            button_widget.bind("<Button-1>", self.__on_click)
        else:
            button_widget = Button(button_frame, background=text_bg, width=30, height=int(button_len/20), font=("Bree Serif", 12),
                                   fg = 'white', text = text)
            button_widget.bind("<Button-1>", self.__on_click)
        #Error handling for button. Button needs these lines of code to show up in the chat but will display an error on the console. 
        #Does not effect perfromance in any way so the handling was implemented to take care of the console errors.
        try:
            button_widget.pack(side=LEFT)
            #Insert statement gives a attribute error but the button wont show up without it.
            button_widget.insert(END, text)
            button_widget.config(state=DISABLED)
        except AttributeError:
            pass
        self.all_conversations.append(button_widget)               
        self.scrolled_win.canv.update_idletasks()
        self.scrolled_win.canv.yview_moveto("1.0")
    #Function for opening up your desired webbrowser. NOTE: If you are using this 
    #application you might need to change this to the correct directory path of your desired webbrowser. Plan on fixing in future iterations
    def callback(self, url):
        # chrome path need to have fwd slash and not bkwd slash as in the windows file path
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    
    #Event handler for handling button clicks by the user's mouse.
    def __on_click(self, event):
        if url_resp != "":
            self.callback(url_resp)
        else:
            self.callback(yt_url_resp)

    #Function for handling emoji button
    def __open_emoji_dialog(self):
        emoji_win = Toplevel()
        emoji_win.title("Emoji")
        emoji_win.resizable(width=False, height=False)
        frame = None
        i = 0
        #For loop handles how many rows of emojis are displayed by the button
        for e in emoji_list:
            # row of emoji
            if i % 5 == 0:
                frame = Frame(emoji_win)
                frame.pack(side=TOP, fill=Y)
            button = Button(frame, command=lambda estring=e: self.__select_emoji(estring), width=1, height=2, text=emoji.emojize(e))
            button.pack(side=LEFT, fill=X)
            i += 1
        position_to_center(win=emoji_win)
    
    #Event handler for handling what happends when the user clicks on an emoji
    def __select_emoji(self, emojiString):
        self.user_input.insert(END, emoji.emojize(emojiString))

    #The main "guts" of the chatbot. Handles user input and chatbot responses.
    def __send_message(self, event):
        #Previously mentioned global variables
        global resp_2, url_resp, yt_url_resp
        
        #Variable for what the user input message
        msg = event.widget.get("1.0", END)
        
        #Hard coded responses from the bot. Used to push the conversation foward when the user inputs "I decline."
        #Will look into integrating into chatbot responses in future iterations and remove the need for hard coding,
        stored_response = "Understood! May I know where you live? You can give me your zip code just say \"My zip code is\" "
        age_response = "Thank you for answering. May I know where you live? You can give me your zip code just say \"My zip code is\" "
        
        #When the user inputs a message it enters the for loop. The message is pushed through semantic and sentimental analysis.
        if msg != '':
            res = gui_integration.chatbot_response(msg)[0]
            self.new_text(name=self.user_name, text=msg, align="ne")
            self.user_input.delete("1.0", END)
        # Call chatbot to return response.
            self.new_text(name="ChatBot", text=res, align="nw")
            #Checks a response from the chatbot. If the bot responds with this message then semantic and sentimental analysis is called.
            if res.endswith("I am sorry to hear that, here are some resources and suggestions that might help. Looking things up may take a few minutes. Please give me some time."):
                custom_response = gui_integration.give_url(msg)
                #If there is no url in the response from the bot
                if "https://www" not in custom_response:
                    self.new_text(name="ChatBot", text=custom_response, align="nw")
                #Otherwise if there is a url.
                else:
                    resp_1, resp_2 = custom_response.split(":", 1)
                    print(resp_1)
                    print(resp_2)                
                    self.new_text(name="ChatBot", text=resp_1, align="nw")
                    #Splits the creation of the url button when multiple links are being outputted by the bot.
                    if "youtube" not in resp_2:
                        resp_2 = [resp_2[:32], resp_2[32:]]
                        print(resp_2)
                        for i in resp_2:
                            url_resp += i
                            url_resp += "\n"
                        print(url_resp)
                        self.new_button(name="ChatBot", text=url_resp, align="nw")
                    #Handles the creation of a single button when one url is outputted by the bot.
                    else:
                        resp_2 = resp_2.split("\n")[:-1]
                        for i in resp_2:
                            i = [i[:24], i[24:]]
                            for j in i:
                                url_resp += j
                                url_resp+="\n"
                            self.new_button(name="ChatBot", text=url_resp, align="nw")
                            yt_url_resp = url_resp
                            print(url_resp)
                            url_resp = ""
            #Hard coded responses by the bot for when the user types "I decline" or their age. Used to push the conversation along.
            elif res.endswith("Thank you for answering."):
                response = "Can you please tell me about your occupation"
                self.new_text(name="ChatBot", text=response, align="nw")
            elif msg.endswith("i decline"):
                self.new_text(name="ChatBot", text = stored_response, align="nw")
            elif msg.endswith(" years old"):                    
                self.new_text(name="ChatBot", text=age_response, align="nw")  
                
#Main function starts the GUI        
def main():
    gui = ChatBotGUI()
    gui.start()

if __name__ == "__main__":
    main()

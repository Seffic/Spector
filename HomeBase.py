
#while(true):
    #get input from other pie
    #display  activity on screen browzer history GUI


#intturpt with GUI input
    #send commands to other pie
    #possible commands are renameSSID(string), end()

###############################################################
from Tkinter import *

class MainGUI(Frame):
        def __init__(self, master):
                Frame.__init__(self, master, bg="white")

        def start(self):
                self.setupGUI()
                self.setResponse("Welcome to Spector.")
                self.setImage()
                
                

        def setupGUI(self):
                # pack the GUI
                self.pack(fill=BOTH, expand=1)
                
                MainGUI.player_input = Entry(self, bg="white")
                MainGUI.player_input.bind("<Return>", self.process)
                MainGUI.player_input.pack(side=BOTTOM, fill=X)
                MainGUI.player_input.focus()

                # setup the watch frame of the GUI
                # first, the frame in which the text will be placed
                moniter_frame = Frame(self, width=WIDTH/2)
                #the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the frame's size
                img = None
                MainGUI.image = Label(self, width=WIDTH / 2, image=img)
                MainGUI.image.image = img
                MainGUI.image.pack(side=LEFT, fill=Y)
                MainGUI.image.pack_propagate(False)
                # setup the text to the right of the GUI
                # first, the frame in which the text will be placed
                text_frame = Frame(self, width=WIDTH)
                #the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the frame's size
                MainGUI.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                MainGUI.text.pack(fill=Y, expand=1)
                text_frame.pack(side=LEFT, fill=Y)
                text_frame.pack_propagate(False)



        def setResponse(self, response):
                 MainGUI.text.config(state=NORMAL)
                 MainGUI.text.delete("1.0", END)

                 MainGUI.text.insert(END,response)
                
                 MainGUI.text.config(state=DISABLED)

        def setImage(self):
                MainGUI.img = PhotoImage(file="skull.gif")
                # display the image on the left of the GUI
                MainGUI.image.config(image=MainGUI.img)
                MainGUI.image.image = MainGUI.img
                

        def process(self, event):
                # grab the player's input from the input at the bottom of
                # the GUI
                command = MainGUI.player_input.get()
                # set the user's input to lowercase to make it easier to
                # compare the verb and noun to known values
                command= command.lower()
                # set a default response
                response = "I don't understand."
                
                # exit the game if the player wants to leave (supports quit,
                # exit, and bye)
                if (command == "quit" or command == "exit" or command == "bye" or command == "sionara!"):
                    exit(0)

                elif(command == "ssh"):
                        response = "started ssh"

                elif(command == "scan"):
                        #sudo airodump-ng wlanX - gives list of mac addresses and channels
                        response = "scan started"

                elif(command == "twin"):
                        #sudo airbase-ng -a MAC ADDRESS --essid "Wifi Name" -c "channel #" wlanX:
                        response = "started twin"

                elif(command == "renamessid"):
                        # send to rename id
                        response = "renamed SSID"

                
                self.setResponse(response)
                MainGUI.player_input.delete(0, END)
                
               
                
                
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Spector")
# create the game as a Tkinter Frame inside the window
s = MainGUI(window)
s.start()
# wait for the window to close
window.mainloop()

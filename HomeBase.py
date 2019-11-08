###############################################################
#Names: Jace Ziegler, Cole Edwards, Stuart Redfearn
#Class: CSC 132-02
#Date: 11/6/2019
#Disc: program to opperate recon drone
###############################################################
from Tkinter import *
import paramiko
import time

class MainGUI(Frame):
        def __init__(self, master):
                Frame.__init__(self, master, bg="white")
                
        # call all needed functions to start
        def start(self):
                self.setupGUI()
                self.setResponse("Welcome to Spector.")
                
        def setupGUI(self):
                # pack the GUI
                self.pack(fill=BOTH, expand=1)

               # setup entry from to get entry from person 
                MainGUI.user_input = Entry(self, bg="white")
                MainGUI.user_input.bind("<Return>", self.process)
                MainGUI.user_input.pack(side=BOTTOM, fill=X)
                MainGUI.user_input.focus()


                # setup the text to the right of the GUI
                # the frame in which the text will be placed
                text_frame = Frame(self, width=WIDTH)
                # the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the frame's size
                MainGUI.text = Text(text_frame, bg="grey", state=DISABLED)
                MainGUI.text.pack(fill=Y, expand=1)
                text_frame.pack(side=LEFT, fill=Y)
                text_frame.pack_propagate(False)


        #sets respons on the text 
        def setResponse(self, response):
                #make text editable
                 MainGUI.text.config(state=NORMAL)
                 #delete prior text
                 MainGUI.text.delete("1.0", END)
                 #insert text
                 MainGUI.text.insert(END,response)
                 #reset disabled state
                 MainGUI.text.config(state=DISABLED)
                

        def process(self, event):
                #grab the input from the input at the bottom of the GUI
                command = MainGUI.user_input.get()

                #set the user's input to lowercase to make it easier to
                command= command.lower()

                #set a default response
                response = "I don't understand."
                
                 #exit the game if the user wants to leave (supports quit, exit, and bye)
                if (command == "quit" or command == "exit" or command == "bye" or command == "sionara!"):
                    exit(0)

                # puts wlan1 into moniter mode 
                elif(command == "moniter"):
                        # sudo airodump-ng wlanX - gives list of mac addresses and channels
                        stdin, stout, stderr = ssh.exec_command("iwconfig wlan1 mode monitor")
                        response = "scan started"

                # create the graph
                elif(command == "graph"):
                        # tell user to wait
                        self.setResponse("Wait")
                        MainGUI.user_input.delete(0, END)
                        # start arodump to find info
                        stdin, stout, stderr = ssh.exec_command('airodump-ng wlan1 -w "/root/Graphs"')
                        # wait 5 sec till controll + c
                        time.sleep(5)
                        stdin, stout, stderr = ssh.exec_command(chr(3))
                        # make the graph with info from arodump
                        time.sleep(3)
                        stdin, stout, stderr = ssh.exec_command("airgraph-ng -i '/root/Graphs-01.csv' -o '/root/Graphs-01' -g CAPR")
                        stdin, stout, stderr = ssh.exec_command(chr(3))
                        response = "graphed"

                        
                self.setResponse(response)
                MainGUI.user_input.delete(0, END)
                
               
                
                
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# credintals
password = "hd123"
host = "10.0.0.18"
users = "root"

# start ssh with paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = host, username = users, password = password)

window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Spector")
# create the game as a Tkinter Frame inside the window
s = MainGUI(window)
# call needed functions
s.start()
# wait for the window to close
window.mainloop()

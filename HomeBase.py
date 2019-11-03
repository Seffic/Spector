
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
                #master.attributes("-fullscreen", True)
                self.setupGUI()

        def setupGUI(self):
                self.text = Label(self.master,text = "Possible Commands: exit, renameSSID")
                self.text.pack
                # pack the GUI
                self.pack(fill=BOTH, expand=1)
                

        def process(self, command):
                if(command == "exit"):
                        #send command that exits spector program
                        sys.exit()
                elif(command == "renameSSID"):
                        # send to rename id
                        print "Renamed SSID."
##########################################################
                
window = Tk()
window.title("Spector")
# create the game as a Tkinter canvas inside the window
s = MainGUI(window)
s.setupGUI()
# wait for the window to close
window.mainloop()

# Main
# import all required
import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
from logins import *
from inputCorrection import *
from gets import *

TITLE_FONT = ("Verdana", 20)

# class DCM is used to controll all the pages
class DCM(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "CPU L8R")

        #container is the frame that we will populate depending on the page we need
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="True")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
#        self.minsize(400, 400)

        for F in (StartPage, RegisterPage, PageOne, AOO, VOO, AAI, VVI, DOO, AOOR, VOOR, AAIR, VVIR, DOOR):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #tkraise brings the page we want that's in the back to the front
        frame.tkraise()

#This is the initial log-in page
class StartPage(tk.Frame):

    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Welcome", font="TITLE_FONT").grid(row = 0, column=1, padx=30, pady=10)
        self.controller = controller
        self.username = tk.StringVar()  #variable to store username input later
        self.password = tk.StringVar()  #variable to store password input later
        ttk.Label(self, text="Username").grid(row = 1, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.username).grid(row = 1, column=1, padx=(20,40), pady=2)   #textbox input for username
        ttk.Label(self, text="Password").grid(row = 2, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.password).grid(row = 2, column=1, padx=(20,40), pady=2)   #textbox input for password

        ttk.Button(self, text="Log In", command=self.login).grid(row = 1, column=2, padx=10, pady=5)    #if button is pressed the login() method below is activated to check the password
        ttk.Button(self, text="New User?", command=lambda: controller.show_frame(RegisterPage)).grid(row = 4, column=1,padx=10, pady=5) #Button to the Register New User page

    def login(self):
        #Uses methods created in logins.py to verify user authentication, if not creates a popup
        if checkPassword(self.username.get(), self.password.get()):
            recent(self.username.get())
            self.controller.show_frame(PageOne)
        else:
            return alert('Incorrect Username or Password!')

#Page to register new users
class RegisterPage(tk.Frame):

    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Register", font="TITLE_FONT").grid(row = 0, column=1, padx=30, pady=10)
        self.controller = controller
        self.username = tk.StringVar()  #variable to store username
        self.password = tk.StringVar()  #variable to store password
        ttk.Label(self, text="Username").grid(row = 1, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.username).grid(row = 1, column=1, padx=(20,40), pady=2)
        ttk.Label(self, text="Password").grid(row = 2, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.password).grid(row = 2, column=1, padx=(20,40), pady=2)

        ttk.Button(self, text="Register", command=self.adduser).grid(row = 3, column=1, padx=10, pady=5)    #if button is pressed the adduser() method below is activated
        ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).grid(row = 4, column=1,padx=10, pady=5) #Button to go back to the StartPage

    #Method to register new users
    def adduser(self):
        if checkCountUsers() == False:  #check if there is space for new users, if not create an alert
            return alert('Too Many Users')
        elif register(self.username.get(), self.password.get()) == True:    #method from logins.py that registers new users. Returns true if registration was successful.
            return alert('Registration Successful')
        else:
            return alert('Invalid Input') #if logins.py returns false, that means a user with that username already exists


class PageOne(tk.Frame):

    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text= "WELCOME ", font="TITLE_FONT").grid(row = 0, column = 3)

        ttk.Label(self, text= "Modes:").grid(row = 1, column = 0)

        #Buttons to view all the modes
        AOO_button = ttk.Button(self, text="AOO", command=lambda: controller.show_frame(AOO))
        AOO_button.grid(row = 1, column = 1,  pady=(10,10), padx=(20,10))

        VOO_button = ttk.Button(self, text="VOO", command=lambda: controller.show_frame(VOO))
        VOO_button.grid(row = 1, column = 2,  pady=(10,10), padx=(10,10))

        AAI_button = ttk.Button(self, text="AAI", command=lambda: controller.show_frame(AAI))
        AAI_button.grid(row = 1, column = 3,  pady=(10,10), padx=(10,10))

        VVI_button = ttk.Button(self, text="VVI", command=lambda: controller.show_frame(VVI))
        VVI_button.grid(row = 1, column = 4,  pady=(10,10), padx=(10,10))

        DOO_button = ttk.Button(self, text="DOO", command=lambda: controller.show_frame(DOO))
        DOO_button.grid(row = 1, column = 5,  pady=(10,10), padx=(10,10))

        AOOR_button = ttk.Button(self, text="AOOR", command=lambda: controller.show_frame(AOOR))
        AOOR_button.grid(row = 2, column = 1,  pady=(10,50), padx=(20,10))

        VOOR_button = ttk.Button(self, text="VOOR", command=lambda: controller.show_frame(VOOR))
        VOOR_button.grid(row = 2, column = 2,  pady=(10,50), padx=(10,10))

        AAIR_button = ttk.Button(self, text="AAIR", command=lambda: controller.show_frame(AAIR))
        AAIR_button.grid(row = 2, column = 3,  pady=(10,50), padx=(10,10))

        VVIR_button = ttk.Button(self, text="VVIR", command=lambda: controller.show_frame(VVIR))
        VVIR_button.grid(row = 2, column = 4,  pady=(10,50), padx=(10,10))

        DOOR_button = ttk.Button(self, text="DOOR", command=lambda: controller.show_frame(DOOR))
        DOOR_button.grid(row = 2, column = 5,  pady=(10,50), padx=(10,10))

        #This Button creates a popup to view the most recent values
        RUN_button = ttk.Button(self, text="Run")
        RUN_button.grid(row = 20, column = 5,  pady=(10,10), padx=(10,10))

        #This Button creates a popup to view the most recent values
        VALUES_button = ttk.Button(self, text="Show Values", command=self.showValues)
        VALUES_button.grid(row = 20, column = 3,  pady=(10,10), padx=(10,10))

        LOGOUT_button = ttk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        LOGOUT_button.grid(row = 20, column = 0,  pady=(10,10), padx=(10,10))

    def showValues(self):  #Function to retrieve and display all the current inputs for the user

        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in using the getValue() method from gets
        mode = str(getValue(usr, "mode"))

        if mode == 'aoo':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'APW: '+str(getValue(usr, "APW")))

        elif mode == "voo":
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'   +'VPW: '+str(getValue(usr, "VPW")))

        elif mode == "aai":
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'APW: '+str(getValue(usr, "APW")) +'\n'    +'ARP: '+str(getValue(usr, "ARP")))

        elif mode =='vvi':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'   +'VPW: '+str(getValue(usr, "VPW")) +'\n'    +'VRP: '+str(getValue(usr, "VRP")))

        elif mode =='doo':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'      +'APW: '+str(getValue(usr, "APW")) +'\n'+
            'VPW: '+str(getValue(usr, "VPW"))+ '\n'  +'FAVD: '+str(getValue(usr, "FAVD")))

        elif mode == 'aoor':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'APW: '+str(getValue(usr, "APW")) +'\n' +'MSR: '+str(getValue(usr, "MSR"))+ '\n'    +
            'AT: '+str(getValue(usr, "AT")) +'\n'+  'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n' +'RF: '+str(getValue(usr, "RF"))+ '\n'+
            'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')

        elif mode == 'voor':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'   +'VPW: '+str(getValue(usr, "VPW")) +'\n' +'MSR: '+str(getValue(usr, "MSR"))+ '\n'    +
            'AT: '+str(getValue(usr, "AT")) +'\n'+  'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n' +'RF: '+str(getValue(usr, "RF"))+ '\n'+
            'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')

        elif mode == 'aair':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'APW: '+str(getValue(usr, "APW")) +'\n'+   'ARP: '+str(getValue(usr, "ARP")) +'\n'+
            'MSR: '+str(getValue(usr, "MSR"))+ '\n'    +'AT: '+str(getValue(usr, "AT")) +'\n'+  'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n'+
            'RF: '+str(getValue(usr, "RF"))+ '\n'+  'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')

        elif mode == 'vvir':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'VAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'VPW: '+str(getValue(usr, "APW")) +'\n'+   'VRP: '+str(getValue(usr, "ARP")) +'\n'+
            'MSR: '+str(getValue(usr, "MSR"))+ '\n'    +'AT: '+str(getValue(usr, "AT")) +'\n'+  'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n'+
            'RF: '+str(getValue(usr, "RF"))+ '\n'+  'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')

        elif mode == 'door':
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'      +'APW: '+str(getValue(usr, "APW")) +'\n'+
            'VPW: '+str(getValue(usr, "VPW"))+ '\n'     +'MSR: '+str(getValue(usr, "MSR"))+ '\n'     +'FAVD: '+str(getValue(usr, "FAVD"))+ '\n'+
            'AT: '+str(getValue(usr, "AT")) +'\n'       +'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n' +'RF: '+str(getValue(usr, "RF"))+ '\n'  +
            'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')

        else:
            return alert('Current Values:\n\n' +
            'mode: '+str(getValue(usr, "mode"))+ '\n'   +'lower: '+str(getValue(usr, "lower"))+ '\n'    +'upper: '+str(getValue(usr, "upper")) +'\n'+
            'AAmp: '+str(getValue(usr, "AAmp"))+ '\n'   +'VAmp: '+str(getValue(usr, "VAmp"))+ '\n'      +'APW: '+str(getValue(usr, "APW")) +'\n'+
            'VPW: '+str(getValue(usr, "VPW"))+ '\n'     +'ARP: '+str(getValue(usr, "ARP"))+ '\n'        +'VRP: '+str(getValue(usr, "VRP")) +'\n'+
            'MSR: '+str(getValue(usr, "MSR"))+ '\n'     +'FAVD: '+str(getValue(usr, "FAVD"))+ '\n'      +'AT: '+str(getValue(usr, "AT")) +'\n'+
            'ReactTime: '+str(getValue(usr, "ReactTime"))+ '\n' +'RF: '+str(getValue(usr, "RF"))+ '\n'  +'RecoveryTime: '+str(getValue(usr, "RecoveryTime")) +'\n')


class AOO(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AOO", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 0, column = 0)

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))


        self.AOO_Button = ttk.Button(self, text="Enter",
                            command= self.aooValues, cursor = "target")
        self.AOO_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aooValues(self):

        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        # gets the value of
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        aamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()


        if checkLRL(lrl) and checkURL(url) and checkAmp(aamp) and checkPW(apw):
            update(usr, "mode", "aoo")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "AAmp",  aamp)
            update(usr, "APW", apw)
            return alert("Values added successfully:")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class VOO(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VOO", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 0, column = 0)

        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VA_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VPW_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.VOO_Button = ttk.Button(self, text="Enter",
                            command= self.vooValues, cursor = "target")
        self.VOO_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def vooValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        vamp = self.VA_Entry.get()
        vpw = self.VPW_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(vamp) and checkPW(vpw):
            update(usr, "mode", "voo")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "VAmp", vamp)
            update(usr, "VPW", vpw)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class AAI(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AAI", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 0, column = 0)

        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.ARP_Entry = tk.DoubleVar()
        self.ARP_Entry.set(250)
        ttk.Label(self, text="Atrial Refractory Period\n(150-500)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ARP_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.AAI_Button = ttk.Button(self, text="Enter",
                            command= self.aaiValues, cursor = "target")
        self.AAI_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aaiValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        aamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()
        arp = self.ARP_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(aamp) and checkPW(apw) and checkRP(arp):
            update(usr, "mode", "aai")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "AAmp", aamp)
            update(usr, "APW", apw)
            update(usr, "ARP", arp)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class VVI(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VVI", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10)

        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VA_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VPW_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.VRP_Entry = tk.DoubleVar()
        self.VRP_Entry.set(320)
        ttk.Label(self, text="Ventricular Refractory Period\n(150-500)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VRP_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.VVI_Button = ttk.Button(self, text="Enter",
                            command= self.vviValues, cursor = "target")
        self.VVI_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def vviValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        vamp = self.VA_Entry.get()
        vpw = self.VPW_Entry.get()
        vrp = self.VRP_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(vamp) and checkPW(vpw) and checkRP(vrp):
            update(usr, "mode", "vvi")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "VAmp", vamp)
            update(usr, "VPW", vpw)
            update(usr, "VRP", vrp)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class DOO(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DOO", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10)

        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.FixedAV_Entry = tk.DoubleVar()
        self.FixedAV_Entry.set(150)
        ttk.Label(self, text="Fixed AV Delay\n(70-300)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.FixedAV_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VA_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VPW_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.DOO_Button = ttk.Button(self, text="Enter",
                            command= self.dooValues, cursor = "target")
        self.DOO_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def dooValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        favd = self.FixedAV_Entry.get()
        aamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()
        vamp = self.VA_Entry.get()
        vpw = self.VPW_Entry.get()


        if checkLRL(lrl) and checkURL(url) and checkAmp(vamp) and checkAmp(aamp) and checkPW(apw) and checkPW(vpw) and checkFAVD(favd):
            update(usr, "mode", "doo")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "FAVD", favd)
            update(usr, "VAmp", vamp)
            update(usr, "AAmp", aamp)
            update(usr, "APW", apw)
            update(usr, "VPW", vpw)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class AOOR(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AOOR", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10, )

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.MSR_Entry = tk.DoubleVar()
        self.MSR_Entry.set(120)
        ttk.Label(self, text="Maximum Sensor Rate\n(50-175)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.MSR_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.AT_Entry = tk.StringVar()
        self.AT_Entry.set("Med")
        ttk.Label(self, text="Activity Threshold\n(V-Low, Low, Med-Low,\nMed, Med-High,\nHigh, V-High)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AT_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.ReactTime_Entry = tk.DoubleVar()
        self.ReactTime_Entry.set(30)
        ttk.Label(self, text="Reaction Time\n(10-50)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ReactTime_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.RF_Entry = tk.DoubleVar()
        self.RF_Entry.set(8)
        ttk.Label(self, text="Reponse Factor\n(1-16)").grid(row = 4, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RF_Entry).grid(row = 4, column = 3, pady=(10,0), padx=(10,10))

        self.RecoveryTime_Entry = tk.DoubleVar()
        self.RecoveryTime_Entry.set(5)
        ttk.Label(self, text="Recovery Time\n(2-16)").grid(row = 1, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RecoveryTime_Entry).grid(row = 1, column = 5, pady=(10,0), padx=(10,10))

        self.AOOR_Button = ttk.Button(self, text="Enter",
                            command= self.aoorValues, cursor = "target")
        self.AOOR_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aoorValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        msr = self.MSR_Entry.get()
        aamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()
        at = self.AT_Entry.get()
        react = self.ReactTime_Entry.get()
        rf = self.RF_Entry.get()
        recovery = self.RecoveryTime_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(aamp) and checkMSR(msr) and checkPW(apw) and checkAT(at) and checkReactTime(react) and checkRF(rf) and checkRecoveryTime(recovery):
            update(usr, "mode", "aoor")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "MSR", msr)
            update(usr, "AAmp", aamp)
            update(usr, "APW", apw)
            update(usr, "AT", apw)
            update(usr, "ReactTime", react)
            update(usr, "RF", rf)
            update(usr, "RecoveryTime", recovery)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class VOOR(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VOOR", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10, )

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.MSR_Entry = tk.DoubleVar()
        self.MSR_Entry.set(120)
        ttk.Label(self, text="Maximum Sensor Rate\n(50-175)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.MSR_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VA_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VPW_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.AT_Entry = tk.StringVar()
        self.AT_Entry.set("Med")
        ttk.Label(self, text="Activity Threshold\n(V-Low, Low, Med-Low,\nMed, Med-High,\nHigh, V-High)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AT_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.ReactTime_Entry = tk.DoubleVar()
        self.ReactTime_Entry.set(30)
        ttk.Label(self, text="Reaction Time\n(10-50)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ReactTime_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.RF_Entry = tk.DoubleVar()
        self.RF_Entry.set(8)
        ttk.Label(self, text="Reponse Factor\n(1-16)").grid(row = 4, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RF_Entry).grid(row = 4, column = 3, pady=(10,0), padx=(10,10))

        self.RecoveryTime_Entry = tk.DoubleVar()
        self.RecoveryTime_Entry.set(5)
        ttk.Label(self, text="Recovery Time\n(2-16)").grid(row = 1, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RecoveryTime_Entry).grid(row = 1, column = 5, pady=(10,0), padx=(10,10))

        self.VOOR_Button = ttk.Button(self, text="Enter",
                            command= self.voorValues, cursor = "target")
        self.VOOR_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def voorValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        msr = self.MSR_Entry.get()
        vamp = self.VA_Entry.get()
        vpw = self.VPW_Entry.get()
        at = self.AT_Entry.get()
        react = self.ReactTime_Entry.get()
        rf = self.RF_Entry.get()
        recovery = self.RecoveryTime_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(vamp) and checkMSR(msr) and checkPW(vpw) and checkAT(at) and checkReactTime(react) and checkRF(rf) and checkRecoveryTime(recovery):
            update(usr, "mode", "voor")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "MSR", msr)
            update(usr, "VAmp", vamp)
            update(usr, "VPW", vpw)
            update(usr, "AT", at)
            update(usr, "ReactTime", react)
            update(usr, "RF", rf)
            update(usr, "RecoveryTime", recovery)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class AAIR(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AAIR", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10, )

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.MSR_Entry = tk.DoubleVar()
        self.MSR_Entry.set(120)
        ttk.Label(self, text="Maximum Sensor Rate\n(50-175)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.MSR_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.ARP_Entry = tk.DoubleVar()
        self.ARP_Entry.set(250)
        ttk.Label(self, text="Atrial Refractory Period\n(150-500)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ARP_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.AT_Entry = tk.StringVar()
        self.AT_Entry.set("Med")
        ttk.Label(self, text="Activity Threshold\n(V-Low, Low, Med-Low,\nMed, Med-High,\nHigh, V-High)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AT_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.ReactTime_Entry = tk.DoubleVar()
        self.ReactTime_Entry.set(30)
        ttk.Label(self, text="Reaction Time\n(10-50)").grid(row = 4, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ReactTime_Entry).grid(row = 4, column = 3, pady=(10,0), padx=(10,10))

        self.RF_Entry = tk.DoubleVar()
        self.RF_Entry.set(8)
        ttk.Label(self, text="Reponse Factor\n(1-16)").grid(row = 1, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RF_Entry).grid(row = 1, column = 5, pady=(10,0), padx=(10,10))

        self.RecoveryTime_Entry = tk.DoubleVar()
        self.RecoveryTime_Entry.set(5)
        ttk.Label(self, text="Recovery Time\n(2-16)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RecoveryTime_Entry).grid(row = 2, column = 5, pady=(10,0), padx=(10,10))

        self.AAIR_Button = ttk.Button(self, text="Enter",
                            command= self.aairValues, cursor = "target")
        self.AAIR_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aairValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        msr = self.MSR_Entry.get()
        aamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()
        arp = self.ARP_Entry.get()
        at = self.AT_Entry.get()
        react = self.ReactTime_Entry.get()
        rf = self.RF_Entry.get()
        recovery = self.RecoveryTime_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(aamp) and checkMSR(msr) and checkPW(apw) and checkRP(arp) and checkAT(at) and checkReactTime(react) and checkRF(rf) and checkRecoveryTime(recovery):
            update(usr, "mode", "aair")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "MSR", msr)
            update(usr, "AAmp", aamp)
            update(usr, "APW", apw)
            update(usr, "ARP", arp)
            update(usr, "AT", at)
            update(usr, "ReactTime", react)
            update(usr, "RF", rf)
            update(usr, "RecoveryTime", recovery)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class VVIR(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VVIR", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10, )

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.MSR_Entry = tk.DoubleVar()
        self.MSR_Entry.set(120)
        ttk.Label(self, text="Maximum Sensor Rate\n(50-175)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.MSR_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VA_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VPW_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.VRP_Entry = tk.DoubleVar()
        self.VRP_Entry.set(320)
        ttk.Label(self, text="Ventricular Refractory Period\n(150-500)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.VRP_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.AT_Entry = tk.StringVar()
        self.AT_Entry.set("Med")
        ttk.Label(self, text="Activity Threshold\n(V-Low, Low, Med-Low,\nMed, Med-High,\nHigh, V-High)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AT_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.ReactTime_Entry = tk.DoubleVar()
        self.ReactTime_Entry.set(30)
        ttk.Label(self, text="Reaction Time\n(10-50)").grid(row = 4, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ReactTime_Entry).grid(row = 4, column = 3, pady=(10,0), padx=(10,10))

        self.RF_Entry = tk.DoubleVar()
        self.RF_Entry.set(8)
        ttk.Label(self, text="Reponse Factor\n(1-16)").grid(row = 1, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RF_Entry).grid(row = 1, column = 5, pady=(10,0), padx=(10,10))

        self.RecoveryTime_Entry = tk.DoubleVar()
        self.RecoveryTime_Entry.set(5)
        ttk.Label(self, text="Recovery Time\n(2-16)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RecoveryTime_Entry).grid(row = 2, column = 5, pady=(10,0), padx=(10,10))

        self.VVIR_Button = ttk.Button(self, text="Enter",
                            command= self.vvirValues, cursor = "target")
        self.VVIR_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def vvirValues(self):
        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        msr = self.MSR_Entry.get()
        vamp = self.VA_Entry.get()
        vpw = self.VPW_Entry.get()
        vrp = self.VRP_Entry.get()
        at = self.AT_Entry.get()
        react = self.ReactTime_Entry.get()
        rf = self.RF_Entry.get()
        recovery = self.RecoveryTime_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkAmp(vamp) and checkMSR(msr) and checkPW(vpw) and checkRP(vrp) and checkAT(at) and checkReactTime(react) and checkRF(rf) and checkRecoveryTime(recovery):
            update(usr, "mode", "vvir")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "MSR", msr)
            update(usr, "VAmp", vamp)
            update(usr, "VPW", vpw)
            update(usr, "AT", at)
            update(usr, "ReactTime", react)
            update(usr, "RF", rf)
            update(usr, "RecoveryTime", recovery)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


class DOOR(tk.Frame):
    #__init__ method describes what is in our page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DOOR", font="TITLE_FONT")
        label.grid(row = 0, column = 0, pady=10, padx=10, )

        #Entry boxes specifies the range of the inputs.
        self.LRL_Entry = tk.DoubleVar()
        self.LRL_Entry.set(60)
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 1, column=0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.LRL_Entry).grid(row = 1, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        self.URL_Entry.set(120)
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.URL_Entry).grid(row = 2, column = 1, pady=(10,0), padx=(10,10))

        self.MSR_Entry = tk.DoubleVar()
        self.MSR_Entry.set(120)
        ttk.Label(self, text="Maximum Sensor Rate\n(50-175)").grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.MSR_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.FixedAV_Entry = tk.DoubleVar()
        self.FixedAV_Entry.set(150)
        ttk.Label(self, text="Fixed AV Delay\n(70-300)").grid(row = 4, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.FixedAV_Entry).grid(row = 4, column = 1, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        self.AA_Entry.set(3.5)
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 1, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 1, column = 3, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        self.VA_Entry.set(3.5)
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AA_Entry).grid(row = 2, column = 3, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        self.APW_Entry.set(0.4)
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 3, column = 3, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        self.VPW_Entry.set(0.4)
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.APW_Entry).grid(row = 4, column = 3, pady=(10,0), padx=(10,10))

        self.AT_Entry = tk.StringVar()
        self.AT_Entry.set("Med")
        ttk.Label(self, text="Activity Threshold\n(V-Low, Low, Med-Low,\nMed,Med-High,\nHigh, V-High)").grid(row = 1, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.AT_Entry).grid(row = 1, column = 5, pady=(10,0), padx=(10,10))

        self.ReactTime_Entry = tk.DoubleVar()
        self.ReactTime_Entry.set(30)
        ttk.Label(self, text="Reaction Time\n(10-50)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.ReactTime_Entry).grid(row = 2, column = 5, pady=(10,0), padx=(10,10))

        self.RF_Entry = tk.DoubleVar()
        self.RF_Entry.set(8)
        ttk.Label(self, text="Reponse Factor\n(1-16)").grid(row = 3, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RF_Entry).grid(row = 3, column = 5, pady=(10,0), padx=(10,10))

        self.RecoveryTime_Entry = tk.DoubleVar()
        self.RecoveryTime_Entry.set(5)
        ttk.Label(self, text="Recovery Time\n(2-16)").grid(row = 4, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, width="8", textvariable=self.RecoveryTime_Entry).grid(row = 4, column = 5, pady=(10,0), padx=(10,10))

        self.DOOR_Button = ttk.Button(self, text="Enter",
                            command= self.doorValues, cursor = "target")
        self.DOOR_Button.grid(row = 20, column = 1, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def doorValues(self):
        return alert('Values added successfully:\n\n' +
        'LRL: ' + str(self.LRL_Entry.get()) + '\n'+
        'URL: ' + str(self.URL_Entry.get()) + '\n'+
        'MSR: ' + str(self.MSR_Entry.get()) + '\n'+
        'FAVD: ' + str(self.FixedAV_Entry.get()) + '\n'+
        'AAmp: ' + str(self.AA_Entry.get()) + '\n'+
        'VAmp: ' + str(self.VA_Entry.get()) + '\n'+
        'APW: ' + str(self.APW_Entry.get()) + '\n'+
        'VPW: ' + str(self.VPW_Entry.get()) + '\n'+
        'AT: ' + str(self.AT_Entry.get()) + '\n'+
        'ReactTime: ' + str(self.ReactTime_Entry.get()) + '\n'+
        'RF: ' + str(self.RF_Entry.get()) + '\n'+
        'RecoveryTime: ' + str(self.RecoveryTime_Entry.get()))

        usr = getRecent() #getRecent() gets the returns the name of the user that is logged in
        lrl = self.LRL_Entry.get()
        url = self.URL_Entry.get()
        msr = self.MSR_Entry.get()
        favd = self.FixedAV_Entry.get()

        aamp = self.AA_Entry.get()
        vamp = self.AA_Entry.get()
        apw = self.APW_Entry.get()
        vpw = self.VPW_Entry.get()

        at = self.AT_Entry.get()
        react = self.ReactTime_Entry.get()
        rf = self.RF_Entry.get()
        recovery = self.RecoveryTime_Entry.get()

        if checkLRL(lrl) and checkURL(url) and checkMSR(msr) and checkFAVD(favd) and checkAmp(aamp) and checkAmp(vamp) and checkPW(apw) and checkPW(vpw) and checkAT(at) and checkReactTime(react) and checkRF(rf) and checkRecoveryTime(recovery):
            update(usr, "mode", "door")
            update(usr, "lower", lrl)
            update(usr, "upper", url)
            update(usr, "MSR", msr)
            update(usr, "FAVD", favd)
            update(usr, "AAmp", aamp)
            update(usr, "VAmp", vamp)
            update(usr, "APW", apw)
            update(usr, "VPW", vpw)
            update(usr, "AT", at)
            update(usr, "ReactTime", react)
            update(usr, "RF", rf)
            update(usr, "RecoveryTime", recovery)
            return alert("Values added successfully")

        else:
            alert("INVALID INPUTS\n\nCheck your values again")


app = DCM()
app.mainloop()

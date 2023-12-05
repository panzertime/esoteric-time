from .presentations import OsamCalendar, Astrologer

class TkErrorCatcher:

    '''
    In some cases tkinter will only print the traceback.
    Enables the program to catch tkinter errors normally

    To use
    import tkinter
    tkinter.CallWrapper = TkErrorCatcher
    '''

    def __init__(self, func, subst, widget):
        self.func = func
        self.subst = subst
        self.widget = widget

    def __call__(self, *args):
        try:
            if self.subst:
                args = self.subst(*args)
            return self.func(*args)
        except SystemExit as msg:
            print(msg)
            #raise SystemExit(msg)
        except Exception as err:
            print(err)
            #raise err

import tkinter as tk
tk.CallWrapper = TkErrorCatcher

def handle_exception(exception, value, traceback):
    print("Caught exception:", exception)

def run():
    root = tk.Tk()

    root.report_callback_exception=handle_exception

    root.title = "O.S. Anno Mundi"
    root.resizable(False,False)
    root.wm_attributes("-topmost", True)
    print("made root")

    mainFrame = tk.Frame(root, padx=5, pady=5)
    mainFrame.pack()

    calendarFrame = tk.Frame(mainFrame, relief="groove", borderwidth=2)
    calendarFrame.pack(fill="x")
    calendar = OsamCalendar(calendarFrame)
    calendar.pack()
    print("made calendar")

    astrologyFrame = tk.Frame(mainFrame, relief="groove", borderwidth=2)
    astrologyFrame.pack(fill="x")
    astrologer = Astrologer(astrologyFrame)
    astrologer.pack()
    print("made astrologer")

    calendar.write()
    print("wrote calendar")
    astrologer.augur()
    print("augured")

    menubar = tk.Menu(root)
    Timemenu = tk.Menu(menubar, tearoff=0)
    Timemenu.add_command(label="Simulate Aquarius", command=lambda: astrologer.dawnAquarius())
    menubar.add_cascade(label="Time", menu=Timemenu)

    root.config(menu=menubar)
    root.mainloop()

    print("main loop started")



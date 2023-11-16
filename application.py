import tkinter as tk

from presentations import OsamCalendar, Astrologer

root = tk.Tk()
root.tk_strictMotif()
root.title = "O.S. Anno Mundi"
root.resizable(False,False)
root.wm_attributes("-topmost", True)

mainFrame = tk.Frame(root, padx=5, pady=5)
mainFrame.pack()

calendarFrame = tk.Frame(mainFrame, relief="groove", borderwidth=2)
calendarFrame.pack(fill="x")
calendar = OsamCalendar(calendarFrame)
calendar.pack()

astrologyFrame = tk.Frame(mainFrame, relief="groove", borderwidth=2)
astrologyFrame.pack(fill="x")
astrologer = Astrologer(astrologyFrame)
astrologer.pack()

calendar.write()
astrologer.augur()
# Simulate the Age of Aquarius for testing purposes
# astrologer.after(1000, astrologer.dawnAquarius) 
root.mainloop()
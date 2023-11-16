import tkinter as tk
from datetime import datetime, timedelta
from itertools import cycle
from threading import Thread
from playsound import playsound

import astrologer

def romanize(input):
    # bastardized from some o'reilly cookbook
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

def angleFormat(input: float):
    if input < 10:
        return str(input)[:3] + "°"
    else:
        return str(input).split(".")[0] + "°"

class OsamCalendar(tk.Label):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.contents = tk.StringVar()
        self.contents.set(self.getDate())

    def write(self):
        self.config(textvariable=self.contents)
        self.contents.set(self.getDate())
        self.after(1000, self.write)

    def getDate(self):
        julian = datetime.today() - timedelta(days = 13)

        year = julian.year + 5508
        if julian.month > 8:
            year += 1
        date_string = str(julian.day) + " / " + romanize(julian.month) + " / " + str(year)
        time_string = str(julian.hour - 12 if julian.hour > 12 else (12 if julian.hour == 0 else julian.hour)) + " : " + str(julian.minute).zfill(2) + " : " + str(julian.second).zfill(2) + (" PM" if julian.hour > 11 else " AM")
        return date_string + "\n" + time_string
    
class Astrologer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        moonFrame = tk.Frame(self)
        moonFrame.pack()
        self.moonHouse = tk.StringVar()
        self.moonHouseBox = tk.Entry(moonFrame, textvariable=self.moonHouse, justify="center", width=4)
        self.moonHouseLbl = tk.Label(moonFrame, text="Moon's House:", anchor="w", justify="left", width=20)
        self.moonHouseLbl.pack(side="left", fill="both")
        self.moonHouseBox.pack(side="left", fill="y")

        planetsFrame = tk.Frame(self)
        planetsFrame.pack()
        self.planetaryAngle = tk.StringVar()
        self.planetaryAngleBox = tk.Entry(planetsFrame, textvariable=self.planetaryAngle, justify="center", width=4)
        self.planetaryAngleLbl = tk.Label(planetsFrame, text="Jupiter-Mars Conjugation:", anchor="w", justify="left", width=20)
        self.planetaryAngleLbl.pack(side="left", fill="y")
        self.planetaryAngleBox.pack(side="left", fill="y")

        self.moonHouse.set("I")
        self.moonHouseBox.config(state="readonly")

        self.planetaryAngle.set("0°")
        self.planetaryAngleBox.config(state="readonly")

        self.aquariusFrame = tk.Frame(self)
        self.aquariusFrame.pack()
        self.aquariusLabel = tk.Label(self.aquariusFrame, text="This is the dawning of the Age of Aquarius!", bg="#cc0000")
        self.aquariusLabel.pack()
        self.aquariusPhilosophy = tk.Message(self.aquariusFrame, width=250, justify="center", font="-slant italic")
        self.aquariusPhilosophy.pack(fill="x")

        self.philosophyCounter = 0
        self.isAquarius = False

        self.aquariusFrame.pack_forget()

    def dawnAquarius(self):
        self.aquariusFrame.pack()
        self.isAquarius = True
        Thread(target=playsound, args=['./aquarius.mp3']).start()
        self.waxEloquent()

    def sunsetAquarius(self):
        self.aquariusFrame.pack_forget()
        self.isAquarius = False

    def waxEloquent(self):
        if self.philosophyCounter == 3:
            self.philosophyCounter = 0
        line = astrologer.PHILOSOPHY[self.philosophyCounter]
        self.aquariusPhilosophy.configure(text=line)
        self.philosophyCounter += 1
        if self.isAquarius:
            self.after(2500, self.waxEloquent)

    def augur(self):
        alignment = astrologer.alignmentToAngular(astrologer.computeCurrentAlignment())
        self.moonHouseBox.config(state="normal")
        self.moonHouse.set(romanize(alignment.moonHouse))
        self.moonHouseBox.config(state="readonly")
        self.planetaryAngleBox.config(state="normal")
        self.planetaryAngle.set(angleFormat(alignment.jupiterMarsAngle))
        self.planetaryAngleBox.config(state="readonly")
        if (not self.isAquarius) and astrologer.isMomentAquarian(alignment):
            self.dawnAquarius()
        elif self.isAquarius and (not astrologer.isMomentAquarian(alignment)):
            self.sunsetAquarius()
        self.after(60000, self.augur)

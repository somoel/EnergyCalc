import scipy.constants
import math
import numpy
from tkextrafont import Font
import tkinter as tk

"""
TODO:
    Graphic mode
        Separate files
        Check negative particles
        Scientific notation
        Check entry data
        Clean and comment code
        Handle end of calculus

"""

welcomeScreen = tk.Tk()
welcomeScreen.title("Energy Calc")
welcomeScreen.eval('tk::PlaceWindow . center')


mediumFont = Font(file = 'fonts/HindSiliguri_Medium.ttf', family = "HindSiliguriMedium")

class CLabel(tk.Label):
    def __init__(self, parent, text, fontSize = 10):
        tk.Label.__init__(self, parent, text = text, font = (mediumFont, fontSize))

class CEntry(tk.Entry):
    def __init__(self, parent, stringVar, fontSize = 10, enterFun = None):
        tk.Entry.__init__(self, parent, textvariable = stringVar, font = (mediumFont, fontSize))
        if enterFun != None:
            self.bind('<Return>', enterFun)

class CButton(tk.Button):
    def __init__(self, parent, text, command, fontSize = 10):
        tk.Button.__init__(self, parent, text = text, font = (mediumFont, fontSize), command = command)



welcomeFrame = tk.Frame(welcomeScreen)
welcomeFrame.pack()
CLabel(welcomeFrame, "Bienvenido a Energy Calc", 15).grid()
CLabel(welcomeFrame, "¿Con cuántas cargas piensas trabajar?").grid(row=1)
chargeCount = tk.StringVar()
CEntry(welcomeFrame, chargeCount).grid(row = 1, column = 1)

CLabel(welcomeFrame, "Distancia en y de la partícula desde el orígen (m)").grid(row=2)
particleY = tk.StringVar()


chargeFrames = []
charges = []

def confirmChargeCount(e = None):
    global chargeFrames, particleY, chargeCount
    welcomeFrame.pack_forget()
    particleY = int(particleY.get())
    chargeCount = int(chargeCount.get())
    for i in range(chargeCount):
        chargeFrames.append(ChargeFrame(welcomeScreen, i))
        charges.append(None)
    chargeFrames[0].pack()
    
    
CEntry(welcomeFrame, particleY, enterFun = confirmChargeCount).grid(row = 2, column = 1)

CButton(welcomeFrame, "Continuar", confirmChargeCount).grid(row = 3, columnspan = 2)


class ChargeFrame(tk.Frame):
    def __init__(self, parent, index):
        tk.Frame.__init__(self, parent)
        self.index = index

        CLabel(self, f"Carga #{self.index + 1}", 15).grid()

        CLabel(self, "Carga eléctrica (C)").grid(row = 1)
        
        self.chargeStrVar = tk.StringVar()
        CEntry(self, self.chargeStrVar).grid(row = 1, column = 1)

        CLabel(self, "Distancia en x con respecto a la partícula (m)").grid(row = 2)
        
        self.xDistanceStrVar = tk.StringVar()
        CEntry(self, self.xDistanceStrVar, enterFun=self.nextCharge).grid(row = 2, column = 1)

        CButton(self, "Volver", self.back).grid(row = 3, column = 0)

        CButton(self, "Siguiente", self.nextCharge).grid(row = 3, column = 1)
    
    def nextCharge(self, e = None):
        global chargeFrames, charges, totalEnergys

        charges[self.index] = Charge(
            charge = float(self.chargeStrVar.get()),
            xDistance = float(self.xDistanceStrVar.get())
        )

        self.pack_forget()
        if (self.index + 1) < len(chargeFrames):
            chargeFrames[self.index + 1].pack()
        else:
            totalEnergy.set(calculateTotalEnergy(charges))
            resultFrame.pack()

    def back(self):
        global chargeFrames
        self.pack_forget()
        if (self.index - 1) < 0:
            welcomeFrame.pack()
        else:
            chargeFrames[self.index - 1].pack()

        
resultFrame = tk.Frame(welcomeScreen)
CLabel(resultFrame, "Resultados", 15).grid()
CLabel(resultFrame, "Campo electrico total:").grid(row=1)
totalEnergy = tk.StringVar()
tk.Label(resultFrame, textvariable=totalEnergy, font = (mediumFont, 13)).grid(row = 2)


# Constants
e0 = scipy.constants.epsilon_0
pi = math.pi
k = (1/(4 * pi * e0))

# Trigonometric functions to degress
def dSin (num):
    return math.sin(math.radians(num))

def dCos (num):
    return math.cos(math.radians(num))

def dArcTan(num):
    return numpy.rad2deg(numpy.arctan(num))



class Charge:
    global particleY
    def __init__(self, charge: float, xDistance: float) -> None:
        self.charge = charge
        self.xDistance = xDistance
        self.angle = dArcTan(particleY / abs(xDistance)) if xDistance != 0 else 0
        self.qUpRectangle = abs(self.charge) / (particleY**2 + self.xDistance**2)
        self.vectorParts = dCos(self.angle) + ((- dSin(self.angle)) if charge < 0 else dSin(self.angle))



def calculateTotalEnergy(charges: list) -> float:
    global k

    acumCharges = 0
    for i in range(len(charges)):
        acumCharges += charges[i].qUpRectangle * charges[i].vectorParts

    return k * acumCharges


# Out total energy
print("\n\n\nRESULTADOS:\nEnergía total que maneja la partícula: ", end="")
print(totalEnergy)

welcomeScreen.mainloop()
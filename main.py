import scipy.constants
import math
import numpy
from tkextrafont import Font
import tkinter as tk
from tkinter import messagebox

"""
TODO:
    Graphic mode
        Separate files
        Check negative particles
        Scientific notation
        Clean and comment code
        Handle end of calculus
        Add keybinding to back button

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
chargeCountStrVar = tk.StringVar()
CEntry(welcomeFrame, chargeCountStrVar).grid(row = 1, column = 1)

CLabel(welcomeFrame, "Distancia en y de la partícula desde el orígen (m)").grid(row=2)
particleYStrVar = tk.StringVar()


chargeFrames = []
charges = []


def confirmChargeCount(e = None):
    global chargeFrames, particleY, chargeCount
    try:
        particleY = float(particleYStrVar.get())
        if particleY < 0:
            messagebox.showerror("Error", "Aún está en desarrollo las particulas debajo del eje x.")
            return
        
        chargeCount = int(chargeCountStrVar.get())
        if chargeCount > 99 or chargeCount < 1:
            messagebox.showerror("Error", "Actualmente solo se permiten de 1 a 99 cargas dentro del campo.")
            return
    except:
        messagebox.showerror("Error", "Un dato está mal ingresado. Verifique los datos e intente nuevamente.")
        return
    for i in range(chargeCount):
        chargeFrames.append(ChargeFrame(welcomeScreen, i))
        charges.append(None)

    welcomeFrame.pack_forget()
    chargeFrames[0].pack()
    
    
CEntry(welcomeFrame, particleYStrVar, enterFun = confirmChargeCount).grid(row = 2, column = 1)

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

        try:
            charge = float(self.chargeStrVar.get())
            if charge == 0:
                messagebox.showwarning("Advertencia", "Si esa carga es 0, ¿para qué la pone? Cansón.")
            xDistance = float(self.xDistanceStrVar.get())
        except:
            messagebox.showerror("Error", "Un dato está mal ingresado. Verifique los datos e intente nuevamente")
            return

        charges[self.index] = Charge(charge = charge, xDistance = xDistance)

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


welcomeScreen.mainloop()
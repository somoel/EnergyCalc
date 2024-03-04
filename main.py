import scipy.constants
import math
import numpy
from tkextrafont import Font
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

"""
TODO: 
    Graphic mode
        Separate files
        Clean and comment code
        Enhance desing
        Add Java OOP
        Use zero
        Add units
        Show grahic
        Get Angle
        Use correct result
"""

welcomeScreen = tk.Tk()
welcomeScreen.title("Energy Calc")
welcomeScreen.eval('tk::PlaceWindow . center')


mediumFont = Font(file = 'fonts/HindSiliguri_Medium.ttf', family = "HindSiliguriMedium")

class CLabel(tk.Label):
    def __init__(self, parent, text, fontSize = 10):
        tk.Label.__init__(self, parent, text = text, font = (mediumFont, fontSize))

class CEntry(tk.Entry):
    def __init__(self, parent, stringVar, fontSize = 10, enterFun = None, startWithFocus = False, *args, **kwargs):
        tk.Entry.__init__(self, parent, textvariable = stringVar, font = (mediumFont, fontSize), *args, **kwargs)
        if enterFun != None:
            self.bind('<Return>', enterFun)
        if startWithFocus:
            self.focus()

class CButton(tk.Button):
    def __init__(self, parent, text, command, fontSize = 10):
        tk.Button.__init__(self, parent, text = text, font = (mediumFont, fontSize), command = command)

class CComboBox(ttk.Combobox):
    def  __init__(self, parent, *args, **kwargs):
        ttk.Combobox.__init__(self, parent, font = (mediumFont, 10), *args, **kwargs)



welcomeFrame = tk.Frame(welcomeScreen)
welcomeFrame.pack()

CLabel(welcomeFrame, "Bienvenido a Energy Calc", 15).grid()
CLabel(welcomeFrame, "¿Con cuántas cargas piensas trabajar?").grid(row=1)
chargeCountStrVar = tk.StringVar()
CEntry(welcomeFrame, chargeCountStrVar, startWithFocus = True, width = 3).grid(row = 1, column = 1)

CLabel(welcomeFrame, "Distancia en y de la partícula desde el orígen").grid(row=2)
particleYStrVar = tk.StringVar()


chargeFrames = []
charges = []


def confirmChargeCount(e = None):
    global chargeFrames, particleY, chargeCount, yDUnitValues
    try:
        
        chargeCount = int(chargeCountStrVar.get())
        if chargeCount > 99 or chargeCount < 1:
            messagebox.showerror("Error", "Actualmente solo se permiten de 1 a 99 cargas dentro del campo.")
            return
        
        particleY = float(particleYStrVar.get())
        
        expParticleY = int(expPYStrVar.get())

        unitParticleY = yDUnitValues.index(yDUnitStrVar.get())
        
        particleY = particleY * 10**expParticleY
        particleY = (particleY * 10**-2) if unitParticleY == 1 else particleY

        print(unitParticleY)
        print(particleY)
        
    
    except:
        messagebox.showerror("Error", "Un dato está mal ingresado. Verifique los datos e intente nuevamente.")
        return
    for i in range(chargeCount):
        chargeFrames.append(ChargeFrame(welcomeScreen, i))
        charges.append(None)

    welcomeFrame.pack_forget()
    chargeFrames[0].pack()
    chargeFrames[0].chargeEntry.focus()
    
    
CEntry(welcomeFrame, particleYStrVar, enterFun = confirmChargeCount, width = 7).grid(row = 2, column = 1)

CLabel(welcomeFrame, "x10^").grid(row = 2, column = 2)
expPYStrVar = tk.StringVar()
expPYStrVar.set("0")
CEntry(welcomeFrame, expPYStrVar, enterFun = confirmChargeCount, width = 3).grid(row = 2, column = 3)

yDUnitStrVar = tk.StringVar()
yDUnitValues = ["m", "cm"]
yDUnitCombo = CComboBox(welcomeFrame, textvariable = yDUnitStrVar,
            values = yDUnitValues, width = 2, state = "readonly")
yDUnitCombo.grid(row = 2, column = 4)
yDUnitCombo.set(yDUnitValues[0])



CButton(welcomeFrame, "Continuar", confirmChargeCount).grid(row = 3, columnspan = 2)


class ChargeFrame(tk.Frame):
    def __init__(self, parent, index):
        tk.Frame.__init__(self, parent)
        global chargeCount
        self.index = index

        CLabel(self, f"Carga #{self.index + 1}", 15).grid()

        CLabel(self, "Carga eléctrica").grid(row = 1)
        
        self.chargeStrVar = tk.StringVar()
        self.chargeEntry = CEntry(self, self.chargeStrVar, width = 7)
        self.chargeEntry.grid(row = 1, column = 1)
        self.chargeEntry.bind('<Alt-Left>', self.back)

        CLabel(self, "x10^").grid(row = 1, column = 2)
        self.expChargeStrVar = tk.StringVar()
        self.expChargeStrVar.set("0")
        CEntry(self, self.expChargeStrVar, width = 3).grid(row = 1, column = 3)

        self.chargeUnitStrVar = tk.StringVar()
        self.chargeUnitValues = ["C", "μC"]
        self.chargeUnitCombo = CComboBox(self, textvariable = self.chargeUnitStrVar,
                   values = self.chargeUnitValues, width = 2, state = "readonly")
        self.chargeUnitCombo.grid(row = 1, column = 4)
        self.chargeUnitCombo.set(self.chargeUnitValues[0])



        CLabel(self, "Distancia en x con respecto a la partícula").grid(row = 2)
        
        self.xDistanceStrVar = tk.StringVar()
        CEntry(self, self.xDistanceStrVar, enterFun=self.nextCharge, width = 7).grid(row = 2, column = 1)

        CLabel(self, "x10^").grid(row = 2, column = 2)
        self.xDChargeStrVar = tk.StringVar()
        self.xDChargeStrVar.set("0")
        CEntry(self, self.xDChargeStrVar, width = 3, enterFun=self.nextCharge).grid(row = 2, column = 3)

        self.xDUnitStrVar = tk.StringVar()
        self.xDUnitValues = ["m", "cm"]
        self.xDUnitCombo = CComboBox(self, textvariable = self.xDUnitStrVar,
                   values = self.xDUnitValues, width = 2, state = "readonly")
        self.xDUnitCombo.grid(row = 2, column = 4)
        self.xDUnitCombo.set(self.xDUnitValues[0])



        CButton(self, "Volver", self.back).grid(row = 3, column = 0)

        nextText = "Finalizar" if self.index == chargeCount - 1 else "Siguiente"
        CButton(self, nextText, self.nextCharge).grid(row = 3, column = 1)
    
    def nextCharge(self, e = None):
        global chargeFrames, charges, totalEnergys

        try:
            charge = float(self.chargeStrVar.get())
            if charge == 0:
                messagebox.showwarning("Advertencia", "Si esa carga es 0, ¿para qué la pone? Cansón.")
            xDistance = float(self.xDistanceStrVar.get())
            expCharge = int(self.expChargeStrVar.get())
            expXDistance = int(self.xDChargeStrVar.get())
            unitCharge = self.chargeUnitValues.index(self.chargeUnitStrVar.get())
            unitXDistance = self.xDUnitValues.index(self.xDUnitStrVar.get())


            charge = charge * 10**expCharge
            charge = (charge * 10**-6) if unitCharge == 1 else charge
            xDistance = xDistance * 10**expXDistance
            xDistance = (xDistance * 10**-2) if unitXDistance == 1 else xDistance

        except:
            messagebox.showerror("Error", "Un dato está mal ingresado. Verifique los datos e intente nuevamente")
            return

        charges[self.index] = Charge(charge = charge, xDistance = xDistance)

        self.pack_forget()
        if (self.index + 1) < len(chargeFrames):
            chargeFrames[self.index + 1].pack()
            chargeFrames[self.index + 1].chargeEntry.focus()
        else:
            totalEnergy.set(str(calculateTotalEnergy(charges)) + " C")
            resultFrame.pack()
            resultFrame.focus()

    def back(self, e = None):
        global chargeFrames, charges, chargeCountStrVar, particleYStrVar
        self.pack_forget()
        if (self.index - 1) < 0:
            charges = []
            chargeFrames = []
            chargeCountStrVar.set('')
            particleYStrVar.set('')
            expPYStrVar.set('0')
            welcomeFrame.pack()
        else:
            chargeFrames[self.index - 1].pack()
            chargeFrames[self.index - 1].chargeEntry.focus()

        
resultFrame = tk.Frame(welcomeScreen)

CLabel(resultFrame, "Resultados", 15).grid()
CLabel(resultFrame, "Campo electrico total:").grid(row=1)
totalEnergy = tk.StringVar()
tk.Label(resultFrame, textvariable=totalEnergy, font = (mediumFont, 13)).grid(row = 2)


def closeApp(e = None):
    welcomeScreen.destroy()

def backToCharges(e = None):
    global chargeFrames
    resultFrame.pack_forget()
    chargeFrames[-1].pack()

def resetApp(e = None):
    global charges, chargeFrames, chargeCountStrVar, particleYStrVar
    charges = []
    chargeFrames = []
    chargeCountStrVar.set('')
    particleYStrVar.set('')
    expPYStrVar.set('0')

    resultFrame.pack_forget()
    welcomeFrame.pack()


resultFrame.bind('r', resetApp)
resultFrame.bind('v', backToCharges)
resultFrame.bind('c', closeApp)

CButton(resultFrame, "Cerrar", closeApp).grid(row = 3)
CButton(resultFrame, "Volver", backToCharges).grid(row = 3, column = 1)
CButton(resultFrame, "Reiniciar", resetApp).grid(row = 3, column = 2)


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
        self.angle = dArcTan(abs(particleY) / abs(xDistance)) if xDistance != 0 else 0
        self.qUpRectangle = abs(self.charge) / (particleY**2 + self.xDistance**2)
        self.vectorParts = dCos(self.angle) + ((- dSin(self.angle)) if charge < 0 else dSin(self.angle))


def format_scientific_notation(number, precision=10):
    """
    Formats a decimal number in scientific notation with "x10^" instead of "E+".
    :param number: The decimal number to format.
    :param precision: Number of decimal places for the coefficient (default is 2).
    :return: A string representing the number in scientific notation.
    """
    coefficient, exponent = f"{number:.{precision}E}".split("E")
    return f"{coefficient} x10^{int(exponent)}"


def calculateTotalEnergy(charges: list) -> float:
    global k

    acumCharges = 0
    for i in range(len(charges)):
        acumCharges += charges[i].qUpRectangle * charges[i].vectorParts

    return format_scientific_notation(k * acumCharges)


welcomeScreen.mainloop()
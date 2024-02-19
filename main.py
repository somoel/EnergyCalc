import scipy.constants
import math
import numpy

"""
TODO:
    Graphic mode
    Check correct data input
    Use charge negative values instead of p/n

"""



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

# Input data

print(" -ENERGY CALC-\n\n")
while True:
    try:
        chargeCount = int(input("Número de esferas con cargas a calcular (1-99) >>>"))
        if (1 <= chargeCount <= 99):
            break
    except:
        pass



print("\nPARTÍCULA")
particleY = float(input("Distancia en y de la partícula desde el origen (m) >>>"))


class Charge:
    global particleY
    def __init__(self, charge: float, type: str, xDistance: float) -> None:
        self.charge = charge
        self.type = type
        self.xDistance = xDistance
        self.angle = dArcTan(particleY / abs(xDistance))
        self.qUpRectangle = self.charge / (particleY**2 + self.xDistance**2)
        self.vectorParts = dCos(self.angle) + ((- dSin(self.angle)) if type == "n" else dSin(self.angle))


charges = []
for i in range(chargeCount):
    print(f"\nESFERA #{i+1}")

    charge = float(input("Carga (C) >>>"))
    type = input("Positiva o negativa (p/n) >>>")
    xDistance = float(input("Distancia en x respecto a la partícula (m) >>>"))

    charges.append(Charge(
        charge = charge,
        type = type,
        xDistance = xDistance
    ))
   


# Data to total energy for the particle
    
acumCharges = 0
for i in range(chargeCount):
    acumCharges += charges[i].qUpRectangle * charges[i].vectorParts

totalEnergy = k * acumCharges


# Out total energy
print("\n\n\nRESULTADOS:\nEnergía total que maneja la partícula: ", end="")
print(totalEnergy)
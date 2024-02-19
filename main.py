import scipy.constants
import math
import numpy

"""
TODO:
    Graphic mode
    Value types for micro coulomb and centimeters
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
        print("[ERROR] Datos incorrectos")



print("\nPARTÍCULA")
while True:
    try:
        particleY = float(input("Distancia en y de la partícula desde el origen (m) >>>"))
        break
    except:
        print("[ERROR] Datos incorrectos")


class Charge:
    global particleY
    def __init__(self, charge: float, xDistance: float) -> None:
        self.charge = charge
        self.xDistance = xDistance
        self.angle = dArcTan(particleY / abs(xDistance)) if xDistance != 0 else 0
        self.qUpRectangle = abs(self.charge) / (particleY**2 + self.xDistance**2)
        self.vectorParts = dCos(self.angle) + ((- dSin(self.angle)) if charge < 0 else dSin(self.angle))


charges = []
for i in range(chargeCount):
    print(f"\nESFERA #{i+1}")
    while True:
        try:
            charge = float(input("Carga (+/- C) >>>"))
            if (charge == 0):
                print("[ADVERTENCIA] Si la partícula no tiene carga, pa que la pone, no sea cansón")
            break
        except:
            print("[ERROR] Datos incorrectos")

    while True:
        try:
            xDistance = float(input("Distancia en x respecto a la partícula (m) >>>"))
            break
        except:
            print("[ERROR] Datos incorrectos")

    charges.append(Charge(
        charge = charge,
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
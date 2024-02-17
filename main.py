import scipy.constants
import math

"""
TODO:
    Add multi-charges
    Graphic mode

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

# Input data

print(" -ENERGY CALC-"
      + "\n\n\nPARTÍCULA")

particleY = float(input("Distancia en y de la partícula desde el origen (m) >>>"))

print("\nESFERA #1")
q1Charge = float(input("Carga (C) >>>"))
q1type = input("Positiva o negativa (p/n) >>>")
q1xDistance = float(input("Distancia en x respecto a la partícula (m) >>>"))
q1Angle = float(input("Ángulo que forma el origen con la partícula (°) >>>"))

print("\nESFERA #2")
q2Charge = float(input("Carga (C) >>>"))
q2type = input("Positiva o negativa (p/n) >>>")
q2xDistance = float(input("Distancia en x respecto a la partícula (m) >>>"))
q2Angle = float(input("Ángulo que forma el origen con la partícula (°) >>>"))


# Data to total energy for the particle

q1UpRectangle = (q1Charge / (particleY**2 + q1xDistance**2))
q1VectorParts = (dCos(q1Angle) + ((- dSin(q1Angle)) if q1type == "n" else dSin(q1Angle)) )

q2UpRectangle = (q2Charge / (particleY**2 + q2xDistance**2))
q2VectorParts = (dCos(q2Angle) + ((- dSin(q2Angle)) if q2type == "n" else dSin(q2Angle)) )

totalEnergy = k * (
     ( q1UpRectangle * q1VectorParts ) +
     ( q2UpRectangle * q2VectorParts )
     )


# Out total energy
print("\n\n\nRESULTADOS:\nEnergía total que maneja la partícula: ", end="")
print(totalEnergy)
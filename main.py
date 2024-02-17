import sys
import math

e0 = sys.float_info.epsilon
pi = math.pi

def dSin (num):
    return math.sin(math.radians(num))

def dCos (num):
    return math.cos(math.radians(num))

print(- dSin(30))

q1Charge = float(input("Ingrese la carga eléctrica del la primera esfera (en Coulombs)>>>"))
q1type = input("Ingrese si la carga de la primera esfera es positiva o negativa (p/n) >>>")
q1xDistance = float(input("Ingrese la distancia desde el eje x de la primera esfera (en metros) >>>"))
q1Angle = float(input("Ingrese el ángulo que hay entre el eje x y la partícula desde la primera esfera (en grados) >>>"))

q2Charge = float(input("Ingrese la carga eléctrica del la segunda esfera (en Coulombs)>>>"))
q2type = input("Ingrese si la carga de la primera segunda es positiva o negativa (p/n) >>>")
q2xDistance = float(input("Ingrese la distancia desde el eje x de la segunda esfera (en metros) >>>"))
q2Angle = float(input("Ingrese el ángulo que hay entre el eje x y la partícula desde la segunda esfera (en grados) >>>"))

particleY = float(input("Ingrese la distancia en y que tiene la partícula desde el origen (en metros) >>>"))
particleX = float(input("Ingrese la distancia en x que tiene la partícula desde el origen (en metros) >>>"))

totalEnergy = (1/(4 * pi * e0)) * (
     ( (q1Charge / (particleY**2 + (particleX - q1xDistance)**2)) * (dCos(q1Angle) + (- dSin(q1Angle) if q1type == "n" else dSin(q1Angle)) ) ) +
     ( (q2Charge / (particleY**2 + (particleX - q2xDistance)**2)) * (dCos(q1Angle) + (- dSin(q1Angle) if q1type == "n" else dSin(q1Angle)) ) )
     )
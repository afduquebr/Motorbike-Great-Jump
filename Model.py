# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código desarrolla la trayectoria de un movimiento parabólico con rozamiento.

import math

m = 1; b = 0.2; V0 = 190; u = math.pi/6; X0 = 0; Y0 = 0; g = 9.81

# Esta función devuelve una lista con los coordenadas para cada instante de tiempo de la trayectoria.
def Motorbike(V0):
  x0 = .9995/b
  tvv = tv(Newton(x0, V0))
  xy = list()
  for i in range(0, 51):
    xy.append(XY((i * tvv/50), V0))
  return xy

# Esta función devuelve la coordenada de posición para un instante de tiempo t.
def XY(t, V0):
  xy = [0, 0]
  xy[0] = 245 + round(X0 + (V0 * math.cos(u)/b)*(1 - math.exp(-b*t)), 2)
  xy[1] = 320 - round(Y0 + (1/b)*(V0 * math.sin(u) + (g/b))*(1 - math.exp(-b*t)) - (g*t/b), 2)
  return xy

def Motorbikeb(V0):
  x0 = .9995/b
  tvv = tv(Newton(x0, V0))
  xy = list()
  for i in range(0, 51):
    xy.append(XYb((i * tvv/50), V0))
  return xy

def XYb(t, V0):
  xy = [0, 0]
  xy[0] = round(X0 + (V0 * math.cos(u)/b)*(1 - math.exp(-b*t)), 2)
  xy[1] = round(Y0 + (1/b)*(V0 * math.sin(u) + (g/b))*(1 - math.exp(-b*t)) - (g*t/b), 2)
  return xy

# Esta función permite obtener el tiempo de vuelo del movimiento.
def tv(z):
  return (-1/b)*math.log(1 - b*z)

def f(z, V0):
  return Y0 + (V0 * math.sin(u) + (g/b)) * z + (g/(b*b))*math.log(1-b*z)

def df(z, V0):
  return (V0 * math.sin(u) + (g/b)) + (g/(b*(b*z - 1)))

# Este metodo numérico permite encontrar el valor de z para el cual f(z) es cero.
def Newton(x0, V0):
  xi = x0
  xii = 0
  while(abs(f(xi, V0))>pow(10, -4)):
    xii=xi-(f(xi, V0)/df(xi, V0))
    xi=xii
  return xii

# Ecuación de una recta
def Line(x, B):
  return B[0] * x + B[1]

# Arroja un a lista cuys componentes conforman una linea recta
def Rect(A):
  B = list()
  C = list()
  B.append((A[3] - A[1])/(A[2] - A[0]))
  B.append(A[1] - B[0] * A[0])
  for i in range(10):
    x = i * (A[2] - A[0])/10 +A[0]
    C.append([x,Line(x,B)])
  return C

# Retorna una lista con el valor del angulo para un par de coordenadas respecto al anterior
def Angle(xy,u):
  A =list()
  A.append(u)
  for i in range(1,len(xy)):
    A.append(180 * math.atan2((xy[i][1]-xy[i-1][1]), (xy[i][0]-xy[i-1][0]))/math.pi)
  return A






# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################
# coordenadas:

x_n = np.arange(0,4.5,0.05)
y_n = np.arange(0,5,0.05)
z_n = np.arange(0,5,0.05)
# tengo que usar los vectores y_z y z_n del mismo tamaño porque sino no puedo
# usar cart2pol

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

# inicializo caso, coordenadas, modelo:

d_0 = 0.15
z_h = 0.125
U_hub = 2.2
C_T = 0.42
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)

k_estrella = 0.2
epsilon = 0.25

modelo = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

c_T = 0.5

modelo.play_cart(coordenadas,c_T)

################################################################################
# figura 3: delta_U / delta_U_inf vs r / r_{1/2}

# calculo r_medio (alaliticamente) : (para cada x voy a tener un r_medio)
# a los fines prácticos puedo usar z_n como si fuera r_n, no hace falta transformar
# de coordenadas a polares (uso z_n como r_n indistintamente)

cociente_r_r_medio = np.zeros((len(modelo.x_n),len(z_n)))
r_medio = (log(2) * 2 * (modelo.sigma_n**2))**(0.5)

# esto sale de hacer la cuenta
# por definición log es en base e

for i in range (0,len(x_n)):
    for j in range (0,len(z_n)):
        cociente_r_r_medio[i,j] = z_n[j]/r_medio[i]

from fraccionar import fraccionar
from barrer import barrer

v_0, v_1, v_2, v_3 = fraccionar(modelo.x_n)
barrido_r_n = barrer(z_n)

# tendria que hacer algo asi pero no funciona:
# for i in range(0, 5):
    # # ejemplito : print "We're on time %d" % (i)
    # coordenadas_2 = Coordenadas_Norm(x_n,cociente_r_r_medio[v_"%d",barrido_r_n],cociente_r_r_medio[v_"%d",barrido_r_n]) %(i)
    # modelo.play_cart(coordenadas_2,0.5)
    # barrido_cociente_r_r_medio_en_v_"%d" = barrer(cociente_r_r_medio[v_"%d",barrido_r_n]) %(i)
    # gauss_cociente_v_"%d" = modelo.gauss[v_"%d",barrido_cociente_r_r_medio_en_v_"%d",barrido_cociente_r_r_medio_en_v_"%d"] %(i)

coordenadas = Coordenadas_Norm(x_n,cociente_r_r_medio[v_0,barrido_r_n],cociente_r_r_medio[v_0,barrido_r_n])
modelo.play_cart(coordenadas,0.5)
barrido_cociente_r_r_medio_en_v_0 = barrer(cociente_r_r_medio[v_0,barrido_r_n])
gauss_cociente_v_0 = modelo.gauss[v_0,barrido_cociente_r_r_medio_en_v_0,barrido_cociente_r_r_medio_en_v_0]

coordenadas = Coordenadas_Norm(x_n,cociente_r_r_medio[v_1,barrido_r_n],cociente_r_r_medio[v_1,barrido_r_n])
barrido_cociente_r_r_medio_en_v_1 = barrer(cociente_r_r_medio[v_1,barrido_r_n])
modelo.play_cart(coordenadas,0.5)
gauss_cociente_v_1 = modelo.gauss[v_0,barrido_cociente_r_r_medio_en_v_0,barrido_cociente_r_r_medio_en_v_0]

coordenadas = Coordenadas_Norm(x_n,cociente_r_r_medio[v_2,barrido_r_n],cociente_r_r_medio[v_2,barrido_r_n])
modelo.play_cart(coordenadas,0.5)
barrido_cociente_r_r_medio_en_v_2 = barrer(cociente_r_r_medio[v_2,barrido_r_n])
gauss_cociente_v_2 = modelo.gauss[v_0,barrido_cociente_r_r_medio_en_v_0,barrido_cociente_r_r_medio_en_v_0]

coordenadas = Coordenadas_Norm(x_n,cociente_r_r_medio[v_3,barrido_r_n],cociente_r_r_medio[v_3,barrido_r_n])
modelo.play_cart(coordenadas,0.5)
barrido_cociente_r_r_medio_en_v_3 = barrer(cociente_r_r_medio[v_3,barrido_r_n])
gauss_cociente_v_3 = modelo.gauss[v_0,barrido_cociente_r_r_medio_en_v_0,barrido_cociente_r_r_medio_en_v_0]

x_y = { 'x_1': cociente_r_r_medio[v_0,barrido_r_n], 'y_1': gauss_cociente_v_0,
        'x_2': cociente_r_r_medio[v_1,barrido_r_n], 'y_2': gauss_cociente_v_1,
        'x_3': cociente_r_r_medio[v_2,barrido_r_n], 'y_3': gauss_cociente_v_2,
        'x_4': cociente_r_r_medio[v_3,barrido_r_n], 'y_4': gauss_cociente_v_3 }

nombre = "figura_3"
xLabel = r'$r/r_{1/2}$'
yLabel = r'$\Delta U / \Delta U_{max} $'
numero = 4

figura = Figura(nombre,x_y,xLabel,yLabel,numero)
figura.show_save()

# figura 3 del paper : checked!

################################################################################
# figura 4: sigma_n / x_n

x_y = { 'x_1': cociente_r_r_medio[v_0,barrido_r_n], 'y_1': gauss_cociente_v_0,

nombre = "figura_4"
xLabel = r'$x/d_{0}$'
yLabel = r'$\sigma / d{0} $'
numero = 1

figura = Figura(nombre,x_y,xLabel,yLabel,numero)
figura.show_save()



plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\sigma / d_{0} $')
plt.plot(x_n,sigma_n, 'x')
plt.show()
fig.savefig('figuras/gaussiana_4.png')

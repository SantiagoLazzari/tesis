# coding=utf-8

# from Modelo import Modelo
import numpy as np
from numpy import exp
from cart2pol import cart2pol
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm

# super() lets you avoid referring to the base class explicitly, which can be nice.
# But the main advantage comes with multiple inheritance, where all sorts of fun
# stuff can happen.


# tengo de estos por todos lados: IndentationError: unexpected indent
# tiene que ver con usar la barra espaciadora y y el tab en el mismo script??


class Gaussiana(object):

    def __init__(self, case, k_estrella, epsilon):
        super(Gaussiana, self).__init__()
        # aca no sirve de nada porque le puse (object)
        self.case = case
        self.k_estrella = k_estrella
        self.epsilon = epsilon
        # aca las coordenadas nuevas estan pisando las "coordenadas de Metodo"
        # no entiendo si me sirve para algo la inheritance en este caso

# me parece que esto no hace nada distinto porque en la práctica usar r es lo
# mismo que usar z

    def evalDeficitNorm(self, coord):
        pass
        return deficit

    def play_pol_2d(self, coordenadas, c_T):
        if isinstance(coordenadas, Coordenadas):
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
            coordenadas.normalizar(self.case)
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
        elif isinstance(coordenadas, Coordenadas_Norm):
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
            coordenadas.desnormalizar(self.case)
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
        self.c_T = c_T
        self.r, self.phi = cart2pol(self.y_n, self.z_n)
        sigma_n = self.k_estrella * self.x_n + self.epsilon
        sigma_n_cuadrado = (sigma_n)**2
        r_cuadrado = self.r**2
        c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(0.5)
        exponente = np.zeros((len(self.x_n),len(self.r)))
        self.gauss = np.zeros((len(self.x_n),len(self.r)))
        self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.r)))
        for i in range (0,len(self.x_n)):
            for j in range (0,len(self.r)):
                exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i])
                self.gauss[i,j] = exp(exponente[i,j])
                self.deficit_dividido_U_inf[i,j] = c[i] * self.gauss[i,j]

    def play_pol(self, coordenadas, c_T):
        if isinstance(coordenadas, Coordenadas):
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
            coordenadas.normalizar(self.case)
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
        elif isinstance(coordenadas, Coordenadas_Norm):
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
            coordenadas.desnormalizar(self.case)
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
        self.c_T = c_T
        self.sigma_n = self.k_estrella * self.x_n + self.epsilon
        sigma_n_cuadrado = (self.sigma_n)**2
        #r_cuadrado = self.y_n**2 + self.z_n**2
        c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(0.5)
        r_cuadrado = np.zeros((len(self.y_n),len(self.z_n)))
        exponente = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        self.gauss = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        for i in range (0,len(self.x_n)):
            for j in range (0,len(self.y_n)):
                    for k in range (0,len(self.z_n)):
                        r_cuadrado[j,k] = (self.y_n[j])**2 + (self.z_n[k])**2
                        exponente[i,j,k] = -r_cuadrado[j,k] / (2 * sigma_n_cuadrado[i])
                        self.gauss[i,j,k] = exp(exponente[i,j,k])
                        self.deficit_dividido_U_inf[i,j,k] = c[i] * self.gauss[i,j,k]


    def play_cart(self, coordenadas, c_T):
        if isinstance(coordenadas, Coordenadas):
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
            coordenadas.normalizar_hub(self.case)
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
        elif isinstance(coordenadas, Coordenadas_Norm):
            self.x_n = coordenadas.x_n
            self.y_n = coordenadas.y_n
            self.z_n = coordenadas.z_n
            coordenadas.desnormalizar_hub(self.case)
            self.x = coordenadas.x
            self.y = coordenadas.y
            self.z = coordenadas.z
        self.c_T = c_T
        self.sigma_n = self.k_estrella * self.x_n + self.epsilon
        sigma_n_cuadrado = (self.sigma_n)**2
        #r_cuadrado = self.y_n**2 + self.z_n**2
        c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(0.5)
        r_cuadrado = np.zeros((len(self.y_n),len(self.z_n)))
        exponente = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        self.gauss = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
        for i in range (0,len(self.x_n)):
            for j in range (0,len(self.y_n)):
                    for k in range (0,len(self.z_n)):
                        r_cuadrado[j,k] = (self.y_n[j])**2 + (self.z_n[k])**2
                        exponente[i,j,k] = -r_cuadrado[j,k] / (2 * sigma_n_cuadrado[i])
                        self.gauss[i,j,k] = exp(exponente[i,j,k])
                        self.deficit_dividido_U_inf[i,j,k] = c[i] * self.gauss[i,j,k]

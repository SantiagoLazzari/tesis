import numpy as np

class Coordenadas(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.x_n = None
        self.y_n = None
        self.z_n = None

    def normalizar(self,case):
        self.x_n = self.x/case.d_0
        self.y_n = self.y/case.d_0
        self.z_n = self.z /case.d_0

    def normalizar_hub(self,case):
        self.x_n = self.x/case.d_0
        self.y_n = self.y/case.d_0
        self.z_n = (self.z - case.z_h)/case.d_0

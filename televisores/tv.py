


class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV+= 1
    
    def setMarca(self, marca):
        self.numero = marca
    def getMarca(self):
        return self.marca
    def setCanal(self, canal):
        if (canal>=1 and canal<= 120 and self.estado==True):
            self.canal = canal
    def getCanal(self):
        return self.canal
    def setPrecio(self, precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio
    def setEstado(self, estado):
        self.estado = estado
    def getEstado(self):
        return self.estado
    def setControl(self, control):
        self.control = control
    def getControl(self):
        return self.control
    def setVolumen(self, volumen):
        if (volumen>=0 and volumen<=7 and self.estado == True):
            self.volumen = volumen
    def getVolumen(self):
        return self.volumen
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod 
    def setNumTV(cls, numTV):
        if numTV>=0:
            cls.numTV = numTV
    def turnOn(self):
        if self.estado == False:
            self.estado = True
    def turnOff(self):
        if self.estado == True:
            self.estado = False
    def canalUp(self):
        if (self.estado == True and self.canal<120 and self.canal>=1 ):
            self.canal += 1
    def canalDown(self):
        if (self.estado == True and self.canal<120 and self.canal>1 ):
            self.canal -= 1
    def volumenUp(self):
        if (self.estado == True and self.volumen<7 and self.volumen>=0):
            self.volumen += 1
    def volumenDown(self):
        if (self.estado == True and self.volumen >0 and self.volumen <=7):
            self.volumen-=1





        
        






    
    
    
    
        

    

    


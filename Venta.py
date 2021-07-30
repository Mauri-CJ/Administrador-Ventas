from datetime import date
class Venta:
    
    def __init__(self,id_venta=-1,productos=0,monto=0,dia=date.today()):
        self._id_venta = id_venta
        self._productos = productos
        self._monto    = monto
        self._dia      = dia

    
    def __str__(self):
        return f'''
        ------------------------------------
        ID-VENTA           : {self._id_venta}
        Productos vendidos : {self._productos}
        Monto recaudado    : ${self._monto:.2f}
        Dia de la venta    : {self._dia}
        ------------------------------------
        '''

    @property
    def id_venta(self):
        return self._id_venta

    @id_venta.setter
    def id_venta(self,id_venta):
        self._id_venta = id_venta


    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self,productos):
        self._productos = productos

    
    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self,monto):
        self._monto = monto

    
    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self,dia):
        self._dia = dia
    




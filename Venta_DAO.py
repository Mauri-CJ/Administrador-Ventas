from Venta import Venta
from logger_base import log
from Cursor_Del_Pool import CursorDelPool


class VentaDao:
    _SELECT = 'SELECT * FROM venta'
    _INSERT = 'INSERT INTO venta (productos_vendidos,monto_recaudado,dia) VALUES (%s,%s,%s);'
    _UPDATE = 'UPDATE venta SET productos_vendidos = %s, monto_recaudado=%s,dia=%s WHERE id_venta = %s;'
    _DELETE = 'DELETE FROM venta WHERE id_venta = %s;'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()

            return registros

    @classmethod
    def insertar(cls,venta):
        with CursorDelPool() as cursor:
            valores = (venta.productos,venta.monto,venta.dia)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount

    @classmethod 
    def actualizar(cls,venta):
        with CursorDelPool() as cursor:
            valores = (venta.productos,venta.monto,venta.dia,venta.id_venta)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,venta):
        with CursorDelPool() as cursor:
            valores= (venta.id_venta,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount


  

   

    


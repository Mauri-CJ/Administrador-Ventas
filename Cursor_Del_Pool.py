from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion  =None
        self._cursor    =None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor   = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,exc_val,exc_type,exc_tb):
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ha ocurrido un error en la transaccion.Tipo de excepcion:{exc_val} | Traceback : {exc_tb}. Se hizo rollback')

        else:
            self._conexion.commit()
            log.info(f'Transaccion exitosa. Se hizo commit')
        
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM venta')
        log.info(cursor.fetchall())
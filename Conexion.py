from logger_base import log
from psycopg2 import pool 
import sys

class Conexion:
    _DATABASE = 'administrador_ventas'
    _HOST     = '127.0.0.1'
    _PORT     = '5432'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool     = None

    @classmethod 
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONN,   
                    cls._MAX_CONN,
                    database = cls._DATABASE ,  
                    host     = cls._HOST,   
                    port     = cls._PORT,   
                    user     = cls._USERNAME,   
                    password = cls._PASSWORD   
                )
                log.info('Se ha obtenido el pool de conexiones de manera exitosa.')
                return cls._pool

            except Exception as e:
                log.error(f'Ha ocurrido un error al obtener el pool de conexiones.{e}')
                sys.exit()

        else:
            return cls._pool 

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.info(f'Se ha obtenido una conexion del pool exitosa: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.info(f'Se ha liberado la conexion: {conexion}. Ha regresado al pool de conexiones')
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.info('Se han cerrado todas las conexiones del pool.')



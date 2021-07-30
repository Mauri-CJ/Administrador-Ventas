from Venta import Venta
from Venta_DAO import VentaDao
from os import system
from time import sleep

def limpiar_pantalla():
    sleep(1.0)
    system('clear')

def transformar_registros(registros):
    ventas = []
    for registro in registros:
        venta = Venta(registro[0],registro[1],registro[2],registro[3])
        ventas.append(venta)
    return ventas 

def traer_ventas():
    system('clear')
    registros = VentaDao.seleccionar()
    ventas = transformar_registros(registros)
    if len(ventas) == 0 :
        print("----------------------------------------------------------------------------------------")
        print("Actualmente no posees ventas")
        print("----------------------------------------------------------------------------------------")
        
    else:
        print("VENTAS:")
        for venta in ventas:
            print(venta)
        print("--------------------------------------------")

def insertar_venta():
    system('clear')
    productos_vendidos = int(input("Ingrese los productos vendidos el dia de la fecha: "))
    monto_recaudado    = float(input("Ingrese el monto recaudado el dia de la fecha: "))

    venta = Venta(productos=productos_vendidos,monto=monto_recaudado)
    
    ventas_insertadas = VentaDao.insertar(venta)
    print(f'Has insertado: {ventas_insertadas} venta.')
    limpiar_pantalla()

def actualizar_venta():
    system('clear')
    id_venta           = int(input("Ingrese el ID de la venta que desea actualizar: "))
    productos_vendidos = int(input("Ingrese los productos vendidos el dia de la fecha: "))
    monto_recaudado    = float(input("Ingrese el monto recaudado el dia de la fecha: "))
    dia = input('Ingrese el dia de la venta (EN EL SIGUIENTE FORMATO: AÑO-MES-DIA [EJ:2021-02-29]): ')

    venta = Venta(id_venta=id_venta, productos=productos_vendidos,monto=monto_recaudado,dia=dia)
    ventas_actualizadas = VentaDao.actualizar(venta)

    if ventas_actualizadas == 0:
        print("----------------------------------------------------------------------------------------")
        print(f"No hemos podido eliminar la venta debido a que no encontramos la venta con ID:{id_venta}")
        print("----------------------------------------------------------------------------------------")
    else:
        print(f'Ventas actualizadas: {ventas_actualizadas} venta')
    limpiar_pantalla()

def eliminar_venta():
    system('clear')
    id_venta = int(input("Ingrese el ID de la venta que desea eliminar: "))
    
    venta = Venta(id_venta=id_venta)
    ventas_eliminadas = VentaDao.eliminar(venta)
    
    if ventas_eliminadas == 0:
        print("----------------------------------------------------------------------------------------")
        print(f"No hemos podido eliminar la venta debido a que no encontramos la venta con ID:{id_venta}")
        print("----------------------------------------------------------------------------------------")
    else:
        print(f'Ventas eliminadas: {ventas_eliminadas} venta')
    limpiar_pantalla()

def cerrar_programa():
    system('clear')
    print('Nos vemos luego.')
    sleep(2)

opcion_usuario = None

opciones = {
    '1':traer_ventas,
    '2':insertar_venta,
    '3':actualizar_venta,
    '4':eliminar_venta,
    '5':cerrar_programa,
}

if __name__ =='__main__':
    system('clear')
    print("ADMINISTRADOR DE VENTAS".center(120,"-"))

    opcion_usuario = input('''
        ----------------------------
        ADMINISTRADOR DE VENTAS
        ----------------------------
        OPCIONES:
        [1]:Listar todas las ventas.
        [2]:Insertar una venta.
        [3]:Modificar una venta.
        [4]:Eliminar una venta.
        [5]:Cerrar el programa
    
        Ingrese una opcion: ''')
    while(opcion_usuario != '5'):
        if opcion_usuario in opciones.keys():
            opciones[opcion_usuario]()
        else:
            print("Has elegido una opcion incorrecta")
        opcion_usuario = input('''
        ----------------------------
        ADMINISTRADOR DE VENTAS
        ----------------------------
        OPCIONES:
        [1]:Listar todas las ventas.
        [2]:Insertar una venta.
        [3]:Modificar una venta.
        [4]:Eliminar una venta.
        [5]:Cerrar el programa
    
        Ingrese una opcion: ''')
    else:
        opciones[opcion_usuario]()
        
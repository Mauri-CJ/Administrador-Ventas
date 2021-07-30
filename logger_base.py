import logging as log

log.basicConfig(
    level    =log.ERROR,
    format   ='%(asctime)s %(levelname)s [%(filename)s line:%(lineno)s] %(message)s',
    datefmt  ='%I:%M:%S:%p',
    handlers =[
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
) 

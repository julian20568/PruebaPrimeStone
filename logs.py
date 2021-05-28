import os, platform, logging

if platform.platform().startswith('Windows'):
    fichero_log = os.path.join(os.getenv('HOMEDRIVE'), 
                               os.getenv("HOMEPATH"),
                               'test.log')
else:
    fichero_log = os.path.join(os.getenv('HOME'), 'test.log')

print('Archivo Log en ', fichero_log)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = 'w',)
logging.debug('Comienza el programa')
logging.info('Procesando con normalidad')
logging.warning('Advertencia')

#cierre
logging.shutdown()
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import platform, logging

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SistemaAdminEstudiantil.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#logs a base de archivos de texto
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
logging.debug('Comienza el programa\n')
logging.info('Procesando con normalidad\n')
logging.warning('Advertencia')


if __name__ == '__main__':
    main()

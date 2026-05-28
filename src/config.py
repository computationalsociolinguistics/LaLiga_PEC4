'''
Contiene las dos variables obligatorias: nom_alumne (nombre del autor) y date_time (fecha actual).
'''
from datetime import datetime

NOM_ALUMNE = 'Damián Morales Sánchez'
date_time = datetime.now().strftime('%Y%m%d_%H%M%S')

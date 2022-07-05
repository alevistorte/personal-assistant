import pandas as pd
import csv
import os
from actions.public import *
# from public import *

ALARMAS = PATH + 'alarmas/'
files = os.listdir(ALARMAS)

activeAlarms = {'Especialidad': [],	'Severidad': [],
                'Fuente': [], 'Descripcion': []}

especialidades = {'c': ['Comercio Electronico', True],
                  'p': ['Plataformas', True],
                  'i': ['Infraestructura', False]}

setSeveridad = {'Critical': 'Critical',
                'Major': 'Major',
                'Minor': 'Minor',
                'Warning': 'Warning',
                'CRIT': 'Critical',
                'WARN': 'Warning',
                'UNKN': 'Unkown'
                }

# los nombres de los archivos deben comenzar con las letras p para plataforma, c para comercio electronico, i para los ficheros de las alarmas de los centros de datos

'''
['service_state', 'service_state', 'host', 'service_description', 'service_icons', 'svc_plugin_output', 'svc_state_age', 'svc_check_age,,,,']

['Severity', 'Name', 'Alarm Source', 'Last Occurrence Time', 'First Occurrence Time', 'Location Info', 'Remarks', 'Arrive At', 'Duration', 'Occurrence Times', 'Clearance Status', 'Cleared By', 'Clearance Time', 'Clearance Type', 'Auto Clear', 'Acknowledgement Status', 'Acknowledged By', 'Acknowledged On', 'Additional Information', 'Additional Text', 'Threshold Information', 'Probable Cause', 'Alarm Source Type', 'Alarm Type', 'Alarm ID', 'Alarm Serial Number', 'Equipment Alarm Serial Number']
'''


def get_alarms():
    for f in files:
        firstLetter = f[0].lower()
        especialidad = especialidades[firstLetter][0]
        isFromCMK = especialidades[firstLetter][1]

        delimiter = ';' if isFromCMK else ','

        with open(ALARMAS + f) as csvfile:
            csvAlarms = csv.reader(csvfile, delimiter=delimiter)

            isFirstTime = True
            for row in csvAlarms:
                if (isFirstTime):
                    isFirstTime = False
                    if(isFromCMK):
                        indexSeveridad = row.index('service_state')
                        indexFuente = row.index('host')
                        indexDescripcion = row.index('service_description')
                    else:
                        indexSeveridad = row.index('Severity')
                        indexFuente = row.index('Alarm Source Type')
                        indexDescripcion = row.index('Name')

                    continue

                activeAlarms['Especialidad'].append(especialidad)
                activeAlarms['Severidad'].append(
                    setSeveridad[row[indexSeveridad]])
                activeAlarms['Fuente'].append(
                    row[indexFuente] if isFromCMK else row[indexFuente][1:])
                activeAlarms['Descripcion'].append(
                    row[indexDescripcion] + ' ' + row[indexDescripcion + 2] if isFromCMK else row[indexDescripcion][1:])

    dfAlarmas = pd.DataFrame(activeAlarms, index=range(
        1, 1 + len(activeAlarms['Especialidad'])))

    return dfAlarmas

import pandas as pd
from actions.public import *


def update_tickets():

    xls = pd.ExcelFile(TICKETS)
    tickets = pd.read_excel(xls)

    xls = pd.ExcelFile(USERS_DB)
    users = pd.read_excel(xls)

    uPlataforma = []
    uGito = []
    for u in users.itertuples():
        if(isIncluded(PLATAFORMAS, u[7])):
            uPlataforma.append(u[8] + ' ' + u[9])
            continue
        if(u[7] == 'GITO'):
            uGito.append(u[8] + ' ' + u[9])

    '''
    Esta es la cabecera de los tickets
    ['Elmto Red.', 'Provincia', 'Centro', 'Municipio', 'Sitio', 'Número',
       'Título', 'Hecho Ext.', 'F.Inicio', 'F.Fin', 'T.Problema', 'A.Serv',
       'A.Elmto', 'Responsable', 'Especialidad', 'Elemento', 'Equipo',
       'User. Abrio', 'Categoria', 'Clave Cierre', 'Estado', 'Tg', 'Operador',
       'Ticket Operador', 'Provincia Id', 'Centro Id', 'Municipio Id',
       'Sitio Id', 'Elemento Id']


    Esta es la cabecera del archivo de los usuarios actualizados con sus departamentos
    ['Unnamed: 0', 'Login', 'Dominio', 'Correo', 'Móvil', 'Cargo',
       'Departamento', 'Nombre', 'Apellido', 'Provincia', 'Area', 'Disponible',
       'Notificar x Sms', 'Notificar x Email', 'Notificar Sólo Hecho Extra']

    Se debe actualizar la especialidad del ticket en dependencia del area del responsable
    ya que el area en la que se abrio puede cambiar
    '''

    camposPlataforma = {'Número': [],	'Título': [], 'F.Inicio': [],
                        'Responsable': [],	'Estado': [],	'Tiempo': []}
    camposGito = {'Número': [],	'Título': [], 'F.Inicio': [],
                  'Responsable': [],	'Estado': [],	'Tiempo': []}

    for t in tickets.itertuples():
        nombre = t[14].split('-')[0]
        if(isIncluded(uPlataforma, nombre)):
            camposPlataforma['Número'].append(t[6])
            camposPlataforma['Título'].append(t[7])
            camposPlataforma['F.Inicio'].append(t[9].date())
            camposPlataforma['Responsable'].append(nombre)
            camposPlataforma['Estado'].append(t[21])
            camposPlataforma['Tiempo'].append(get_time(str(t[9].date())))
            continue

        if(isIncluded(uGito, nombre)):
            camposGito['Número'].append(t[6])
            camposGito['Título'].append(t[7])
            camposGito['F.Inicio'].append(t[9].date())
            camposGito['Responsable'].append(nombre)
            camposGito['Estado'].append(t[21])
            camposGito['Tiempo'].append(get_time(str(t[9].date())))

    dfPlataforma = pd.DataFrame(camposPlataforma, index=range(
        1, 1 + len(camposPlataforma['Estado'])))
    dfGito = pd.DataFrame(camposGito, index=range(
        1, 1 + len(camposGito['Estado'])))

    return dfPlataforma, dfGito

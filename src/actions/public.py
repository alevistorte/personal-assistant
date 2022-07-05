from datetime import datetime


from datetime import date

# areas
PLATAFORMAS = ('COMERCIO ELECTRONICO', 'SOPORTE PLATAFORMA OPERACION',
               'INFRAESTRUCTURA CENTRO DATOS', 'PLATAFORMAS')
GITO = ('GITO')

# files
PATH = '/home/alevistorte/Documents/00Projects/personal-assistant/'
TICKETS = PATH + '/data/tickets.xls'
USERS_DB = PATH + '/data/usuariosDB.xlsx'
TICKETS_DB = PATH + 'data/ticketsDB.xlsx'


def isIncluded(iterable, value):
    for i in iterable:
        if(i == value):
            return True
    return False


def get_time(fecha: str):
    hoy = date.today()
    inicio = date.fromisoformat(fecha)
    return str((hoy - inicio).days) + ' días'

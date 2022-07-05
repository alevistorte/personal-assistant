from datetime import datetime


from datetime import date

# areas
PLATAFORMAS = ('COMERCIO ELECTRONICO', 'SOPORTE PLATAFORMA OPERACION',
               'INFRAESTRUCTURA CENTRO DATOS', 'PLATAFORMAS')
GITO = ('GITO')

# files
TICKETS = '/home/alevistorte/Documents/00Projects/personal-assistant/data/tickets.xls'
USERS_DB = '/home/alevistorte/Documents/00Projects/personal-assistant/data/usuariosDB.xlsx'
TICKETS_DB = '/home/alevistorte/Documents/00Projects/personal-assistant/data/ticketsDB.xlsx'


def isIncluded(iterable, value):
    for i in iterable:
        if(i == value):
            return True
    return False


def get_time(fecha: str):
    hoy = date.today()
    inicio = date.fromisoformat(fecha)
    return str((hoy - inicio).days) + ' días'

import pandas as pd

USERS = '/home/alevistorte/Documents/00Projects/personal-assistant/data/usuarios.xls'
ESPECIALISTAS = '/home/alevistorte/Documents/00Projects/personal-assistant/data/especialistas.xlsx'


def update_users():
    print('Actualizando el departamento de los usuarios...')

    xls = pd.ExcelFile(USERS)
    users = pd.read_excel(xls)

    xlsx = pd.ExcelFile(ESPECIALISTAS)
    especialistas = pd.read_excel(xlsx)

    '''
    Las posiciones comienzan desde 1 porque el primero es el index
    La cabecera del fichero de los usuarios es:
    Login	Dominio	Correo	Móvil	Cargo	Departamento	Nombre	Apellido	Provincia	Area

    Mientras que la del fichero de los especialistas es:
    DEPARTAMENTO	RESPONSABLE	NOMBRE Y APELLIDO	TELF. MOVIL	Login	NIVEL
    '''

    for u in users.itertuples():
        for e in especialistas.itertuples():
            if(u[1] == e[5].split('@')[0]):
                users.iat[u[0], 5] = e[1]
                break

    USERS_DB = '/home/alevistorte/Documents/00Projects/personal-assistant/data/usuariosDB.xlsx'
    users.to_excel(USERS_DB)

    print('La actualizacion ha terminado. Puede ver los resultado en ', USERS_DB)


update_users()

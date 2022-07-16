import argparse
import xlsxwriter

from actions.get_alarms import get_alarms
from actions.update_tickets import *
from actions.update_users import update_users

# Parseadno los argumentos
parser = argparse.ArgumentParser(
    description='Automatizacion de las tareas diarias como EP')

parser.add_argument('-t', '--tickets',
                    help='Imprimir el listado de tickets', nargs='?', default='', const='present')
parser.add_argument('-i', '--informe',
                    help='Realizar el informe para la reunion de operaciones', nargs='?', default='', const='present')
parser.add_argument('-a', '--alarmas',
                    help='Imprimir el listado de alarmas', nargs='?', default='', const='present')
parser.add_argument('-u', '--usuarios',
                    help='Actualizar el area de los usuarios', nargs='?', default='', const='present')

args = parser.parse_args()

if (args.tickets == 'present'):
    tickets, dfGito = update_tickets()
    print('\n')
    print(tickets)
    print('\n')
    print('-----------------------TICKETS PENDIENTES DE ASIGNAR-----------------------------')
    print('\n')
    print(dfGito)
    print('\n')

elif(args.informe == 'present'):
    print('Obteniendo tickets...')
    tickets = update_tickets()[0]

    print('Obteniendo alarmas...')
    alarmas = get_alarms()

    print('Creando informe...')

    # Creando tablas dinamicas
    tabla_resumen = pd.pivot_table(alarmas,
                                   index='Especialidad',
                                   columns='Severidad',
                                   values='Descripcion',
                                   aggfunc=lambda x: len(x),
                                   fill_value=0,
                                   margins=True,
                                   margins_name='Total'
                                   )

    tabla_alarmas = pd.pivot_table(alarmas,
                                   index=['Especialidad',
                                          'Fuente', 'Descripcion'],
                                   columns='Severidad',
                                   aggfunc=lambda x: len(x),
                                   fill_value=0,
                                   )

    with pd.ExcelWriter(PATH + '/data/Informe.xlsx', engine='xlsxwriter') as writer:
        tabla_resumen.to_excel(writer, sheet_name='Resumen')
        tabla_alarmas.to_excel(writer, sheet_name='ResumenXNodo')
        tickets.to_excel(writer, sheet_name="Tickets", index=False)
        alarmas.to_excel(writer, sheet_name="Alarmas", index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        wsTickets = writer.sheets['Tickets']
        wsAlarmas = writer.sheets['Alarmas']

        # Get the dimensions of the dataframe.
        (max_row_tic, max_col_tic) = tickets.shape
        (max_row_al, max_col_al) = alarmas.shape

        # Create a list of column headers, to use in add_table().
        column_settings_tic = [{'header': column}
                               for column in tickets.columns]
        column_settings_al = [{'header': column} for column in alarmas.columns]

        # Add the Excel table structure. Pandas will add the data.
        wsTickets.add_table(0, 0, max_row_tic, max_col_tic - 1,
                            {'columns': column_settings_tic})
        wsAlarmas.add_table(0, 0, max_row_al, max_col_al - 1,
                            {'columns': column_settings_al})

        # Make the columns wider for clarity.
        wsTickets.set_column(0, max_col_tic - 1, 18)
        wsAlarmas.set_column(0, max_col_al - 1, 18)

    print('Informe creado')


elif(args.alarmas == 'present'):
    alarmas = get_alarms()
    print(alarmas)

elif(args.usuarios == 'present'):
    update_users()

else:
    print(parser.print_help())

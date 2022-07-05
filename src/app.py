import argparse

from actions.update_tickets import *

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
    dfPlataforma, dfGito = update_tickets()
    print('\n')
    print(dfPlataforma)
    print('\n')
    print('-----------------------TICKETS PENDIENTES DE ASIGNAR-----------------------------')
    print('\n')
    print(dfGito)
    print('\n')

elif(args.informe == 'present'):
    print('Realizar informe para la reunion de operaciones')

elif(args.alarmas == 'present'):
    print('Realizar resumen de alarmas')

elif(args.usuarios == 'present'):
    print("Resumen de usuarios")

else:
    print(parser.print_help())

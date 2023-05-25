from os import system, name

def limpiar():
    '''Limpia la pantalla de terminal en equipos Windows o Linux'''
    system('cls' if name == 'nt' else 'clear')

def decorar_opcion(num, text):
    print('   ---------------')
    print(f'{num}) {text}')
    print('   ---------------')

def obtener_intrucciones():
    print('Los jugadores tendrán en su poder un mazo de cartas, con las que podrán lanzar cartas a las del contrario.')
    print('Objtetivo: Debilitar los PS de las cartas del contrario, manteniendo los puntos de magia de uno')
    print('Por cada turno puedes elegir una carta para atacar, curar una carta más de una vez o directamente salir del juego')
    print('El ganador sera el que pueda mantener su mazo de cartas hasta el final.')
    print('!Diviértete jugando PyCards :)¡.')
    print('\n*\n* By Diego Gomez :)')

logotipo = '''
            _____        _____              _     
            |  __ \      / ____|            | |    
            | |__) |   _| |     __ _ _ __ __| |___ 
            |  ___/ | | | |    / _` | '__/ _` / __|
            | |   | |_| | |___| (_| | | | (_| \__ \\
            |_|    \__, |\_____\__,_|_|  \__,_|___/
                    __/ |                          
                    |___/                           
        '''

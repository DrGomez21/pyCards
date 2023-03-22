import juego
import tablero
import jugador
import carta as c
import ataques.ataque as atq


def menu_bienvenida():
    '''Mostrar un menu de bienvenida. La pantalla inicial del juego.'''
    print('''
        _____        _____              _     
        |  __ \      / ____|            | |    
        | |__) |   _| |     __ _ _ __ __| |___ 
        |  ___/ | | | |    / _` | '__/ _` / __|
        | |   | |_| | |___| (_| | | | (_| \__ \\
        |_|    \__, |\_____\__,_|_|  \__,_|___/
                __/ |                          
                |___/                           
    ''')
    
    print('1) Tablero especial\n2) Tablero basico')
    op = int(input('Elige un tablero para empezar:'))
    while op < 1 or op > 2:
        op = input('Elige un tablero para empezar:')

    if op == 1:
        return tablero.TableroEspecial('Potenciar')
    else:
        return tablero.TableroBasico('Potenciar')

tab = menu_bienvenida()

player1 = jugador.Jugador('Diego', [
    c.CartaBasica('Messi', 'Mundial', 10, 4, atq.Derribo()),
    c.CartaMagica('CR7', 'SIUUU', 10, 4, atq.FuerzaMagica(), 8)
], 10)

player2 = jugador.Jugador('Rival', [
    c.CartaBasica('Goku', 'SSJ', 8, 4, atq.FuerzaPsiquica()),
    c.CartaBasica('Vegeta', 'Principe', 7, 4, atq.Derribo())
], 8)

game = juego.Juego(tab, player1, player2)
game.jugar(player1, player2)
game.ver_ganador()

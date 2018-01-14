#3rd party modules
import libtcodpy as libtcod
import pygame

#game files
import constants

#=================================================================
#   _____ _______ _____  _    _  _____ _______ _    _ _____  ______  _____ 
#  / ____|__   __|  __ \| |  | |/ ____|__   __| |  | |  __ \|  ____|/ ____|
# | (___    | |  | |__) | |  | | |       | |  | |  | | |__) | |__  | (___  
#  \___ \   | |  |  _  /| |  | | |       | |  | |  | |  _  /|  __|  \___ \ 
#  ____) |  | |  | | \ \| |__| | |____   | |  | |__| | | \ \| |____ ____) |
# |_____/   |_|  |_|  \_\\____/ \_____|  |_|   \____/|_|  \_\______|_____/ 

class struc_Tile:
    def __init__ (self, block_path):
        self.block_path = block_path



#=================================================================
#  __  __          _____  
# |  \/  |   /\   |  __ \ 
# | \  / |  /  \  | |__) |
# | |\/| | / /\ \ |  ___/ 
# | |  | |/ ____ \| |     
# |_|  |_/_/    \_\_| 


def map_create():
    new_map = [[ struc_Tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map

#=================================================================
#  _____  _____       __          _______ _   _  _____  _____ 
# |  __ \|  __ \     /\ \        / /_   _| \ | |/ ____|/ ____|
# | |  | | |__) |   /  \ \  /\  / /  | | |  \| | |  __| (___  
# | |  | |  _  /   / /\ \ \/  \/ /   | | | . ` | | |_ |\___ \ 
# | |__| | | \ \  / ____ \  /\  /   _| |_| |\  | |__| |____) |
# |_____/|_|  \_\/_/    \_\/  \/   |_____|_| \_|\_____|_____/ 
                                        

def draw_game():    #SyntaxError - all function should end with ":"

    global SURFACE_MAIN

    # clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
    #TODO Draw the map
    draw_map(GAME_MAP)

    # draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, ( 200, 200 ))

    # update the display (flip and update)
    pygame.display.flip()

def draw_map(map_to_draw):

    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                #draw wall
                SURFACE_MAIN.blit(constants.S_WALL, ( x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT ))

            else:
                #draw floor
                SURFACE_MAIN.blit(constants.S_FLOOR, ( x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT ))


#=================================================================
#  _____          __  __ ______ 
#  / ____|   /\   |  \/  |  ____|
# | |  __   /  \  | \  / | |__   
# | | |_ | / /\ \ | |\/| |  __|  
# | |__| |/ ____ \| |  | | |____ 
#  \_____/_/    \_\_|  |_|______|


def game_main_loop():
    '''In this function we loop the main game?'''
    game_quit = False

    while not game_quit:

        #get player input
        events_list = pygame.event.get()

        #TODO process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        # draw the game
        draw_game()

    #quit the game
    pygame.quit() #was an error IndentationError: unindent does not match any outer indentation level. Cause - inside def game_main_loop() there were 5 spaces instead of 4
    exit()



def game_initialize():
    '''This function initialize main window and pygame'''
    global SURFACE_MAIN, GAME_MAP

    #initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

    GAME_MAP = map_create()

#=================================================================

# RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUUNNNNNNNN        NNNNNNNN
# R::::::::::::::::R  U::::::U     U::::::UN:::::::N       N::::::N
# R::::::RRRRRR:::::R U::::::U     U::::::UN::::::::N      N::::::N
# RR:::::R     R:::::RUU:::::U     U:::::UUN:::::::::N     N::::::N
#   R::::R     R:::::R U:::::U     U:::::U N::::::::::N    N::::::N
#   R::::R     R:::::R U:::::D     D:::::U N:::::::::::N   N::::::N
#   R::::RRRRRR:::::R  U:::::D     D:::::U N:::::::N::::N  N::::::N
#   R:::::::::::::RR   U:::::D     D:::::U N::::::N N::::N N::::::N
#   R::::RRRRRR:::::R  U:::::D     D:::::U N::::::N  N::::N:::::::N
#   R::::R     R:::::R U:::::D     D:::::U N::::::N   N:::::::::::N
#   R::::R     R:::::R U:::::D     D:::::U N::::::N    N::::::::::N
#   R::::R     R:::::R U::::::U   U::::::U N::::::N     N:::::::::N
# RR:::::R     R:::::R U:::::::UUU:::::::U N::::::N      N::::::::N
# R::::::R     R:::::R  UU:::::::::::::UU  N::::::N       N:::::::N
# R::::::R     R:::::R    UU:::::::::UU    N::::::N        N::::::N
# RRRRRRRR     RRRRRRR      UUUUUUUUU      NNNNNNNN         NNNNNNN

def main():
    game_initialize()
    game_main_loop()

if __name__ == '__main__':
    main()


#    print "j"

#game_main_loop()
#
#if __name__ == '__main__':
#    print "k"
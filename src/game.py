#3rd party modules
import libtcodpy as libtcod
import pygame

#game files
import constants
import gamelogger
import logging
import mapcoordinates

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
#   ____  ____       _ ______ _____ _______ _____ 
#  / __ \|  _ \     | |  ____/ ____|__   __/ ____|
# | |  | | |_) |    | | |__ | |       | | | (___  
# | |  | |  _ < _   | |  __|| |       | |  \___ \ 
# | |__| | |_) | |__| | |___| |____   | |  ____) |
#  \____/|____/ \____/|______\_____|  |_| |_____/ 

class obj_Actor:
    def __init__(self, x, y, sprite):
        self.x = x #map address, not pixel
        self.y = y #map address, not pixel
        self.sprite = sprite

    def draw(self, surface, mapCoord):
        surface.blit(self.sprite, (mapCoord.xLP2DP(self.x), mapCoord.yLP2DP(self.y) ))

    def move(self, dx, dy, gameMap, mapCoord):
        x = int(round(self.x))
        y = int(round(self.y))
        if gameMap[x + dx][y + dy].block_path == False:
            self.x += dx
            self.y += dy
            mapCoord.shift(dx, dy)

            # logging.debug('Player position %d %d', self.x, self.y)

class Game:

    def __init__(self):
        logging.info('Game initialization')
        self.game_initialize()

    def run(self):
        logging.info('Start main loop')
        self.game_main_loop()
#=================================================================
#  __  __          _____  
# |  \/  |   /\   |  __ \ 
# | \  / |  /  \  | |__) |
# | |\/| | / /\ \ |  ___/ 
# | |  | |/ ____ \| |     
# |_|  |_/_/    \_\_| 


    def map_create(self):
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
                                        

    def draw_game(self):    #SyntaxError - all function should end with ":"

        # clear the surface
        self.SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
        #TODO Draw the map
        self.draw_map(self.GAME_MAP)

        # draw the character  ???
        self.PLAYER.draw(self.SURFACE_MAIN, self.mapCoord)

        # update the display (flip and update)
        pygame.display.flip()

    def draw_map(self, map_to_draw):

        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if map_to_draw[x][y].block_path == True:
                    #draw wall

                    self.SURFACE_MAIN.blit(constants.S_WALL, (self.mapCoord.xLP2DP(x), self.mapCoord.yLP2DP(y) ))

                else:
                    #draw floor
                    self.SURFACE_MAIN.blit(constants.S_FLOOR, (self.mapCoord.xLP2DP(x), self.mapCoord.yLP2DP(y) ))


#=================================================================
#  _____          __  __ ______ 
#  / ____|   /\   |  \/  |  ____|
# | |  __   /  \  | \  / | |__   
# | | |_ | / /\ \ | |\/| |  __|  
# | |__| |/ ____ \| |  | | |____ 
#  \_____/_/    \_\_|  |_|______|


    def game_main_loop(self):
        '''In this function we loop the main game?'''
        game_quit = False

        while not game_quit:

            #get player input
            events_list = pygame.event.get()

            # process input
            for event in events_list:
                if event.type == pygame.QUIT:
                    game_quit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.PLAYER.move(0, 1, self.GAME_MAP, self.mapCoord)
                    if event.key == pygame.K_DOWN:
                        self.PLAYER.move(0, -1, self.GAME_MAP, self.mapCoord)
                    if event.key == pygame.K_LEFT:
                        self.PLAYER.move(-1, 0, self.GAME_MAP, self.mapCoord)
                    if event.key == pygame.K_RIGHT:
                        self.PLAYER.move(1, 0, self.GAME_MAP, self.mapCoord)

            # draw the game
            self.draw_game()

        #quit the game
        pygame.quit() #was an error IndentationError: unindent does not match any outer indentation level. Cause - inside def game_main_loop() there were 5 spaces instead of 4
        exit()



    def game_initialize(self):
        '''This function initialize main window and pygame'''

        #initialize pygame
        pygame.init()
        self.mapCoord = mapcoordinates.constructPositive(screenWidth=constants.GAME_WIDTH, screenHeight=constants.GAME_HEIGHT, mapWidth=constants.MAP_WIDTH, mapHeight=constants.MAP_HEIGHT, tileSize=constants.CELL_WIDTH)

        self.SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

        self.GAME_MAP = self.map_create()

        mapCenter = self.mapCoord.mapRect.centre()
        self.PLAYER = obj_Actor(mapCenter.x, mapCenter.y, constants.S_PLAYER)

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
    gamelogger.init()

    game = Game()
    game.run()


# if __name__ == '__main__':
    # main()


#    print "j"

#game_main_loop()
#
#if __name__ == '__main__':
#    print "k"
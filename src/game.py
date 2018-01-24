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

class struc_Tile(object):
    def __init__ (self, block_path):
        self.block_path = block_path


#=================================================================
#   _____ ____  __  __ _____   ____  _   _ ______ _   _ _______ _____ 
#  / ____/ __ \|  \/  |  __ \ / __ \| \ | |  ____| \ | |__   __/ ____|
# | |   | |  | | \  / | |__) | |  | |  \| | |__  |  \| |  | | | (___  
# | |   | |  | | |\/| |  ___/| |  | | . ` |  __| | . ` |  | |  \___ \ 
# | |___| |__| | |  | | |    | |__| | |\  | |____| |\  |  | |  ____) |
#  \_____\____/|_|  |_|_|     \____/|_| \_|______|_| \_|  |_| |_____/ 

class com_Creature(object):
    '''Creatures have health, and can damage objects by attacking, can also die'''
    def __init__(self, name_instance, hp = 10):
        self.name_instance = name_instance
        self.hp = hp

        
#TODO class com_Item(object):
#     """docstring for com_Item"""
#     def __init__(self, arg):
#         super(com_Item, self).__init__()
#         self.arg = arg
        
#TODO class com_Container(object):
#     """docstring for com_Container"""
#     def __init__(self, arg):
#         super(com_Container, self).__init__()
#         self.arg = arg



#=================================================================
#           _____ 
#     /\   |_   _|
#    /  \    | |  
#   / /\ \   | |  
#  / ____ \ _| |_ 
# /_/    \_\_____|

class ai_Test(object):
    '''Execute once per turn'''
    def take_turn(self, gameMap, gameObjects, mapCoord):
        self.owner.move(libtcod.random_get_int(0, -1, 1), libtcod.random_get_int(0, -1, 1), gameMap, gameObjects, mapCoord)
        # self.owner.move(0, 0, gameMap, gameObjects, mapCoord)


#=================================================================
#   ____  ____       _ ______ _____ _______ _____ 
#  / __ \|  _ \     | |  ____/ ____|__   __/ ____|
# | |  | | |_) |    | | |__ | |       | | | (___  
# | |  | |  _ < _   | |  __|| |       | |  \___ \ 
# | |__| | |_) | |__| | |___| |____   | |  ____) |
#  \____/|____/ \____/|______\_____|  |_| |_____/ 

class obj_Actor(object):
    def __init__(self, x, y, name_object, sprite, creature = None, ai = None):
        self.x = x #map address, not pixel
        self.y = y #map address, not pixel
        self.sprite = sprite

        self.creature = creature
        if creature:
            creature.owner = self

        self.ai = ai
        if ai:
            ai.owner = self


    def draw(self, surface, mapCoord):
        surface.blit(self.sprite, (mapCoord.xLP2DP(self.x), mapCoord.yLP2DP(self.y) ))

    def extraMove(self, dx, dy, mapCoord):
        pass

    def move(self, dx, dy, gameMap, gameObjects, mapCoord):
        x = int(round(self.x))
        y = int(round(self.y))

        tile_is_wall = (gameMap[x + dx][y + dy].block_path == True)

        target = None

        for object in gameObjects:
            if (object is not self and
                object.x == self.x + dx and
                object.y == self.y + dy and
                object.creature):
                target = object
                break

        if target:
            logging.info(self.creature.name_instance + " attacks " + target.creature.name_instance)

        if not tile_is_wall and target is None:
            self.x += dx
            self.y += dy
            self.extraMove(dx, dy, mapCoord)

            # logging.debug('Player position %d %d', self.x, self.y)



class Player(obj_Actor):
    """player actor"""
    def __init__(self, x, y, name_object, sprite, creature = None, ai = None):
        super(Player, self).__init__(x, y, name_object, sprite, creature, ai)
 

    def extraMove(self, dx, dy, mapCoord):
        super(Player, self).extraMove(dx, dy, mapCoord)
        mapCoord.shift(dx, dy)
        

class Game(object):

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

        self.border_create2(new_map)

        return new_map

    def border_create(self, new_map):
        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if x < constants.MAP_WIDTH:
                    if y == 0:
                        new_map[x][y].block_path = True

        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if x == 0 :
                    if y < constants.MAP_HEIGHT:
                        new_map[x][y].block_path = True

        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if x >= constants.MAP_WIDTH - 1:
                    if y < constants.MAP_HEIGHT:
                        new_map[x][y].block_path = True
                        
        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if x < constants.MAP_WIDTH:
                    if y >= constants.MAP_HEIGHT - 1:
                        new_map[x][y].block_path = True                                        

    def border_create2(self, new_map):
        for x in range(0, constants.MAP_WIDTH):
            new_map[x][0].block_path = True
            new_map[x][constants.MAP_HEIGHT-1].block_path = True

        for y in range(0, constants.MAP_HEIGHT):    
            new_map[0][y].block_path = True
            new_map[constants.MAP_WIDTH-1][y].block_path = True



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
        # self.ENEMY.draw(self.SURFACE_MAIN, self.mapCoord)
        # # draw the character  ???
        # self.PLAYER.draw(self.SURFACE_MAIN, self.mapCoord)

        #draw all objects
        for obj in self.GAME_OBJECTS:
            obj.draw(self.SURFACE_MAIN, self.mapCoord)

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

        #player action definition ???
        player_action = "no-action"

        while not game_quit:

            #handle the keys
            player_action = self.game_handle_keys()

            if player_action == "QUIT":
                game_quit = True

                # logging.debug("action = %s", player_action)
            elif player_action != "no-action":
                for obj in self.GAME_OBJECTS:
                    if obj.ai:
                        obj.ai.take_turn(self.GAME_MAP, self.GAME_OBJECTS, self.mapCoord)


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


        creature_com1 = com_Creature("greg")
        mapCenter = self.mapCoord.mapRect.centre()
        self.PLAYER = Player(mapCenter.x, mapCenter.y, "human", constants.S_PLAYER, creature = creature_com1)

        creature_com2 = com_Creature("jackie")
        ai_com = ai_Test()
        self.ENEMY = obj_Actor(10, 5, "carrot", constants.S_ENEMY, creature = creature_com2, ai = ai_com)

        self.GAME_OBJECTS = [self.ENEMY, self.PLAYER]


    def game_handle_keys(self):

        #get player input
        events_list = pygame.event.get()

        # process input
        for event in events_list:
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.PLAYER.move(0, 1, self.GAME_MAP, self.GAME_OBJECTS, self.mapCoord)
                    return "player-moved"
                if event.key == pygame.K_DOWN:
                    self.PLAYER.move(0, -1, self.GAME_MAP, self.GAME_OBJECTS,  self.mapCoord)
                    return "player-moved"
                if event.key == pygame.K_LEFT:
                    self.PLAYER.move(-1, 0, self.GAME_MAP, self.GAME_OBJECTS,  self.mapCoord)
                    return "player-moved"
                if event.key == pygame.K_RIGHT:
                    self.PLAYER.move(1, 0, self.GAME_MAP, self.GAME_OBJECTS,  self.mapCoord)
                    return "player-moved"

        return "no-action"
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
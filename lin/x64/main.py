import pygame
import sys
import os
import libtcodpy as libtcod

# Launch this script file to start
if __name__ == '__main__':
    scriptPath = os.path.dirname(sys.argv[0]) # Detect script path
    sourcesPath = scriptPath + "/../../src" # Detect where are the sources located

    sys.path.insert(0,sourcesPath) # Make all the sources visible
    os.chdir(sourcesPath) # Change working directory to source directory

    import game
    game.main() # Run the thing

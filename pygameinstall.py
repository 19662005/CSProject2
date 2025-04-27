#importing pygame
import pygame
import sys
pygame.init()
#pygame.display.set_mode((640, 480))
#pygame.display.set_caption("Pygame Installation Test")

#setting up the game window
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harm Reduction Adventure")

#Setting up colors so we can use them later - can be changed later on
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230) 
DARK_BLUE = (0, 0, 139)

#Setting up the font - can be changed later on
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)


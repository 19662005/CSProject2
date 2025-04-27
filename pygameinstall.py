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

# Setting up the game screens (also called states), which we'll use to help track what we are displaying and so that things aren't played all at once
START_SCREEN = "start"
SCENARIO_SELECT = "select"
current_screen = START_SCREEN

#setting up 'buttons' - these are the clickable areas on the screen that will take you to different screens
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = LIGHT_BLUE
        self.callback = callback
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, DARK_BLUE, self.rect, 3)  # border
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

#setting up the buttons for the start screen    
def start_game():
    global current_screen
    current_screen = SCENARIO_SELECT

#Later on this is where the code for the actual scenes of each scenario will go
def scenario_1():
    print("Scenario 1 selected")

def scenario_2():
    print("Scenario 2 selected")

def scenario_3():
    print("Scenario 3 selected")

#Setting up the buttons for the scenario select screen - these will be used to select which scenario to play
start_button = Button("Start", WIDTH//2 - 100, HEIGHT//2 - 40, 200, 80, start_game)
scenario_buttons = [
    Button("Scenario 1", WIDTH//2 - 150, 150, 300, 60, scenario_1),
    Button("Scenario 2", WIDTH//2 - 150, 250, 300, 60, scenario_2),
    Button("Scenario 3", WIDTH//2 - 150, 350, 300, 60, scenario_3),
]


running = True #keeps running the game until you close it.
while running:
    screen.fill(WHITE) #white background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if current_screen == START_SCREEN:
                if start_button.is_clicked(pos):
                    start_button.callback()
            elif current_screen == SCENARIO_SELECT:
                for button in scenario_buttons:
                    if button.is_clicked(pos):
                        button.callback()
    if current_screen == START_SCREEN:
        start_button.draw(screen)
    elif current_screen == SCENARIO_SELECT:
        title_surf = small_font.render("Choose Your Scenario:", True, BLACK)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 50))
        screen.blit(title_surf, title_rect)
        for button in scenario_buttons:
            button.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
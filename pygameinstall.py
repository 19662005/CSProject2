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
SCENARIO_1_SCREEN = "scenario_1"
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
    global current_screen
    current_screen = SCENARIO_1_SCREEN

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
#set up scenario 1
question = "You are at a nightclub and a close friend offers you a pill. What do you do?"
selected_option = None
feedback = ""
options = [
    "Take the pill"
    "Ask what it is and who it came from"
    "Use a fentanyl test strip"
    "Deny"
] 

#create responses given the player's choice
def option_selected(index):
    global selected_option, feedback
    selected_option = index
    if index == 0:
        feedback = "This puts you at a large risk for fentanyl or other unknown drug overdose. Always ask what the source of the drug is and always test with a fentanyl test strip."
    elif index == 1:
        feedback = "Good job asking the source!"
    elif index == 2:
        feedback = "Great job using the strip. The test came back positive and you just saved your life."
    elif index == 3:
        feedback = "Great job standing strong. If you are not comfortable with a substance - do not take it!"

#Create the buttons for scenario 1
scenario_1_buttons = [
    Button ("Take the pill", WIDTH//2 - 250, 100, 500, 60, lambda: option_selected (0)),
    Button ("Ask what it is and who it came from", WIDTH//2 - 250, 180, 500, 60, lambda:option_selected(1)),
    Button ("Use fentanyl test strip", WIDTH // 2 - 250, 260, 500, 60, lambda: option_selected (2)),
    Button ("Deny", WIDTH // 2 - 250, 340, 500, 60, lambda: option_selected (3)),
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
    elif current_screen == SCENARIO_1_SCREEN:
        question_surf = small_font.render (question, True, BLACK)
        screen.blit (question_surf, (30, 30))
        for button in scenario_1_buttons:
            button.draw(screen)
        if selected_option is not None:
            feedback_surf = small_font.render (feedback, True, BLACK)
            screen.blit (feedback_surf, (30, 430))
    pygame.display.update()

pygame.quit()
sys.exit()
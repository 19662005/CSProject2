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

# Loading fentanyl summary image
try:
    summary_image = pygame.image.load("fentanyllethaldosage.png")
    summary_image = pygame.transform.scale(summary_image, (180, 180))
except:
    summary_image = None  # Fail gracefully if image not found


# Setting up the game screens (also called states), which we'll use to help track what we are displaying and so that things aren't played all at once
START_SCREEN = "start"
SCENARIO_SELECT = "select"
current_screen = START_SCREEN
SCENARIO_3_SCREEN = "scenario3_scene1"
SCENARIO_3_SCENE2 = "scenario3_scene2"
SCENARIO_3_SCENE3 = "scenario3_scene3"
SUMMARY_SCREEN = "summary"

SCENARIO_1_SCREEN = "scenario1_scene1"
SCENARIO_1_SCENE2 = "scenario1_scene2"
SCENARIO_1_SCENE3 = "scenario1_scene3"

SCENARIO_2_SCREEN = 'scenario_2_screen'
SCENARIO_2_SCENE2 = 'scenario_2_scene2'


# Define the draw_wrapped_text function
def draw_wrapped_text(surface, text, x, y, font, color, width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        test_width = font.size(test_line)[0]
        if test_width <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    
    # Add the last line
    lines.append(' '.join(current_line))
    
    # Draw each line
    current_height = y
    for line in lines:
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, current_height))
        current_height += font.get_height() + 2

#setting up 'buttons' - these are the clickable areas on the screen that will take you to different screens
class Button:
    def __init__(self, text, x, y, width, height, callback, font=font):  # default is large font
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = LIGHT_BLUE
        self.callback = callback
        self.font = font  # store the font for use later

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, DARK_BLUE, self.rect, 3)  # border
        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

#setting up the buttons for the start screen    
def start_game():
    global current_screen
    current_screen = SCENARIO_SELECT

def play_again():
    global current_screen, scenario1_selected, scenario1_selected2, scenario1_selected3, scenario2_selected1, scenario2_selected2, scenario3_selected, scenario3_selected2, scenario3_selected3
    scenario1_selected = None
    scenario1_selected2 = None
    scenario1_selected3 = None
    scenario3_selected = None
    scenario3_selected2 = None
    scenario3_selected3 = None
    current_screen = SCENARIO_SELECT
    scenario2_selected1 = None
    scenario2_selected2 = None

def exit_game():
    pygame.quit()
    sys.exit()


# Setting up the summary screen and loading the image
def draw_summary_screen():
    screen.fill(WHITE)
    summary_font = pygame.font.SysFont(None, 28)  # or 24 if you want it smaller

    # Display a summary message
    summary_text = (
        "Great job navigating tough choices! This game highlights the importance of: Asking questions, Testing unknown substances, Saying no when unsure, and Calling for help in emergencies"
        " Remember: Even small amounts of fentanyl can be deadly. Always test substances, stay informed, and prioritize safety."
    )

    draw_wrapped_text(screen, summary_text, 30, 30, small_font, BLACK, WIDTH - 60)

    # Display the fentanyl image
    if summary_image:
        img_rect = summary_image.get_rect(center=(WIDTH // 2, 310))
        screen.blit(summary_image, img_rect)
    # Draw Play Again and Exit buttons
    for button in summary_buttons:
        button.draw(screen)
summary_buttons = [
    Button("Play Again", WIDTH // 2 - 150, 420, 140, 50, play_again, small_font),
    Button("Exit", WIDTH // 2 + 10, 420, 140, 50, exit_game, small_font)
]

#This is where the code for the actual scenes of each scenario goes
# Scenario 1 Scene 1 prompt
def scenario_1():
    global current_screen
    current_screen = SCENARIO_1_SCREEN

scenario1_question1 = "You're at a music festival and someone offers you a mysterious pill. What do you do?"
scenario1_feedback = ""
scenario1_selected = None

# Scenario 1 Scene 1 answers options
scenario1_buttons1 = [
    Button("Take it", WIDTH//2 - 200, 100, 400, 60, lambda: scenario1_option1_selected(0)),
    Button("Use a fentanyl test strip", WIDTH//2 - 200, 180, 400, 60, lambda: scenario1_option1_selected(1)),
    Button("Say no", WIDTH//2 - 200, 260, 400, 60, lambda: scenario1_option1_selected(2)),
]

# Scenario 1 Scene 1 feedback and responses
def scenario1_option1_selected(index):
    global scenario1_selected, scenario1_feedback, current_screen
    scenario1_selected = index
    if index == 0:
        scenario1_feedback = "You took the pill and feel very sick — you're at risk of overdose."
    elif index == 1:
        scenario1_feedback = "You found out it was laced with fentanyl and saved yourself."
    elif index == 2:
        scenario1_feedback = "Good call! You said no. You move on to watch the performance."
    pygame.time.set_timer(pygame.USEREVENT + 3, 2500)  # Wait for 2.5 seconds before transitioning

# Scenario 1 Scene 2 prompt
scenario1_question2 = "You've taken an unknown pill from your older sibling and went to a party with friends, but you start to feel dizzy. What do you do?"
scenario1_feedback2 = ""
scenario1_selected2 = None

# Scenario 1 Scene 2 options
scenario1_buttons2 = [
    Button("Go to the bathroom alone", WIDTH//2 - 200, 120, 400, 60, lambda: scenario1_option2_selected(0)),
    Button("Go outside with a friend", WIDTH//2 - 200, 200, 400, 60, lambda: scenario1_option2_selected(1)),
    Button("Call 911", WIDTH//2 - 200, 280, 400, 60, lambda: scenario1_option2_selected(2)),
]

# Scenario 1 Scene 2 feedback and responses
def scenario1_option2_selected(index):
    global scenario1_selected2, scenario1_feedback2
    scenario1_selected2 = index
    if index == 0:
        scenario1_feedback2 = "You risk the chance of an overdose with no help. This is dangerous"
    elif index == 1:
        scenario1_feedback2 = "You risk the chance of an overdose, but you do have a trusted individual to call for help if needed. This is still dangerous."
    elif index == 2:
        scenario1_feedback2 = "You called 911 and medical professionals were able to help you avoid an overdose."
    pygame.time.set_timer(pygame.USEREVENT + 4, 2500)


# Scenario 1 Scene 3 prompt
scenario1_question3 = "You and your friends get offered a pill at a night club. What do you do?"
scenario1_feedback3 = ""
scenario1_selected3 = None

# Scenario 1 Scene 3 options
scenario1_buttons3 = [
    Button("Take it", WIDTH//2 - 200, 100, 400, 60, lambda: scenario1_option3_selected(0)),
    Button("Ask where it is from", WIDTH//2 - 200, 180, 400, 60, lambda: scenario1_option3_selected(1)),
    Button("Say no", WIDTH//2 - 200, 260, 400, 60, lambda: scenario1_option3_selected(2)),
]

# Scenario 1 Scene 3 feedback and responses
def scenario1_option3_selected(index):
    global scenario1_selected3, scenario1_feedback3
    scenario1_selected3 = index
    if index == 0:
        scenario1_feedback3 = "You are at risk of overdose. This is dangerous."
    elif index == 1:
        scenario1_feedback3 = "Your friend starts acting concerning. You call for help and save their life."
    elif index == 2:
        scenario1_feedback3 = "The pill tested positive for fentynal. You saved you and your friends' lives."
    pygame.time.set_timer(pygame.USEREVENT + 2, 2500)


def scenario_2():
    global current_screen
    current_screen = SCENARIO_2_SCREEN

#Scenario 2 Scene 1 prompt
scenario2_question1 = "At a music festival, you're offered a pill. You refuse, but your friend takes it and starts acting weird. What do you do?"
scenario2_feedback1 = ""
scenario2_selected1 = None

# Scenario 2 Scene 1 answers options
scenario2_buttons1 = [
    Button("Let them walk it off", WIDTH//2 - 200, 120, 400, 60, lambda: scenario2_scene1_choice(0)),
    Button("Keep an eye on them", WIDTH//2 - 200, 200, 400, 60, lambda: scenario2_scene1_choice(1)),
    Button("Take it yourself", WIDTH//2 - 200, 280, 400, 60, lambda: scenario2_scene1_choice(2)),
]

# Scenario 2 Scene 1 feedback and responses
def scenario2_scene1_choice(index):
    global scenario2_selected1, scenario2_feedback1
    scenario2_selected1 = index
    if index == 0:
        scenario2_feedback1 = "Letting them walk it off is dangerous. They may not wake up."
    elif index == 1:
        scenario2_feedback1 = "Keeping an eye on them may save them."
    elif index == 2:
        scenario2_feedback1 = "Taking it too puts you both at risk."
    pygame.time.set_timer(pygame.USEREVENT + 5, 2500)

# Scenario 2 Scene 2 prompt
scenario2_question2 = "Your friend is unconscious and struggling to breathe. What do you do?"
scenario2_feedback2 = ""
scenario2_selected2 = None

# Scenario 2 Scene 2 options
scenario2_buttons2 = [
    Button("Call 911, check for pulse", WIDTH//2 - 200, 120, 400, 60, lambda: scenario2_scene2_choice(0)),
    Button("Move to a quiet place", WIDTH//2 - 200, 200, 400, 60, lambda: scenario2_scene2_choice(1)),
    Button("Wait for another friend", WIDTH//2 - 200, 280, 400, 50, lambda: scenario2_scene2_choice(2)),
]

# Scenario 2 Scene 2 feedback and responses
def scenario2_scene2_choice(index):
    global scenario2_selected2, scenario2_feedback2
    scenario2_selected2 = index
    if index == 0:  
        scenario2_feedback2 = "Great response. You might have saved your friend’s life."
    elif index == 1:
        scenario2_feedback2 = "You risk your friend's chance of an overdose. This is very dangerous."
    elif index == 2:
        scenario2_feedback2 = "You and your friend are not equipped in case of an overdose. This is dangerous."
    pygame.time.set_timer(pygame.USEREVENT + 2, 2500)


def scenario_3():
    global current_screen
    current_screen = SCENARIO_3_SCREEN

#Scenario 3 Scene 1 prompt
scenario3_question1 = "You’re exhausted and someone offers you a 'study pill'. What do you do?"
scenario3_feedback = ""
scenario3_selected = None

# Scenario 3 Scene 1 answers options
scenario3_buttons1 = [
    Button("Take it", WIDTH//2 - 200, 100, 400, 60, lambda: scenario3_option1_selected(0)),
    Button("Google it first", WIDTH//2 - 200, 180, 400, 60, lambda: scenario3_option1_selected(1)),
    Button("Say no", WIDTH//2 - 200, 260, 400, 60, lambda: scenario3_option1_selected(2)),
]

# Scenario 3 Scene 1 feedback and responses
def scenario3_option1_selected(index):
    global scenario3_selected, scenario3_feedback, current_screen
    scenario3_selected = index
    if index == 0:
        scenario3_feedback = "You took the pill and feel very sick — you're at risk of overdose."
    elif index == 1:
        scenario3_feedback = "You googled it — it’s not prescribed to you and could be dangerous."
    elif index == 2:
        scenario3_feedback = "Good call! You said no. You move on to the celebration."

    # Display feedback and set timer for transition
    pygame.time.set_timer(pygame.USEREVENT + 1, 2500)  # Wait for 1.5 seconds before transitioning

# Scenario 3 Scene 2 prompt
scenario3_question2 = "You’re out celebrating and someone hands you a gummy they say is 'just weed.' What do you do?"
scenario3_feedback2 = ""
scenario3_selected2 = None

# Scenario 3 Scene 2 options
scenario3_buttons2 = [
    Button("Say no", WIDTH//2 - 200, 100, 400, 60, lambda: scenario3_option2_selected(0)),
    Button("Take it", WIDTH//2 - 200, 180, 400, 60, lambda: scenario3_option2_selected(1)),
    Button("Ask what’s in it", WIDTH//2 - 200, 260, 400, 60, lambda: scenario3_option2_selected(2)),
]

# Scenario 3 Scene 2 feedback and responses
def scenario3_option2_selected(index):
    global scenario3_selected2, scenario3_feedback2
    scenario3_selected2 = index
    if index == 0:
        scenario3_feedback2 = "You said no. 15 minutes later, others feel lightheaded."
    elif index == 1:
        scenario3_feedback2 = "You took it and feel very lightheaded. This is dangerous."
    elif index == 2:
        scenario3_feedback2 = "You found out it was laced with fentanyl."

    # Wait before transition to Scene 3
    pygame.time.set_timer(pygame.USEREVENT + 1, 2500)

# Scenario 3 Scene 3 prompt
scenario3_question3 = "3/4 of those at the party display distressing signs. You want to call 911, but others threaten you. What do you do?"
scenario3_feedback3 = ""
scenario3_selected3 = None

# Scenario 3 Scene 3 options
scenario3_buttons3 = [
    Button("Call 911 anyway", WIDTH//2 - 200, 120, 400, 60, lambda: scenario3_option3_selected(0)),
    Button("Leave the party", WIDTH//2 - 200, 200, 400, 60, lambda: scenario3_option3_selected(1)),
    Button("Wait and see", WIDTH//2 - 200, 280, 400, 60, lambda: scenario3_option3_selected(2)),
]

# Scenario 3 Scene 3 feedback and responses
def scenario3_option3_selected(index):
    global scenario3_selected3, scenario3_feedback3
    scenario3_selected3 = index
    if index == 0:
        scenario3_feedback3 = "You called 911. Help arrives, and lives are saved."
    elif index == 1:
        scenario3_feedback3 = "You left. Sadly, others were at risk without help."
    elif index == 2:
        scenario3_feedback3 = "Waiting made things worse — overdoses happened."
    pygame.time.set_timer(pygame.USEREVENT + 2, 2500)

start_button = Button("Start", WIDTH//2 - 100, HEIGHT//2 - 40, 200, 80, start_game)
scenario_buttons = [
    Button("Party Time", WIDTH//2 - 150, 150, 300, 60, scenario_1),
    Button("Festival", WIDTH//2 - 150, 250, 300, 60, scenario_2),
    Button("Exam Season", WIDTH//2 - 150, 350, 300, 60, scenario_3),
]


# Setting up the main loop
running = True  # Keeps running the game until you close it.
while running:  # This is the event loop
    screen.fill(WHITE)  # White background
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
            # Scenario 1
            elif current_screen == SCENARIO_1_SCREEN:
                for button in scenario1_buttons1:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SCENARIO_1_SCENE2:
                for button in scenario1_buttons2:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SCENARIO_1_SCENE3:
                for button in scenario1_buttons3:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SUMMARY_SCREEN:
                for button in summary_buttons:
                    if button.is_clicked(pos):
                        button.callback()
        # Scenario 2
            if current_screen == SCENARIO_2_SCREEN:
                for button in scenario2_buttons1:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SCENARIO_2_SCENE2:
                for button in scenario2_buttons2:
                    if button.is_clicked(pos):
                        button.callback()
        # Scenario 3
            if current_screen == SCENARIO_3_SCREEN:
                for button in scenario3_buttons1:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SCENARIO_3_SCENE2:
                for button in scenario3_buttons2:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SCENARIO_3_SCENE3:
                for button in scenario3_buttons3:
                    if button.is_clicked(pos):
                        button.callback()
            elif current_screen == SUMMARY_SCREEN:
                for button in summary_buttons:
                    if button.is_clicked(pos):
                        button.callback()





        elif event.type == pygame.USEREVENT + 1:
             # Advance scenes based on current screen
             if current_screen == SCENARIO_3_SCREEN:
                 current_screen = SCENARIO_3_SCENE2
             elif current_screen == SCENARIO_3_SCENE2:
                 current_screen = SCENARIO_3_SCENE3
             pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Stop timer

        elif event.type == pygame.USEREVENT + 2:  # Timer for Scene 3 to Summary Screen transition
            current_screen = SUMMARY_SCREEN  # Transition to Summary Screen
            pygame.time.set_timer(pygame.USEREVENT + 2, 0)  # Stop the timer after the transition

    
    # Timer event handling for feedback display
        if event.type == pygame.USEREVENT + 1:  # Timer for Scene 1 to Scene 2 transition
            if current_screen == SCENARIO_3_SCENE2:
                current_screen = SCENARIO_3_SCENE2  # Transition to Scene 2
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Stop the timer after the transition

        elif event.type == pygame.USEREVENT + 2:  # Timer for Scene 2 to Scene 3 transition
            if current_screen == SCENARIO_3_SCENE3:
                current_screen = SCENARIO_3_SCENE3  # Transition to Scene 3
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)  # Stop the timer after the transition

        # Timer event handling for Scenario 1
        elif event.type == pygame.USEREVENT + 3:  # Timer for Scene 1 to Scene 2 transition
            if current_screen == SCENARIO_1_SCREEN:
                current_screen = SCENARIO_1_SCENE2
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)  # Stop the timer

        elif event.type == pygame.USEREVENT + 4:  # Timer for Scene 2 to Scene 3 transition
            if current_screen == SCENARIO_1_SCENE2:
                current_screen = SCENARIO_1_SCENE3
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)  # Stop the timer
        
        elif event.type == pygame.USEREVENT + 5:
            if current_screen == SCENARIO_2_SCREEN:
                current_screen = SCENARIO_2_SCENE2
                pygame.time.set_timer(pygame.USEREVENT + 5, 0)

        elif event.type == pygame.USEREVENT + 2:
            if current_screen == SCENARIO_2_SCENE2:
                current_screen = SUMMARY_SCREEN
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)


        elif event.type == pygame.USEREVENT + 3:
            if current_screen == SCENARIO_1_SCREEN:
                current_screen = SCENARIO_1_SCENE2
            elif current_screen == SCENARIO_1_SCENE2:
                current_screen = SCENARIO_1_SCENE3
            elif current_screen == SCENARIO_1_SCENE3:
                current_screen = SUMMARY_SCREEN
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)


# Rendering section
    if current_screen == START_SCREEN:
        start_button.draw(screen)  # Draw start screen button
    elif current_screen == SCENARIO_SELECT:
        title_surf = small_font.render("Choose Your Scenario:", True, BLACK)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 50))
        screen.blit(title_surf, title_rect)
        for button in scenario_buttons:
            button.draw(screen)  # Draw scenario selection buttons
    elif current_screen == SUMMARY_SCREEN:
        draw_summary_screen()  # Render the Summary Screen

    # rendering scenario 1
    elif current_screen == SCENARIO_1_SCREEN:
        draw_wrapped_text(screen, scenario1_question1, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario1_buttons1:
            button.draw(screen)
        if scenario1_selected is not None:
            draw_wrapped_text(screen, scenario1_feedback, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SCENARIO_1_SCENE2:
        draw_wrapped_text(screen, scenario1_question2, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario1_buttons2:
            button.draw(screen)
        if scenario1_selected2 is not None:
            draw_wrapped_text(screen, scenario1_feedback2, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SCENARIO_1_SCENE3:
        draw_wrapped_text(screen, scenario1_question3, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario1_buttons3:
            button.draw(screen)
        if scenario1_selected3 is not None:
            draw_wrapped_text(screen, scenario1_feedback3, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SUMMARY_SCREEN:
        for button in summary_buttons:
            if button.is_clicked(pos):
                button.callback()
    
    # rendering scenario 2
    elif current_screen == SCENARIO_2_SCREEN:
        draw_wrapped_text(screen, scenario2_question1, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario2_buttons1:
            button.draw(screen)
        if scenario2_selected1 is not None:
            draw_wrapped_text(screen, scenario2_feedback1, 30, 400, small_font, BLACK, WIDTH - 60)

    elif current_screen == SCENARIO_2_SCENE2:
        draw_wrapped_text(screen, scenario2_question2, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario2_buttons2:
            button.draw(screen)
        if scenario2_selected2 is not None:
            draw_wrapped_text(screen, scenario2_feedback2, 30, 400, small_font, BLACK, WIDTH - 60)


   # rendering scenario 3
    elif current_screen == SCENARIO_3_SCREEN:
        draw_wrapped_text(screen, scenario3_question1, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario3_buttons1:
            button.draw(screen)  # Draw options for Scene 1
        if scenario3_selected is not None:
            draw_wrapped_text(screen, scenario3_feedback, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SCENARIO_3_SCENE2:
        # Scenario 3 Scene 2
        draw_wrapped_text(screen, scenario3_question2, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario3_buttons2:
            button.draw(screen)
        if scenario3_selected2 is not None:
            draw_wrapped_text(screen, scenario3_feedback2, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SCENARIO_3_SCENE3:
        # Scenario 3 Scene 3
        draw_wrapped_text(screen, scenario3_question3, 30, 30, small_font, BLACK, WIDTH - 60)
        for button in scenario3_buttons3:
            button.draw(screen)  # Draw options for Scene 3
        if scenario3_selected3 is not None:
            draw_wrapped_text(screen, scenario3_feedback3, 30, 400, small_font, BLACK, WIDTH - 60)
    elif current_screen == SUMMARY_SCREEN:
        for button in summary_buttons:
            if button.is_clicked(pos):
                button.callback()

    pygame.display.update()  # Update the display

pygame.quit()
sys.exit()
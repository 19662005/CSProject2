import pygame
import sys
import os

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scenario 2 Test")
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

# Timing
INTRO_DURATION = 2000  # milliseconds
CHOICE1_DURATION = 2000  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (50, 50, 50)

# Load images
def load_image(name):
    path = os.path.join("images", name)
    try:
        return pygame.image.load(path)
    except pygame.error:
        print(f"Error: Could not load image {path}")
        sys.exit()

scene_images = {
    "intro": load_image("scenario2beforescene1.png"),
    "scene1": load_image("scenario2duringchoicescene1.png"),
    "choice0": load_image("scenario2scene1choice1.png"),
    "choice1": load_image("scenario2scene1choice2.png"),
    "choice2": load_image("scenario2scene1choice3.png"),
    "progress": load_image("scenario2afterscene1choice.png"),
    "scene2": load_image("scenario2duringchoicescene2.png"),
    "final0": load_image("scenario2scene2choice1.png"),
    "final1": load_image("scenario2scene2choice2.png"),
    "final2": load_image("scenario2scene2choice3.png"),
}

# Screen states
INTRO = "intro"
SCENARIO_2_SCENE1 = "scenario2_scene1"
CHOICE1_RESULT = "choice1_result"
SCENARIO_2_SCENE2 = "scenario2_scene2"
SUMMARY_SCREEN = "summary"

current_screen = INTRO
pygame.time.set_timer(pygame.USEREVENT + 1, INTRO_DURATION)
choice1_result_start_time = None

# State tracking
scenario2_selected1 = None
scenario2_feedback1 = ""
scenario2_selected2 = None
scenario2_feedback2 = ""

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, LIGHT_BLUE, self.rect)
        pygame.draw.rect(surface, DARK_GRAY, self.rect, 2)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

# Text wrapper
def draw_wrapped_text(surface, text, x, y, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    for i, line in enumerate(lines):
        line_surf = font.render(line.strip(), True, color)
        surface.blit(line_surf, (x, y + i * font.get_linesize()))

# Scene 1
scenario2_question1 = "At a music festival, you're offered a pill. You refuse, but your friend takes it and starts acting weird. What do you do?"
scenario2_buttons1 = [
    Button("Let them walk it off", WIDTH//2 - 200, 400, 400, 50, lambda: scenario2_scene1_choice(0)),
    Button("Keep an eye on them", WIDTH//2 - 200, 460, 400, 50, lambda: scenario2_scene1_choice(1)),
    Button("Take it yourself", WIDTH//2 - 200, 520, 400, 50, lambda: scenario2_scene1_choice(2)),
]

def scenario2_scene1_choice(index):
    global scenario2_selected1, scenario2_feedback1, current_screen, choice1_result_start_time
    scenario2_selected1 = index
    if index == 0:
        scenario2_feedback1 = "Letting them walk it off is dangerous. They may not wake up."
    elif index == 1:
        scenario2_feedback1 = "Keeping an eye on them may save them."
    elif index == 2:
        scenario2_feedback1 = "Taking it too puts you both at risk."
    current_screen = CHOICE1_RESULT
    choice1_result_start_time = pygame.time.get_ticks()

# Scene 2
scenario2_question2 = "Your friend is unconscious and struggling to breathe. What do you do?"
scenario2_buttons2 = [
    Button("Call 911 and check their pulse", WIDTH//2 - 200, 400, 400, 50, lambda: scenario2_scene2_choice(0)),
    Button("Move them to a quiet place", WIDTH//2 - 200, 460, 400, 50, lambda: scenario2_scene2_choice(1)),
    Button("Wait for another friend", WIDTH//2 - 200, 520, 400, 50, lambda: scenario2_scene2_choice(2)),
]

def scenario2_scene2_choice(index):
    global scenario2_selected2, scenario2_feedback2, current_screen
    if scenario2_selected1 == 2:  # Took the pill
        scenario2_feedback2 = "You're too impaired to respond effectively."
        scenario2_selected2 = None
    else:
        scenario2_selected2 = index
        if index == 0:
            scenario2_feedback2 = "Great response. You might have saved your friend’s life."
        else:
            scenario2_feedback2 = "Delaying help could lead to death from overdose."
    current_screen = SUMMARY_SCREEN

# Draw scene with image
def draw_scene_with_image(image_key, question, buttons, feedback, selected):
    image = scene_images[image_key]
    screen.blit(pygame.transform.scale(image, (WIDTH, 200)), (0, 0))
    draw_wrapped_text(screen, question, 30, 220, small_font, BLACK, WIDTH - 60)
    if selected is None:
        for button in buttons:
            button.draw(screen)
    else:
        draw_wrapped_text(screen, feedback, 30, 300, small_font, BLACK, WIDTH - 60)

def draw_summary_screen():
    screen.fill(WHITE)
    if scenario2_selected1 == 2:  # Took the pill
        final_key = "final2"
    elif scenario2_selected2 is not None:
        final_key = f"final{scenario2_selected2}"
    else:
        final_key = "final2"
    screen.blit(pygame.transform.scale(scene_images[final_key], (WIDTH, HEIGHT)), (0, 0))
    draw_wrapped_text(screen, "Summary:\nYou've completed Scenario 2.", 30, 30, font, BLACK, WIDTH - 60)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT + 1 and current_screen == INTRO:
            current_screen = SCENARIO_2_SCENE1
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # turn off timer

        if current_screen == SCENARIO_2_SCENE1 and scenario2_selected1 is None:
            for button in scenario2_buttons1:
                button.handle_event(event)
        elif current_screen == SCENARIO_2_SCENE2 and scenario2_selected2 is None and scenario2_selected1 != 2:
            for button in scenario2_buttons2:
                button.handle_event(event)

    # Update screen logic
    if current_screen == INTRO:
        screen.blit(pygame.transform.scale(scene_images["intro"], (WIDTH, HEIGHT)), (0, 0))

    elif current_screen == SCENARIO_2_SCENE1:
        draw_scene_with_image("scene1", scenario2_question1, scenario2_buttons1, scenario2_feedback1, scenario2_selected1)

    elif current_screen == CHOICE1_RESULT:
        img_key = f"choice{scenario2_selected1}"
        screen.blit(pygame.transform.scale(scene_images[img_key], (WIDTH, HEIGHT)), (0, 0))
        if choice1_result_start_time is not None:
            elapsed = pygame.time.get_ticks() - choice1_result_start_time
            if elapsed >= CHOICE1_DURATION:
                current_screen = SCENARIO_2_SCENE2

    elif current_screen == SCENARIO_2_SCENE2:
        screen.blit(pygame.transform.scale(scene_images["progress"], (WIDTH, 200)), (0, 0))
        draw_scene_with_image("scene2", scenario2_question2, scenario2_buttons2, scenario2_feedback2, scenario2_selected2)

    elif current_screen == SUMMARY_SCREEN:
        draw_summary_screen()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

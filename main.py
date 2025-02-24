# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    global user_defined_coordinates
    global user_drawings
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
            if event.button == 1: # New point
                user_defined_coordinates.append(pygame.mouse.get_pos())
                print(user_defined_coordinates)
            elif event.button == 2: # Clear Board
                user_drawings = {}
                user_defined_coordinates = []
            elif event.button == 3: # New Picture
                if len(user_defined_coordinates) > 1:
                    user_drawings[len(user_drawings)] = user_defined_coordinates
                    user_defined_coordinates = []
                    print(user_drawings)

    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)

        if user_drawings: # Draw full pictures
            for image in user_drawings:
                if len(user_drawings[image]) == 2:
                    pygame.draw.line(screen, config.BLACK, user_drawings[image][0], user_drawings[image][1], 5)
                elif len(user_drawings[image]) > 2:
                    pygame.draw.polygon(screen, config.BLACK, user_drawings[image], 5)

        if user_defined_coordinates:
            for point in user_defined_coordinates:
                pygame.draw.circle(screen, config.RED, point, 5)
                
        pygame.display.flip()

        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

user_drawings = {}
user_defined_coordinates = []
if __name__ == '__main__':
    main()
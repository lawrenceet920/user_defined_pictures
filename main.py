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
    global fill
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit exc button
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Exit exc key
                return False
            elif event.key == pygame.K_BACKSPACE: # remove last point
                if user_defined_coordinates:
                    user_defined_coordinates.pop()
                elif user_drawings: # Remove last picture
                    del user_drawings[len(user_drawings) - 1]
            elif event.key == pygame.K_f:
                if fill:
                    fill = False
                else: 
                    fill = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # New point
                user_defined_coordinates.append(pygame.mouse.get_pos())
            elif event.button == 2: # Clear Board
                user_drawings = {}
                user_defined_coordinates = []
            elif event.button == 3: # New Picture
                if len(user_defined_coordinates) > 1:
                    if fill:
                        user_defined_coordinates.append(0)
                    else:
                        user_defined_coordinates.append(5)
                    user_drawings[len(user_drawings)] = user_defined_coordinates
                    user_defined_coordinates = []
                    print(user_drawings)

    return True
def main():
    color = [255, 0, 255]

    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)

        if user_drawings: # Draw full pictures
            if color_flow == True:
                color = find_color(color)
            for image in user_drawings:
                if len(user_drawings[image]) == 3:
                    pygame.draw.line(screen, color, user_drawings[image][0], user_drawings[image][1], 5)
                elif len(user_drawings[image]) > 3:
                    current_drawing = []
                    for point in user_drawings[image]:
                        if point != user_drawings[image][-1]:
                            current_drawing.append(point)
                    pygame.draw.polygon(screen, color, current_drawing, user_drawings[image][-1])

        if user_defined_coordinates:
            for point in user_defined_coordinates:
                pygame.draw.circle(screen, config.RED, point, 5)
                
        pygame.display.flip()
        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

def find_color(next_color):
    global color_direction

    if next_color[0] == 255 and color_direction[0] == 1:
        color_direction[0] = 0
        color_direction[1] = 1
        color_direction[2] = -1
    elif next_color[1] == 255 and color_direction[1] == 1:
        color_direction[0] = -1
        color_direction[1]= 0
        color_direction[2] = 1
    elif next_color[2] == 255 and color_direction[2] == 1:
        color_direction[0] = 1
        color_direction[1] = -1
        color_direction[2]= 0

    next_color = [next_color[0] + color_direction[0], next_color[1] + color_direction[1], next_color[2] + color_direction[2]]
    print(f'Color: {next_color}')
    return next_color

user_drawings = {}
user_defined_coordinates = []
fill = False
color_flow = True
color_direction = [1, 1, 1]
if __name__ == '__main__':
    main()
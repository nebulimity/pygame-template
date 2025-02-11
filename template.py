import pygame # Import the pygame library
import sys # Import the sys library

SCREEN_RESOLUTION = (800, 600) # Window resolution
FPS = 60 # Frames per second (how many times the window updtates per second)
WHITE = (255, 255, 255) # RGB color for white (we will use this as the background color)

pygame.init() # Initialize pygame

screen = pygame.display.set_mode((SCREEN_RESOLUTION[0], SCREEN_RESOLUTION[1])) # Create the window
pygame.display.set_caption("Pygame Template") # Set the window title

clock = pygame.time.Clock() # Create a clock object to control the frame rate

running = True # Variable to control the main loop of the game
while running:
    for event in pygame.event.get(): # Get all the events that have happened
        if event.type == pygame.QUIT:
            running = False # If the user closes the window, the game loop will end

    screen.fill(WHITE) # Fill the screen with the background color

    pygame.display.flip() # Update the screen
    clock.tick(FPS) # Control the frame rate

pygame.quit() # Quit pygame
sys.exit() # Quit the program
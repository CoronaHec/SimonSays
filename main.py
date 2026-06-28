import pygame
import random
import time
from button import Button

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GREEN_ON = (0, 255, 0)
GREEN_OFF = (0,227, 0)
RED_ON = (255, 0, 0)
RED_OFF = (227, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 227)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (227, 227, 0)

# Pass in respective sounds for each color
#GREEN_SOUND = pygame.mixer.Sound("bell1.mp3") # bell1
#RED_SOUND = pygame.mixer.Sound("bell1.mp3") # bell2
#BLUE_SOUND = pygame.mixer.Sound("bell1.mp3") # bell3
#YELLOW_SOUND = pygame.mixer.Sound("bell1.mp3") # bell4
GREEN_SOUND = None
BLUE_SOUND = None
RED_SOUND = None
YELLOW_SOUND = None


#Button Sprite Objects
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 10)
red = Button(RED_ON, RED_OFF, RED_SOUND, 260, 10)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 260, 260)
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 10, 260)

# Variables
colors = ["green", "red", "blue", "yellow"]
cpu_sequence = []
choice = ""

def draw_board():
    # Call the draw method on all four button objects
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)

def cpu_turn():
    choice = random.choice(colors) # pick a random color
    cpu_sequence.append(choice) # update cpu_sequence
    if choice == "green":
        green.update(SCREEN)
    # check other three color options
    elif choice == "red":
        red.update(SCREEN)
    elif choice == "blue":
        blue.update(SCREEN)
    elif choice == "yellow":
        yellow.update(SCREEN)

def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            else:
                yellow.update(SCREEN)
            pygame.time.wait(500)

def player_turn():
    turn_time = time.time()
    players_sequence = []
    while time.time() <= turn_time + 3 and len(players_sequence) < len(cpu_sequence):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #button click occured
                # Grab the current position of mouse here
                pos = pygame.mouse.get_pos()
                if green.selected(pos): #green button was selected
                    green.update(SCREEN) # illuminate button
                    players_sequence.append("green") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer

                # CHECK OTHER THREE OPTIONS

                if red.selected(pos): #green button was selected
                    red.update(SCREEN) # illuminate button
                    players_sequence.append("red") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer

                if blue.selected(pos): #green button was selected
                    blue.update(SCREEN) # illuminate button
                    players_sequence.append("blue") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer

                if yellow.selected(pos): #green button was selected
                    yellow.update(SCREEN) # illuminate button
                    players_sequence.append("yellow") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer
                    


    # If player does not select a button within 3 seconds then the game closes
    if not time.time() <= turn_time + 3:
        game_over()

def check_sequence(players_sequence):
    if players_sequence != cpu_sequence[:len(players_sequence)]:
        game_over()

def game_over():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
    pygame.display.update()

    draw_board() # draws buttons onto pygame screen
    repeat_cpu_sequence() # repeats cpu sequence if it's not empty
    cpu_turn() # cpu randomly chooses a new color
    player_turn() # player tried to recreate cpu sequence
    pygame.time.wait(1000) # waits one second before repeating cpu sequence

    clock.tick(60)
#this is the same as the two.py except we are changing the color between orange/blue when the user presses the space button

import pygame #importing the games package of python

pygame.init() #initializes all the modules required for pygame

screen = pygame.display.set_mode((400,300)) #launches a window of size 400, 300
done = False #initialize done to false
is_blue = True #initialize the blueness

while not done: #starting the event loop: which waits for user input and reacts to events(their actions)
    for event in pygame.event.get(): #foreach loop that gets the most recent event from the event queue(os keeps list of user events and this clears it and get the top of it)
        if event.type == pygame.QUIT: #checking if it is a quit event(top right X)
            done = True #stop the loop

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #if the user presses the space button K is an enum that covers most button presses on the keyboard
            is_blue = not is_blue #set is_blue to its inverse

    if is_blue: color = (0, 128, 255) #this checks if is_blue is true and sets the color value depending on if it is or not
    else: color = (255, 100, 0) #this is saying if it is not set to blue, set the color to orange
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60)) #draw a rectangle on surface screen(from line 7) with color either blue or orange and then define the dimensions of position
                                                                         #and size of the rectangle(x, y, width, height)  
    pygame.display.flip() #this is because python is double buffered which means in the background there is another window that handles ui changes and when it is ready it switches with the primary screen
                          #to reduce flicker, loading, etc.

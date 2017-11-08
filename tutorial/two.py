#this is the same as the one.py except we are drawing a rectangle

import pygame #importing the games package of python

pygame.init() #initializes all the modules required for pygame

screen = pygame.display.set_mode((400,300)) #launches a window of size 400, 300
done = False #initialize done to false

while not done: #starting the event loop: which waits for user input and reacts to events(their actions)
    for event in pygame.event.get(): #foreach loop that gets the most recent event from the event queue(os keeps list of user events and this clears it and get the top of it)
        if event.type == pygame.QUIT: #checking if it is a quit event(top right X)
            done = True #stop the loop
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60)) #draw a rectangle on surface screen(from line 7) with rgb values(0, 128, 255) which is blue and then define the dimensions of position
                                                                         #and size of the rectangle(x, y, width, height)  
    pygame.display.flip() #this is because python is double buffered which means in the background there is another window that handles ui changes and when it is ready it switches with the primary screen
                          #to reduce flicker, loading, etc.

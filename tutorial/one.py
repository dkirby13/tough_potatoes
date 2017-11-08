#this is just a skeleton program to show the concepts of pygame

import pygame #importing the games package of python

pygame.init() #initializes all the modules required for pygame

screen = pygame.display.set_mode((400,300)) #launches a window of size 400, 300
done = False #initialize done to false

while not done: #starting the event loop: which waits for user input and reacts to events(their actions)
    for event in pygame.event.get(): #foreach loop that gets the most recent event from the event queue(os keeps list of user events and this clears it and get the top of it)
        if event.type == pygame.QUIT: #checking if it is a quit event(top right X)
            done = True #stop the loop

    pygame.display.flip() #this is because python is double buffered which means in the background there is another window that handles ui changes and when it is ready it switches with the primary screen
                          #to reduce flicker, loading, etc.

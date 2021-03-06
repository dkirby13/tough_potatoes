#this is the same as the three.py except we making the square move with the arrow keys

import pygame #importing the games package of python

pygame.init() #initializes all the modules required for pygame

screen = pygame.display.set_mode((4000,3000)) #launches a window of size 4000, 3000
done = False #initialize done to false
is_blue = True #initialize the blueness
x = 30 #initialize the x and y position
y = 30


while not done: #starting the event loop: which waits for user input and reacts to events(their actions)
    for event in pygame.event.get(): #foreach loop that gets the most recent event from the event queue(os keeps list of user events and this clears it and get the top of it)
        if event.type == pygame.QUIT: #checking if it is a quit event(top right X)
            done = True #stop the loop

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #if the user presses the space button
            is_blue = not is_blue #set is_blue to its inverse

    pressed = pygame.key.get_pressed()   #this is a way to check if a key is currently being pushed down
    #note that in python decrease the value of y pushes it up on the screen on increasing it pushes it down
        
    if pressed[pygame.K_UP]: y-=30 
    if pressed[pygame.K_DOWN]: y+=30
    if pressed[pygame.K_LEFT]: x-=30
    if pressed[pygame.K_RIGHT]: x+=30

    if is_blue: color = (0, 128, 255) #this checks if is_blue is true and sets the color value depending on if it is or not
    else: color = (255, 100, 0) #this is saying if it is not set to blue, set the color to orange
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 30, 30)) #draw a rectangle on surface screen(from line 7) with color either blue or orange and then define the dimensions of position
                                                                         #and size of the rectangle(x, y, width, height)  
    pygame.display.flip() #this is because python is double buffered which means in the background there is another window that handles ui changes and when it is ready it switches with the primary screen
                          #to reduce flicker, loading, etc.

#this is the same as the four.py except instead of rectangle its an image thats moving around

import pygame #importing the games package of python
import os #importing the os package to let us access the image
_image_library = {} #initializing the image library

def get_image(path): #defining a function that takes in a path and returns the image at that path
    global _image_library #adding the _image_library to the scope of the function
    image = _image_library.get(path) #get the image
    if image == None: #if the image is not loaded already
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep) #this line is just to handle / in the file path with escape charachters
        print(canonicalized_path)
        image = pygame.image.load(canonicalized_path) # load the image
        image = pygame.transform.scale(image, (300, 300)) #changing the size 
        _image_library[path] = image #save the image to the image library
    return image #return the image

pygame.init() #initializes all the modules required for pygame

screen = pygame.display.set_mode((4000,3000)) #launches a window of size 400, 300
done = False #initialize done to false
x = 30 #initialize the x and y position
y = 30

clock = pygame.time.Clock() #initializing the clock to be used when standardizing framerate


while not done: #starting the event loop: which waits for user input and reacts to events(their actions)
    for event in pygame.event.get(): #foreach loop that gets the most recent event from the event queue(os keeps list of user events and this clears it and get the top of it)
        if event.type == pygame.QUIT: #checking if it is a quit event(top right X)
            done = True #stop the loop

    pressed = pygame.key.get_pressed()   #this is a way to check if a key is currently being pushed down
    #note that in python decrease the value of y pushes it up on the screen on increasing it pushes it down

    if pressed[pygame.K_UP]: y-=30
    if pressed[pygame.K_DOWN]: y+=30
    if pressed[pygame.K_LEFT]: x-=30
    if pressed[pygame.K_RIGHT]: x+=30

    screen.fill((255, 255, 255)) #reseting the screen to white
    
    screen.blit(get_image('images/connor_tard.png'), (x, y))
    
    pygame.display.flip() #this is because python is double buffered which means in the background there is another window that handles ui changes and when it is ready it switches with the primary screen
                          #to reduce flicker, loading, etc.
    clock.tick(60) #now the framerate is hardcoded to 60

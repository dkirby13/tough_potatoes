import pygame

#Global Constants

#Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.jump_count = 0
        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.x_speed = 0
        self.y_speed = 0
        self.r = 0;
        self.g = 100;
        self.b = 200;
        self.color = (self.r, self.g, self.b)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

       

# Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.x_speed = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.x_speed = 6
    
    def go_up(self):
        self.y_speed = -6
        
    def go_down(self):
        self.y_speed = 6
 
    def x_stop(self):
        """ Called when the user lets off the keyboard. """
        self.x_speed = 0

    def y_stop(self):
        self.y_speed = 0
    



    def shoot_right(self):
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, 10, 0, self.r, self.g, self.b)

    def shoot_left(self):
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, -10, 0, self.r, self.g, self.b)

    def shoot_up(self):
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, 0, -10, self.r, self.g, self.b)

    def shoot_down(self):
        bullet = Bullet(self.rect.x + self.width/2, self.rect.y + self.height/2, 0, 10, self.r, self.g, self.b)
        return bullet


    def update(self):
        """ Move the player. """
        # Gravity
        
 
        # Move left/right
        self.rect.x += self.x_speed

        self.rect.y += self.y_speed
        self.r+=1
        self.g+=2
        self.b+=3
        if self.r > 255: self.r = 0
        if self.g > 255: self.g = 0
        if self.b > 255: self.b = 0
        self.color = (self.r,self.g,self.b)
        self.image.fill(self.color)

     
       


    
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, x_speed, y_speed, r, g, b):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
      
        self.r = r
        self.g = g
        self.b = b
        self.color = (r, g, b)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
        self.r+=1
        self.g+=1
        self.b+=1
        if self.r > 255: self.r = 0
        if self.g > 255: self.g = 0
        if self.b > 255: self.b = 0
        self.color = (self.r,self.g,self.b)
        self.image.fill(self.color)

    

def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tough Potatoes")
    player = Player()
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
        
             
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_speed < 0:
                    player.x_stop()
                if event.key == pygame.K_RIGHT and player.x_speed > 0:
                    player.x_stop()
                if event.key == pygame.K_UP and player.y_speed < 0:
                    player.y_stop()
                if event.key == pygame.K_DOWN and player.y_speed > 0:
                    player.y_stop()
                    
        active_sprite_list.add(player.shoot_left())
        active_sprite_list.add(player.shoot_up())
        active_sprite_list.add(player.shoot_down())
        active_sprite_list.add(player.shoot_right())


       # screen.fill(BLACK)
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(100)
        
    pygame.quit()
main()

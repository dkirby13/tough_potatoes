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
        self.reloading = 0;
        self.reloading_count = 10;
        self.color = WHITE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

       

# Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.x_speed = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.x_speed = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.x_speed = 0

    def jump(self):
        if self.rect.y <= SCREEN_HEIGHT and self.jump_count < 2:
            self.y_speed = -10
            self.jump_count = self.jump_count + 1

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.y_speed == 0:
            self.y_speed = 1
        else:
            self.y_speed += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.y_speed >= 0:
            self.y_speed = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.jump_count = 0


    def shoot_right(self):
        if(self.reloading > 0):
            return
        self.reloading = self.reloading_count
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, 10, 0)

    def shoot_left(self):
        if(self.reloading > 0):
            return
        self.reloading = self.reloading_count
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, -10, 0)

    def shoot_up(self):
        if(self.reloading > 0):
            return
        self.reloading = self.reloading_count 
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, 0, -10)

    def shoot_down(self):
        if(self.reloading > 0):
            return
        self.reloading = self.reloading_count
        return Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2, 0, 10)


    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.x_speed

        self.rect.y += self.y_speed
        self.reloading = self.reloading - 1

     
       


    
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, x_speed, y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
      
      
        self.color = WHITE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
        

    

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
                if event.key == pygame.K_SPACE:
                    player.jump()
        
             
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_speed < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_speed > 0:
                    player.stop()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]: 
            a = player.shoot_left() 
            if a is not None: active_sprite_list.add(a)
        if pressed[pygame.K_w]: 
            a = player.shoot_up()
            if a is not None: active_sprite_list.add(a)
        if pressed[pygame.K_s]: 
            a = player.shoot_down()
            if a is not None: active_sprite_list.add(a)
        if pressed[pygame.K_d]: 
            a = player.shoot_right()
            if a is not None: active_sprite_list.add(a)


        screen.fill(BLACK)
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
main()

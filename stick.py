from config import *
class Stick:
    def __init__(self):
        stick_x =STICK_OFFSET
        stick_y =(SCREEN_HEIGHT - STICK_HEIGHT) // 2
        self.stick_speed_y =0
    def update(self):
        self.stick_y +=self.stick_speed_y
        if self.stick_y <=0:
            self.stick_y =0
        elif self.stick_y >= SCREEN_HEIGHT - STICK_HEIGHT:
            self.stick_y = SCREEN_HEIGHT - STICK_HEIGHT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.stick_y -= 15
        elif keys[pygame.K_DOWN]:
            self.stick_y += 15

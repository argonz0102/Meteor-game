import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((1400,700))
pygame.display.set_caption('Meteor game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
start_time = 0
game_active = False

player = pygame.Surface((50,50))

rect = player.get_rect()

rect.x = 50
rect.y = 600

player.fill('Red')



SQUARE_1 = pygame.Surface((50,50))

SQUARE_1.fill('Gold1')



rect1 = SQUARE_1.get_rect()

rect1.x = randint(0, 1350)
rect1.y = 0







player.fill('Red')



SQUARE_2 = pygame.Surface((50,50))
rect2 = SQUARE_2.get_rect()

rect2.x = randint(0, 1350)
rect2.y = -60
SQUARE_2.fill('green')

SQUARE_3 = pygame.Surface((50,50))
rect3 = SQUARE_3.get_rect()

rect3.x = randint(0, 1350)
rect3.y = -400
SQUARE_3.fill('Gold1')

SQUARE_4 = pygame.Surface((50,50))
rect4 = SQUARE_4.get_rect()

rect4.x = randint(0, 1350)
rect4.y = -220
SQUARE_4.fill('Gold1')

SQUARE_5 = pygame.Surface((50,50))
rect5 = SQUARE_5.get_rect()

rect5.x = randint(0, 1350)
rect5.y = -600
SQUARE_5.fill('Gold1')

SQUARE_6 = pygame.Surface((50,50))
rect6 = SQUARE_6.get_rect()

rect6.x = randint(0, 1350)
rect6.y = -320
SQUARE_6.fill('Gold1')



SQUARE_7 = pygame.Surface((50,50))
rect7 = SQUARE_7.get_rect()

rect7.x = randint(0, 1350)
rect7.y = 0
SQUARE_7.fill('Gold1')



Menu = test_font.render('Meteor game game', False, (64, 64, 64))

text2 = test_font.render('Press the arrow up button to start', False, (64, 64, 64))

Statue = pygame.Surface((300,300))
Statue.fill('Gold1')

level = "False"
score = 0
gg = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    if game_active == True:
    
        screen.fill((64,250,200))
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rect.x += 5
                if event.key == pygame.K_LEFT:
                    rect.x -= 5
        screen.blit(player, rect)
        if rect.x > 1350:
            rect.x = 1350

        if rect.x < 0:
            rect.x = 0
       

        

        
        if level == "False":

            
                

            

            if rect.colliderect(rect1):
                game_active = False
            
            rect1.y += 5

            if rect1.y == 680:
                rect1.y = -10
                rect1.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_1, rect1)

            if score == 3:
                level = "True"
                



        if level == "True":

            if rect.colliderect(rect2):
                game_active = False
            
            rect2.y += 5

            if rect2.y == 680:
                rect2.y = -10
                rect2.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_2, rect2)

            if rect.colliderect(rect1):
                game_active = False
            
            rect1.y += 5

            if rect1.y == 680:
                rect1.y = -10
                rect1.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_1, rect1)

            if score == 6:
                level = "siu"

        if level == "siu":
            if rect.colliderect(rect2):
                game_active = False
            
            rect2.y += 5

            if rect2.y == 680:
                rect2.y = -10
                rect2.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_2, rect2)

            if rect.colliderect(rect1):
                game_active = False
            
            rect1.y += 5

            if rect1.y == 680:
                rect1.y = -10
                rect1.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_1, rect1)

            if rect.colliderect(rect3):
                game_active = False
            
            rect3.y += 5

            if rect3.y == 680:
                rect3.y = -10
                rect3.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_3, rect3)

            if rect.colliderect(rect4):
                game_active = False
            
            rect4.y += 5

            if rect4.y == 680:
                rect4.y = -10
                rect4.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_4, rect4)

            if rect.colliderect(rect5):
                game_active = False
            
            rect5.y += 5

            if rect5.y == 680:
                rect5.y = -10
                rect5.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_5, rect5)

            if rect.colliderect(rect6):
                game_active = False
            
            rect6.y += 5

            if rect6.y == 680:
                rect6.y = -10
                rect6.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_6, rect6)

            if rect.colliderect(rect7):
                game_active = False
            
            rect7.y += 5

            if rect7.y == 680:
                rect7.y = -10
                rect7.x = randint(0, 1350)
                score += 1
            screen.blit(SQUARE_7, rect7)

    if game_active == False:
        
        screen.fill((64,250,200))
        screen.blit(Menu, (550, 100))
        screen.blit(text2, (430, 550))
        screen.blit(Statue, (525, 200))
        rect1.x = randint(0, 1350)
        rect1.y = 0
        rect.x = 50
        rect.y = 600
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game_active = True
        
        


    pygame.display.update()
    clock.tick(60)
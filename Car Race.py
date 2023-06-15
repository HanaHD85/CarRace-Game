import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 800

blue = (153, 204, 255)
light_red = (255, 128, 128)
dark_red  = (255, 0, 0)
light_green = (204, 255, 204)
black = (0,0,0)
yellow = (255, 255, 204)
dark_green = (0, 102, 0)
white = (255, 255, 255)


logoImg = pygame.image.load('logo.png')
starImg = pygame.image.load('star.png')
carImg = pygame.image.load('car.png')
car_width = 100
car_height = 100

crash_sound = pygame.mixer.Sound('lose.wav')
pygame.mixer.music.load('world.ogg')


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Race Car')
 
clock = pygame.time.Clock()


def button(msg,x,y,w,h , inac , ac , action = None):
    "inac = inactive color , ac = active color"
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()



    if x + w > mouse[0] > x and y + h > mouse[1]> y:
        pygame.draw.rect(gameDisplay , ac , (x , y , w , h ))
        if click[0] == 1 and action != None:
            if action ==  'Play':
                game_loop()

            elif action == 'Exit':
                quitgame()



        smallText = pygame.font.Font('freesansbold.ttf' , 80)
        TextSurf , TextRect = text_objects(msg , smallText  , black)
        TextRect.center = ((x + w/2 ), (y + h/2)) 
        gameDisplay.blit(TextSurf , TextRect)

    else : 
        pygame.draw.rect(gameDisplay , inac , (x , y , w , h ))
        smallText = pygame.font.Font('freesansbold.ttf' , 80)
        TextSurf , TextRect = text_objects(msg , smallText  , white)
        TextRect.center = ((x + w/2 ), (y + h/2)) 
        gameDisplay.blit(TextSurf , TextRect)

def score(count):
    font = pygame.font.SysFont(None , 50 , 0)
    text = font.render('score    : ' + str(count) , True , dark_green ,light_green)
    gameDisplay.blit(text , (0,0))

def quitgame():
    pygame.quit()
    quit()

def stuff(stuf_x , stuf_y , stuf_w , stuf_h , color):
    pygame.draw.rect(gameDisplay , color , [stuf_x , stuf_y ,stuf_w , stuf_h] )

def star(xs,ys):
    gameDisplay.blit(starImg , (xs,ys))

def logo(xl , yl):
    gameDisplay.blit(logoImg , (xl , yl))
def car(x,y):
    """displaying the photo"""
    gameDisplay.blit(carImg , (x,y))

def text_objects(text , font , color , frame = None):
    textSurface = font.render(text , True , color , frame)
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf' , 90)
    TextSurf , TextRect = text_objects(text , largeText , black , light_red)
    TextRect.center = (display_width/2 , display_height/2)
    gameDisplay.blit(TextSurf , TextRect)
    pygame.display.update()

    time.sleep(3)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.Font('freesansbold.ttf' , 120)
    TextSurf , TextRect = text_objects('You Crashed !!! ' , largeText , black , light_red)
    TextRect.center = (500,150)
    gameDisplay.blit(TextSurf , TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        button('Again' , 150 , 350 , 300 , 150  , dark_green , light_green , 'Play' )
        button('Exit' , 550 , 350 , 300 , 150 , dark_red , light_red , 'Exit')
        pygame.display.update()
    

def game_intro():
    intro = True

    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(blue)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("""Let's Play Game !!!""", largeText , black , light_red)
        TextRect.center = (500 , 200)
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("""-- Game By Hana.HD --""", largeText , black , light_red)
        TextRect.center = (500 , 600)
        gameDisplay.blit(TextSurf, TextRect)

        button('Play' , 150 , 350 , 300 , 150  , dark_green , light_green , 'Play' )
        button('Exit' , 550 , 350 , 300 , 150 , dark_red , light_red , 'Exit')
        logo(350 , 560)
        pygame.display.update()


def game_loop():

    pygame.mixer.music.play(-1)

    x =  display_width * 0.45
    y = display_height * 0.8 

    x_change = 0   # for moving left and right on x axix

    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -700
    stuff_speed = 15
    stuff_width =  100   #random.randrange(0 , (display_width/2 - car_width))
    stuff_height = 100
    counter = 0


    gameExit = False
 
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change            

        gameDisplay.fill(yellow)

        stuff(stuff_startx , stuff_starty , stuff_width , stuff_height , dark_red)
        stuff_starty += stuff_speed


        score(counter)
        star(95, 4)
        car(x,y)
        if x > display_width - car_width or x < 0:
            crash()
        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_width)
            counter += 1

            if counter % 5 == 0 :
                stuff_speed += 2


        if y <  stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
             crash()

        pygame.display.update()
        clock.tick(60) #    FPS

game_intro()
game_loop()
quitgame()

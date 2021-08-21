import pygame
import random
pygame.init()

pygame.mixer.init()



# screen width
screen_width = 800
screen_height= 600

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 55)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])


def welcome():
    pygame.mixer.music.load("backg.mp3")
    pygame.mixer.music.play()
    exit_game = False
    white = (255,255,255)
    black = (0,0,0)
    while not exit_game:
        gamewindow.fill(black)
        text_screen("Welcome to snake video game",(0,255,255),140,250)
        text_screen("Press Enter to Continue Game",(255,255,0),140,300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        pygame.display.update()
        pygame.time.Clock().tick(40)



def gameloop():
    pygame.mixer.music.pause()
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 180
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(100, screen_width-100)
    food_y = random.randint(50, screen_height-100)
    size = 20
    clock = pygame.time.Clock()
    fps = 30

    snk_list = []
    snk_length = 1

    with open('highscore.txt','r') as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))


            gamewindow.fill(black)
            text_screen("Game Over! Press Enter to continue",red,80,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y =0

                    if event.key == pygame.K_LEFT:
                        velocity_x =-10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x =0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x =0

            snake_y = snake_y + velocity_y
            snake_x = snake_x + velocity_x

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                pygame.mixer.music.load("eatsound.wav")
                pygame.mixer.music.play()
                score+=10
                food_x = random.randint(20, screen_width)
                food_y = random.randint(20, screen_height)
                snk_length+=5

                if score > int(highscore):
                    highscore = score

            gamewindow.fill(black)
            text_screen(f"Score:  {str(score)}            High Score: {str(highscore)}", red, 5, 5)
            pygame.draw.rect(gamewindow,green,[food_x,food_y,size,size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("eatsound.wav")
                pygame.mixer.music.play()
                game_over = True

            if head in snk_list[:-1]:
                pygame.mixer.music.load("eatsound.wav")
                pygame.mixer.music.play()
                game_over=True

            plot_snake(gamewindow,(100,0,100),snk_list,size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
import pygame, math
from random import randint
pygame.font.init()
pygame.init()

WIDTH = 10
WIN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
ICON = pygame.image.load("snake.png")
pygame.display.set_icon(ICON)

class spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(WIN,(255, 255, 255),(self.x*25,self.y*25,25,25))

grid = [[spot(i, j) for j in  range(32)] for i in range(32)]


snake = list()
snake.append(grid[2][8])
snake_speed = 15



def game():

    score = 0
    main_font = pygame.font.SysFont('comicsans', 50)
    food = grid[25][25]
    snake_dir = "R"
    ck = pygame.time.Clock()
    run = True
    

    while run:

        ck.tick(snake_speed)

        def gameover():

            nonlocal run
            gameover_label = main_font.render(f"GAMEOVER", 1, (255, 255, 255))
            WIN.blit(gameover_label, (330, 270))
            print("gameover")
            run = False


        def redraw():

            score_label = main_font.render(f"SCORE: {score}", 1, (255, 255, 255))
            WIN.fill((0,0,0))
            WIN.blit(score_label, (10, 10))
            food.draw()

            for i in snake:
                i.draw()
    
            pygame.display.update()

        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if keys[pygame.K_RIGHT] and snake_dir in ("U", "D"):
            snake_dir = "R"
        elif keys[pygame.K_LEFT] and snake_dir in ("U", "D"):
            snake_dir = "L"
        elif keys[pygame.K_DOWN] and snake_dir in ("R", "L"):
            snake_dir = "D"
        elif keys[pygame.K_UP] and snake_dir in ("R", "L"):
            snake_dir = "U"
        

        f = 0
        hx, hy = snake[0].x, snake[0].y

        if snake[0].x == food.x and snake[0].y == food.y:
            f_x = randint(0, 31)
            f_y = randint(0, 31)
            food = grid[f_x][f_y]
            snake.insert(0, grid[hx][hy])
            f = 1
            score+=1
        elif snake_dir == "R":
            if grid[(hx+1)%32][hy] not in snake:
                snake.insert(0, grid[(hx+1)%32][hy])
            else:
                gameover()
                break
        elif snake_dir == "L": 
            if grid[hx-1][hy] not in snake:
                snake.insert(0, grid[hx-1][hy])
            else:
                gameover()
                break
        elif snake_dir == "U": 
            if grid[hx][hy-1] not in snake:
                snake.insert(0, grid[hx][hy-1])
            else:
                gameover()
                break
        elif snake_dir == "D":
            if grid[hx][(hy+1)%32] not in snake:
                snake.insert(0, grid[hx][(hy+1)%32])
            else:
                gameover()
                break
        if not f:
            snake.pop()
        
        redraw()

game()
pygame.time.delay(3000)
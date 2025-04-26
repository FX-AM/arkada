import pygame
pygame.init()
window=pygame.display.set_mode((750,750))

window.fill((158, 213, 0))
clock=pygame.time.Clock()
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = color
        self.rect = pygame.Rect(x, y, width, height)
        
    def set_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image=pygame.image.load(filename)
    def draw(self):
        window.blit(self.image(self.x, self.y))
platform_x=200
platform_y=300
ball=Picture("tennis-ball-png-picture-1.png", 160, 200, 50, 50)
platform=Picture("wooden-podium-on-transparent-background-natural-stage-for-product-cosmetic-presentation-mock-up-pedestal-or-platform-for-beauty-products-empty-scene-display-showcase-3d-rendering-png.webp",platform_x,platform_y, 100, 30 )
#створення ворогів
start_x=5
start_y=5
count=4
monsters=[]
for i in range(10):
    y=start_y+(55*i)
    x=start_x+(25*i)
    for j in range(count):
        enemy=Picture("pngtree-video-video-game-retro-vector-png-image_34458072.png", 50, 50 )
        monsters.append(enemy)
        x=x+55
#        count=count-1
.

game=True
while game:
    window.fill((158, 213, 0))
#    platform.fill()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                platform.self_x+=3
            if event.key==pygame.K_LEFT:
                platform.self_x-=3

    for m in monsters:
        m.draw()
    platform.draw
    ball.draw
    ball_rect_x+=speed_x
    ball_rect_y+=speed_y
    if ball.rect_y<0
        speed_y*=-1
    if ball.rect_x<0 or ball.rect_x>750
    speed_x*=-1
    if ball.rect.collidepoint(platform.rect):
        speed_x*=-1
        speed_y*=-1
    clock.tick(40)
    pygame.display.update()
pygame.quit()
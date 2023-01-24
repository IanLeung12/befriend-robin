import pygame, time, math

pygame.init()
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Droid Sans Mono Regular", 26)
font2 = pygame.font.SysFont("Arpona", 68)

selectbutton = [0] * 2
for i in range(2):
    selectbutton[i] = pygame.image.load("Downloads\Creative Teaching\selectbutton" + str(i) + ".png")

BLACK     = (0, 0, 0)
RED       = (255, 0, 0)
GREEN     = (0, 255, 0)
BLUE      = (0, 0, 255)
LBLUE     = (130, 201, 240)
ORANGE    = (255, 127, 0)
CYAN      = (0, 183, 235)
MAGENTA   = (255, 0, 255)
PINK      = (249,161,188)
L_PINK    = (250, 218, 221)
YELLOW    = (255, 255, 0)
WHITE     = (255, 245,240)
clock = pygame.time.Clock()

pygame.mixer.music.load("Downloads\Creative Teaching\waltz.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)

class Circle:
    def __init__(self, x: float, y: int, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(gameWindow, PINK, (self.x, self.y), self.radius)

    def move(self):
        self.x -= 1
        self.y -= 1.5
        if self.x < -30:
            self.x += 1200
        if self.y < -30:
            self.y += 1000
def redrawCbutton(text: str, x, y):
    pos = pygame.mouse.get_pos()
    clicked = False
    imagehb = pygame.Rect(x, y, 150, 75)
    # if mouse is hovering over button
    if imagehb.collidepoint(pos):
        # button image is changed to secondary state
        buttonstate = 1
        mes = font.render(text, True, LBLUE)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
    else: 
        mes = font.render(text, True, BLACK)
        buttonstate = 0
    gameWindow.blit(selectbutton[buttonstate], (x, y))
    gameWindow.blit(mes, (x + 10, y + 10))
    # returns whether or not button is clicked
    return clicked

def redrawTbutton(image, x, y):
    # function to draw and create functionality of a button
    pos = pygame.mouse.get_pos()
    clicked = False
    imagehb = gameWindow.blit(image, (x, y))
    # if mouse is hovering over button
    if imagehb.collidepoint(pos):
        # button image is changed to secondary state
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
    # returns whether or not button is clicked
    return clicked

def moveto(startx, starty, endx, endy, time):
    movex = (endx - startx)/time
    movey = (endy - starty)/time
    return movex, movey
    
def pause():
    pygame.mixer.music.pause()
    pausemes = font2.render("PAUSED", True, BLACK)
    pausemes2 = font.render("PRESS SPACE TO UNPAUSE", True, BLACK)
    gameWindow.blit(pausemes, (25, 25))
    gameWindow.blit(pausemes2, (25, 75))
    inPause = True
    while inPause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inPause = False
        pygame.display.update()
        pygame.event.clear()
        clock.tick(60)
    pygame.mixer.music.unpause()

def drawtext(source, x, y):
    maintext = font.render(source, True, WHITE)
    bordertext = font.render(source, True, BLACK)
    gameWindow.blit(bordertext, (x + 1, y - 1))
    gameWindow.blit(bordertext, (x + 1, y + 1))
    gameWindow.blit(bordertext, (x - 1, y - 1))
    gameWindow.blit(bordertext, (x - 1, y + 1))
    gameWindow.blit(maintext, (x, y))



iangames = pygame.image.load("Downloads\Creative Teaching\\ian games.jpg").convert()
fade = 255

for i in range(240):
    gameWindow.fill(WHITE)
    iangames.set_alpha(fade)
    gameWindow.blit(iangames, (0, 0))
    clock.tick(60)
    if fade > 0:
        fade -= 1.15
    pygame.event.clear()
    pygame.display.update()

circles = []
for y in range(10):
    for x in range(12):
        if y % 2 == 0:
            x += 0.5
        circles.append(Circle(x*100, y*100, 30))

inTitle = True
messagetimer = 0
messagedisplay = True

logo = pygame.image.load("Downloads\Creative Teaching\logo.png")
robin = pygame.image.load("Downloads\Creative Teaching\Robin.png")
srobin = pygame.image.load("Downloads\Creative Teaching\sRobin.png")
robinx = 400
robiny = 700
circley = 1500
while inTitle:
    gameWindow.fill(WHITE)
    for circle in range(len(circles)):
        circles[circle].draw()
        circles[circle].move()
    gameWindow.blit(robin, (robinx, robiny))
    if robinx > 290:
        robinx -= 1.83
    if robiny > 110:
        robiny -= 9.83
    pygame.draw.circle(gameWindow, PINK, (400, circley), 800)
    pygame.draw.circle(gameWindow, L_PINK, (400, circley + 25), 800)
    if circley > 1250:
        circley -= 4
    message = font2.render("PRESS SPACE TO START", True, BLACK)
    messagerect = message.get_rect(center=(WIDTH/2, circley - 690))
    if messagedisplay:
        gameWindow.blit(message, messagerect)
    messagetimer += 1
    if messagetimer > 60:
        messagedisplay = not messagedisplay
        messagetimer = 0
    gameWindow.blit(logo, (30, 30))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inTitle = False
    pygame.display.update()
    pygame.event.clear()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.music.load("Downloads\Creative Teaching\Blue Boi.mp3")
pygame.mixer.music.play(loops=-1)
background1 = pygame.image.load("Downloads\Creative Teaching\\background1.png")
textbox = pygame.image.load("Downloads\Creative Teaching\\textbox.png")
inscene1 = True
quitbutton = pygame.image.load("Downloads\Creative Teaching\quit.png")
pausebutton = pygame.image.load("Downloads\Creative Teaching\pause.png")
scene1text = ["The birds are chirping, you feel ecstatic. Its your first day in high school!", "You stride forward, eager to make some new friends.", 
"Suddenly, you notice someone in a wheelchair trying to enter the school", "What do you do?", "null", "The bell rings and you head to your first class"]
textnum = 0
clicked = False
pygame.mixer.Sound("Downloads\Creative Teaching\\birds.wav").play()
srobinA = 0
srobin.set_alpha(srobinA)
while inscene1:
    gameWindow.blit(background1, (0,0))
    gameWindow.blit(textbox, (25, 375))
    if redrawTbutton(quitbutton, 575, 535):
        inscene1 = False
    elif redrawTbutton(pausebutton, 200, 535):
        pause()
    elif clicked:
        if textnum + 1 < len(scene1text) and textnum != 3:
            textnum += 1
            print(textnum)
            clicked = False
    if textnum != 3:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inscene1 = False
                elif event.key == pygame.K_LEFT:
                    if textnum > 0:
                        textnum -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
    else:
        if redrawCbutton("Ignore him", 300, 50):
            textnum += 1
            scene1text[4] = "You choose to ignore him. When you look back, hes no longer there."
        elif redrawCbutton("Offer help", 300, 175):
            textnum += 1
            scene1text[4] = "You offer him help. He politely declines, pointing out the door opening button."
    if 4 > textnum >= 2:
        if srobinA < 254:
            srobinA += 2
        srobin.set_alpha(srobinA)
        gameWindow.blit(srobin, (190, 290))
    else:
        srobinA = 0
    drawtext(scene1text[textnum], 100, 400)
    pygame.display.update()
    pygame.event.pump()
    clock.tick(60)

pygame.quit()
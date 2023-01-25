import pygame, time, math

pygame.init()
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Droid Sans Mono Regular", 26)
font2 = pygame.font.SysFont("Arpona", 68)
font3 = pygame.font.SysFont("Elephant", 36)

selectbutton = [0] * 2
for i in range(2):
    selectbutton[i] = pygame.image.load("selectbutton" + str(i) + ".png")

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

pygame.mixer.music.load("waltz.mp3")
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
    pygame.event.pump()
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

def drawtext2(source, x, y):
    maintext = font2.render(source, True, BLACK)
    bordertext = font2.render(source, True, WHITE)
    gameWindow.blit(bordertext, (x + 2, y - 2))
    gameWindow.blit(bordertext, (x + 2, y + 2))
    gameWindow.blit(bordertext, (x - 2, y - 2))
    gameWindow.blit(bordertext, (x - 2, y + 2))
    gameWindow.blit(maintext, (x, y))

def drawtext3(source, x, y):
    maintext = font3.render(source, True, WHITE)
    bordertext = font3.render(source, True, BLACK)
    gameWindow.blit(bordertext, (x + 1, y - 1))
    gameWindow.blit(bordertext, (x + 1, y + 1))
    gameWindow.blit(bordertext, (x - 1, y - 1))
    gameWindow.blit(bordertext, (x - 1, y + 1))
    gameWindow.blit(maintext, (x, y))

iangames = pygame.image.load("ian games.jpg").convert()
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

logo = pygame.image.load("logo.png")
robin = pygame.image.load("Robin.png")
srobin = pygame.image.load("sRobin.png")
nametag = pygame.image.load("nametag.png")
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

done = False
username = ""
usermessage = font2.render("PLEASE ENTER YOUR NAME:", True, WHITE)

while not done:
    gameWindow.fill(BLACK)
    for circle in range(len(circles)):
        circles[circle].draw()
        circles[circle].move()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done = True
            elif event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode
    userrect = usermessage.get_rect(center=(WIDTH/2, 100))
    usermessage2 = font2.render(username, True, WHITE)
    userrect2 = usermessage2.get_rect(center=(WIDTH/2, 200))
    drawtext2("PLEASE ENTER YOUR NAME:", userrect.x, userrect.y)
    drawtext2(username, userrect2.x, userrect2.y)
    pygame.event.pump()
    pygame.display.update()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.music.load("Blue Boi.mp3")
pygame.mixer.music.play(loops=-1)
background1 = pygame.image.load("background1.png")
textbox = pygame.image.load("textbox.png")
inscene1 = True
inscene2 = True
inscene3 = True
inend = True
quitbutton = pygame.image.load("quit.png")
pausebutton = pygame.image.load("pause.png")
backbutton = pygame.image.load("back.png")
scene1text = ["The birds are chirping, you feel ecstatic. Its your first day in high school!", "You stride forward, eager to make some new friends.", 
"Suddenly, you notice someone in a wheelchair trying to enter the school", "What do you do?", "null", "The bell rings and you head to your first class", "null"]
textnum = 0
clicked = False
pygame.mixer.Sound("birds.wav").play()
srobinA = 0
srobin.set_alpha(srobinA)
helped = False
while inscene1:
    gameWindow.blit(background1, (0,0))
    gameWindow.blit(textbox, (25, 375))
    if redrawTbutton(quitbutton, 575, 535):
        inscene1 = False
        inscene2 = False
        inscene3 = False
        inend = False
    elif redrawTbutton(pausebutton, 200, 535):
        pause()
    elif redrawTbutton(backbutton, 400, 535) and textnum > 0:
        textnum -= 1 
    elif clicked and textnum != 3:
        if textnum + 1 < len(scene1text) and textnum != 3:
            textnum += 1
            print(textnum)
            clicked = False
    if textnum != 3:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inscene1 = False
                    inscene2 = False
                    inscene3 = False
                    inend = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
    else:
        if redrawCbutton("Ignore him", 300, 150):
            textnum += 1
            scene1text[4] = "You choose to ignore him. When you look back, hes no longer there."
            helped = False
        elif redrawCbutton("Offer help", 300, 275):
            textnum += 1
            scene1text[4] = "You offer him help. He politely declines, pointing out the door opening button."
            helped = True
    if 4 > textnum >= 2:
        if srobinA < 250:
            srobinA += 3
        srobin.set_alpha(srobinA)
        gameWindow.blit(srobin, (190, 290))
    else:
        srobinA = 0
    drawtext(scene1text[textnum], 90, 400)
    pygame.display.update()
    pygame.event.pump()
    clock.tick(60)
    if textnum == 6:
        inscene1 = False

background2 = pygame.image.load("background2.png")
bg2A = 0
background2.set_alpha(bg2A)
pygame.mixer.music.stop()
pygame.mixer.music.load("postmeridie.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.Sound("bell.mp3").play()
textnum = 0
robinx = 900
scene2text = ["As you take your seat, you find yourself sitting beside the person from earlier.", "null", "null", "null", 
"The conversation ends as the teacher begins talking.", "When the period nears its end, Robin taps your shoulder.", "Hey, wanna eat lunch together?", 
"Hey, wanna eat lunch together?", "You willingly accept his offer.", "null"]
if helped:
    scene2text[1] = "Hey, I'm Robin. I didn't get to thank you earlier, so... Thank You"
    scene2text[2] = "Hey, I'm Robin. I didn't get to thank you earlier, so... Thank You"
else:
    scene2text[1] = "Hey, I'm Robin, I hope we can make good friends this year"
    scene2text[2] = "Hey, I'm Robin. I hope we can make good friends this year"
wdydchoice = 0
while inscene2:
    gameWindow.fill(BLACK)
    gameWindow.blit(background2, (0, 0))
    background2.set_alpha(bg2A)
    if bg2A < 254:
        bg2A += 1
    else:
        if 1 <= textnum < 4 or 6 <= textnum:
            gameWindow.blit(nametag, (125, 328))
            drawtext3("Robin", 135, 340)
            if robinx > 330:
                robinx -= 10
        else:
            if robinx < 900:
                robinx += 20
        gameWindow.blit(robin, (robinx, 150))
        gameWindow.blit(textbox, (25, 375))
        drawtext(scene2text[textnum], 90, 400)
        if redrawTbutton(quitbutton, 575, 535):
            inscene2 = False
            inscene3 = False
            inend = False
        elif redrawTbutton(pausebutton, 200, 535):
            pause()
        elif redrawTbutton(backbutton, 370, 535) and textnum > 0:
            textnum -= 1 
        elif clicked:
            if textnum + 1 < len(scene2text):
                textnum += 1
                print(textnum)
                clicked = False
        wdydmes = font2.render("How do you respond?", True, BLACK)
        wdydrect = wdydmes.get_rect(center=(WIDTH/2, 100))
        if textnum != 2 and textnum != 7:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inscene2 = False
                        inscene3 = False
                        inend = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
        elif textnum == 2:
            drawtext2("How do you respond", wdydrect.x, wdydrect.y)
            if redrawCbutton("Don't talk to me", 200, 150):
                wdydchoice = 1
                scene2text[3] = "Learn some manners bro."
                textnum += 1
                scene2text[8] = "You reluctantly agree, giving him your name on the way."
            elif redrawCbutton("Introduce", 450, 150):
                wdydchoice = 2
                scene2text[3] = username + " huh, thats a nice name."
                textnum += 1
                scene2text[8] = "You willingly accept his offer."
            elif redrawCbutton("Wheelchair?", 200, 275):
                wdydchoice  = 3
                scene2text[3] = "I don't want to talk about it right now."
                textnum += 1
                scene2text[8] = "You reluctantly agree, giving him your name on the way."
            elif redrawCbutton("Compliment", 450, 275):
                wdydchoice = 4
                scene2text[3] = "Thanks, but a wheelchair doesn't make me any less of a person."
                textnum += 1
                scene2text[8] = "You reluctantly agree, giving him your name on the way."
        elif textnum == 7:
            if redrawCbutton("Yes", 300, 100) or redrawCbutton("Yes", 300, 250):
                textnum += 1
        if textnum == 9:
            inscene2 = False
    pygame.display.update()
    pygame.event.pump()
    clock.tick(60)
scene3text = ["The second period ends and you head to your agreed upon meeting spot", "You are surprised to see he is already there waiting for you",
"Hey " + username + ", wassup?", "Hey " + username + ", wassup?", "null", "What courses do you have?","What courses do you have?", "Aw that sucks, we're only together period 1", 
"Aw that sucks, we're only together period 1", "Welp, lunch is almost over. See you tommorow " + username + "!",  "Welp, lunch is almost over. See you tommorow " + username + "!",
"null", "null", "You chuckle, glad that you made your first high school friend.", "null"]
background3 = pygame.image.load("background3.png")
bg3A = 0
background3.set_alpha(bg3A)
pygame.mixer.music.stop()
pygame.mixer.music.load("Subwoofer Lullaby.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.Sound("bell.mp3").play()
bg4 = pygame.image.load("background4.png")
bg4A = 0
bg4part1 = True
textnum = 0
robinx = 900
while inscene3:
    gameWindow.fill(BLACK)
    gameWindow.blit(background3, (0, 0))
    background3.set_alpha(bg3A)
    bg4.set_alpha(bg4A)
    if bg3A < 254:
        bg3A += 1
    else:
        if textnum == 8:
            if bg4A < 254:
                bg4A += 2
            else:
                textnum += 1
        if textnum == 9:
            if bg4A > 253:
                bg4A -= 0.02
            elif bg4A > 0:
                bg4A -= 1
        if 2 <= textnum < 11 or textnum == 12:
            gameWindow.blit(nametag, (125, 328))
            drawtext3("Robin", 135, 340)
            if robinx > 330:
                robinx -= 10
        else:
            if robinx < 900:
                robinx += 20
        gameWindow.blit(robin, (robinx, 150))
        gameWindow.blit(textbox, (25, 375))
        drawtext(scene3text[textnum], 90, 400)
        if redrawTbutton(quitbutton, 575, 535):
            inscene3 = False
            inend = False
        elif redrawTbutton(pausebutton, 200, 535):
            pause()
        elif redrawTbutton(backbutton, 370, 535) and textnum > 0:
            textnum -= 1 
        elif clicked:
            if textnum + 1 < len(scene3text):
                textnum += 1
                print(textnum)
                clicked = False
        if textnum != 3 and textnum != 6 and textnum != 8 and textnum != 10:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inscene3 = False
                        inend = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
        elif textnum == 3:
            if redrawCbutton("I'm good", 200, 150):
                scene3text[4] = "Great! Same here."
                textnum += 1
            elif redrawCbutton("I'm bad", 450,150):
                scene3text[4] = "Same, I miss summer break"
                textnum += 1
            elif redrawCbutton("Bully", 300, 275):
                scene3text[4] = "Lol. Stop joking, I know you came here 'cause you like me."
                textnum += 1
        elif textnum == 6:
            if redrawCbutton("Tell him", 300, 250):
                textnum += 1
        elif textnum == 10:
            if redrawCbutton("See ya!", 200, 150):
                scene3text[11] = "YOU: See you tommorow my friend!"
                scene3text[12] = "Haha, see ya buddy."
                textnum += 1
            elif redrawCbutton("~Shy~", 450, 150):
                scene3text[11] = "YOU: Okay. I-It's not like we're friends or anything though!"
                scene3text[12] = "Haha, sure buddy."
                textnum += 1
            elif redrawCbutton("Say doubts", 200, 275):
                scene3text[11] = "YOU: Haha, I didn't know a disabled person could be so fun, but cya!"
                scene3text[12] = "That's really rude buddy. I'll talk with you tommorow."
                textnum += 1
            elif redrawCbutton("Help him", 450, 275):
                scene3text[11] = "YOU: Here, I'll push you to your next class."
                scene3text[12] = "STOP! Don't help me without asking first."
                textnum += 1
        if textnum == 14:
            inscene3 = False
    gameWindow.blit(bg4, (0,0))
    pygame.display.update()
    pygame.event.pump()
    clock.tick(60)
endbg = pygame.image.load("endbg.png")
pygame.mixer.music.stop()
pygame.mixer.music.load("His theme.mp3")
pygame.mixer.music.play(loops=-1)
while inend:
    gameWindow.blit(endbg, (0,0))
    if redrawTbutton(quitbutton, 150, 535):
        inend = False
    pygame.display.update()
    pygame.event.pump()
    clock.tick(60)
pygame.quit()
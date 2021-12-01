import random

HEIGHT = 708
WIDTH = 390

gravity = 0.4
roof = Actor("blackline", (200, 0))
bird = Actor("fat.png", (200, 350))
grass = Actor("grass", (200, 670))
pipet = Actor("top", anchor=("left", "bottom"))
pipeb = Actor("bottom", anchor=("left", "top"))
restart = Actor("1x-restart", (200, 600))
backround = Actor("background", (200,300))
bird.fall = 2
speed = 3.5
gap = 350
bird.score = 0
bird.dead = False

def draw():
    screen.clear()
    backround.draw()
    bird.draw()
    pipet.draw()
    pipeb.draw()
    grass.draw()
    roof.draw()
    if bird.dead == True:
        screen.fill((255, 255, 255))
        restart.draw()
        screen.draw.text(
            "Game Over",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=50,
            fontname="amatic",
            color="black",
        )

    screen.draw.text(
            "Score: "+str(bird.score),
            center=(200,100),
            fontsize=50,
            fontname="amatic",
            color="black",
        )


def update():
    print(bird.pos)
    bird_fall()
    global speed, pos
    pipet.left -= speed
    pipeb.left -= speed

    if pipet.right < 0:
        pipe_gaps()
        if not bird.dead:
            bird.score+=1

    if bird.colliderect(pipet) or bird.colliderect(pipeb):
        bird.image = "birddead"
        bird.dead = True


    print(bird.score)

    if bird.colliderect(grass):
        bird.image = "birddead"
        bird.dead = True
        sounds.die.play()

    if bird.y == (200, 708):
        bird.y = (200, 708)
    if bird.pos < (200, 0):
        bird.pos = (200, 0)

def pipe_gaps():
    global gap
    pipegap = random.randint(200, HEIGHT - 200)
    pipet.pos = (WIDTH, pipegap - gap // 2)
    pipeb.pos = (WIDTH, pipegap + gap // 2)

def bird_fall():
    bird.fall += gravity
    bird.y += bird.fall

def notdie():
    bird.dead = False
def on_key_down():
    if not bird.dead:
        bird.fall = -6.5
        bird.image = "fatdown"
        sounds.wing.play()
        gap = 300


def on_mouse_down(pos):
        if restart.collidepoint(pos):
            print("Hit Restart")
            bird.dead = False
            bird.pos = (200, 350)
            bird.fall = 0
            bird.score = 0
        if backround.collidepoint(pos):
            bird.fall = -7
            bird.image = "fat"
            sounds.wing.play()

def on_key_up():
    bird.image = "fat"


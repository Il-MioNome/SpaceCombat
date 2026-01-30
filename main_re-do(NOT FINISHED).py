from pgzero_api_stub import *
import pgzrun
import random
import time

aliens = []

WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = f"Space Combat Re-Do v1.0.0 (Set to {FPS} FPS)"

## START RIPOSIZIONA ALIENS FUNCTION ##

def riposiziona_aliens():
    for alien in aliens:
        for i, alien in enumerate(aliens):
            if i == 0:
                alien.y = random.randint(-60, -20)
                alien.x = random.randint(30, 770)
            elif i == 1:
                alien.y = random.randint(-100, -60)
                alien.x = random.randint(30, 770)
            elif i == 2:
                alien.y = random.randint(-140, -100)
                alien.x = random.randint(30, 770)
            elif i == 3:
                alien.y = random.randint(-180, -140)
                alien.x = random.randint(30, 770)
            if i == 4:
                alien.y = random.randint(-220, -180)
                alien.x = random.randint(30, 770)
            if i == 5:
                alien.y = random.randint(-260, -220)
                alien.x = random.randint(30, 770)
   
## END RIPOSIZIONA ALIENS FUNCTION ##

#---------------------------------------------

## START ACTORS INITIALIZATION ##             

background = Actor("bg", (400,300))
player = Actor("spacecraft", (400,540))
bad_alien = Actor("nemico_test", (400,450))
command_illustration = Actor("keyboard_test", (400,300))
thought_bubble = Actor("penso_medio", (245,500))
for i in range(5):
    alien = Actor("nemico", riposiziona_aliens())
    aliens.append(alien)
    
## END ACTORS INITIALIZATION ##

#---------------------------------------------

## START GAME VARIABLES INITIALIZATION ##

score = 0
bigger_score = 0
life = 3
GameOver = False
collision = False
level = 1
playing = True
game_pause = False
first_run = True
wait_sec = time.time()
aliens_spawned = False

## END GAME VARIABLES INITIALIZATION ##

def draw():
    global GameOver, playing, life, score, playing, bigger_score, game_pause
    
    background.draw()
    for alien in aliens:
        alien.draw()
    player.draw()
    
    if GameOver and not playing and not game_pause:
        background.draw()
        screen.draw.text("GAME OVER", (18, 260), color = "red", fontsize = 180)
        bad_alien.draw()
        thought_bubble.draw()
        screen.draw.text("Loser!", (225, 480), color = "green", fontsize = 20)
        screen.draw.text("Press 'ENTER/RETURN'", (175, 500), color = "green", fontsize = 20)
        screen.draw.text("to try again", (175, 520), color = "green", fontsize = 20)
        screen.draw.text(f"Max score: {bigger_score}", (325, 190), color = "green", fontsize = 40)
        
    screen.draw.text(f"Life: {life}", (10, 10), color="green", fontsize=40)
    screen.draw.text(f"Score: {score}", (10, 40), color="green", fontsize=40)
    screen.draw.text(f"Level: {level}", (10, 70), color="green", fontsize=40)
    screen.draw.text(f"Max score: {bigger_score}", (10, 100), color="green", fontsize=40)
    
    if game_pause and not playing and not GameOver:
        background.draw()
        screen.draw.text("Game Paused", (220,260), color="red", fontsize=100)
        screen.draw.text("Press 'ENTER/RETURN' to resume", (200, 320), color="green", fontsize=35)
    
    if not playing and not game_pause and not GameOver:
        background.draw()
        command_illustration.draw()
        screen.draw.text("Click 'RETURN/ENTER' when you're ready", (275, 443), color="green", fontsize=35)
    
    
def update(dt):
    global score, life, bigger_score, GameOver, collision, level, game_pause, playing, riposiziona_aliens, first_run, wait_sec, aliens_spawned
    
    ## START PLAYER MOVEMENT ##
    
    if (keyboard.left or keyboard.a) and player.x > 30:
        if level == 1:
            player.x -= 5
        elif level == 2:
            player.x -= 6
        elif level == 3:
            player.x -= 8
        elif level == 4:
            player.x -= 10
        elif level == 5:
            player.x -= 12
            
    elif (keyboard.right or keyboard.d) and player.x < 770:
        if level == 1:
            player.x += 5
        elif level == 2:
            player.x += 6
        elif level == 3:
            player.x += 8
        elif level == 4:
            player.x += 10
        elif level == 5:
            player.x += 12

    elif (keyboard.up or keyboard.w) and player.y > 250:
        if level == 1:
            player.y = player.y - 5
        elif level == 2:
            player.y = player.y - 6
        elif level == 3:
            player.y = player.y - 8
        elif level == 4:
            player.y = player.y - 10
        elif level == 5:
            player.y = player.y - 12

    
    elif (keyboard.down or keyboard.s) and player.y < 570:
        if level == 1:
            player.y = player.y + 5
        elif level == 2:
            player.y = player.y + 6
        elif level == 3:
            player.y = player.y + 8
        elif level == 4:
            player.y = player.y + 10
        elif level == 5:
            player.y = player.y + 12    
    
    ## END PLAYER MOVEMENT ##
    
    #--------------------------------------------
    
    ## START ALIENS MOVEMENT ##
    if not first_run:
        for alien in aliens:
            if alien.y > 650:
                for alien in [0,1,2,3,4]:
                    riposiziona_aliens()
                else:
                    score += 1
            else:
                if level == 1:
                    alien.y += 2
                elif level == 2:
                    alien.y += 5
                elif level == 3:
                    alien.y += 8
                elif level == 4:
                    alien.y += 11
                elif level == 5:
                    alien.y += 14
    elif time.time() - wait_sec > 3:
        first_run = False

    ## FINISH ALIENS MOVEMENT ##
    
pgzrun.go()

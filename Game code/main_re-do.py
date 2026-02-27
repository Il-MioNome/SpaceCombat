from pgzero_api_stub import *
import pgzrun
import random
import time

aliens = []

WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = f"Space Combat Re-Do v1.0.0 (Set to {FPS} FPS)"

## START CREATE ALIENS ACTOR FUNCTION ##

for i in range(6):
    alien = Actor("nemico")
    aliens.append(alien)
    
## FINISH CREATE ALIENS ACTOR FUNCTION ##

#---------------------------------------------

## START RIPOSIZIONA ALIENS FUNCTION ##

def riposiziona_aliens(i):
    if i == 0:
        aliens[i].y = random.randint(-80, -40)
        aliens[i].x = random.randint(30, 770)
    if i == 1:
        aliens[i].y = random.randint(-120, -80)
        aliens[i].x = random.randint(30, 770)
    if i == 2:
        aliens[i].y = random.randint(-160, -120)
        aliens[i].x = random.randint(30, 770)
    if i == 3:
        aliens[i].y = random.randint(-200, -160)
        aliens[i].x = random.randint(30, 770)
    if i == 4:
        aliens[i].y = random.randint(-240, -200)
        aliens[i].x = random.randint(30, 770)
    if i == 5:
        aliens[i].y = random.randint(-280, -240)
        aliens[i].x = random.randint(30, 770)
   
## END RIPOSIZIONA ALIENS FUNCTION ##

#---------------------------------------------

## START ACTORS INITIALIZATION ##             

background = Actor("bg", (400,300))
player = Actor("spacecraft", (400,540))
bad_alien = Actor("nemico_test", (400,450))
command_illustration = Actor("keyboard_new", (400,300))
thought_bubble = Actor("penso_medio", (245,500))
for i in range(len(aliens)):
    riposiziona_aliens(i)
    
## END ACTORS INITIALIZATION ##

#---------------------------------------------

## START GAME VARIABLES INITIALIZATION ##

score = 0
bigger_score = 0
life = 3
GameOver = False
collision = False
level = 1
playing = False
game_pause = False
first_run = False
wait_sec = 0
aliens_spawned = False
wait_sec_displayed = 0
command_illustration_variable = True
new_score_announcement = False
same_score_announcement = False
scored_less_announcement = False

## END GAME VARIABLES INITIALIZATION ##

def draw():
    global GameOver, playing, life, score, playing, bigger_score, game_pause, wait_sec_displayed, first_run, command_illustration_variable, new_score_announcement, same_score_announcement, scored_less_announcement
    
    ## START DRAW BG, ALIENS AND PLAYER
    
    background.draw()
    for alien in aliens:
        alien.draw()
    player.draw()
    
    ## END DRAW BG, ALIENS AND PLAYER
    
    #---------------------------------------------
    
    ## START COUNTDOWN AT START
    
    if first_run:
        if wait_sec_displayed == 1:
            screen.draw.text("3", centerx=WIDTH/2, top=240, color = "green", fontsize = 180)
        elif wait_sec_displayed == 2:
            screen.draw.text("2", centerx=WIDTH/2, top=240, color = "green", fontsize = 180)
        elif wait_sec_displayed == 3:
            screen.draw.text("1", centerx=WIDTH/2, top=240, color = "green", fontsize = 180)
        elif wait_sec_displayed == 4:
            screen.draw.text("START", centerx=WIDTH/2, top=240, color = "green", fontsize = 180)
    
    ## END COUNTDOWN AT START
    
    #---------------------------------------------
    
    ## START GAME OVER SCREEN
    
    if GameOver:
        background.draw()
        screen.draw.text("GAME OVER", centerx=WIDTH/2, top=260, color = "red", fontsize = 180)
        bad_alien.draw()
        thought_bubble.draw()
        screen.draw.text("KEEP GOING!", (190, 485), color = "green", fontsize = 24)
        screen.draw.text("Press 'ENTER'", (190, 505), color = "green", fontsize = 24)
        screen.draw.text("to try again", (200, 525), color = "green", fontsize = 24)
        if new_score_announcement:
            screen.draw.text(f"NEW HIGH SCORE! ({bigger_score})", centerx=WIDTH/2, top=190, color = "gold", fontsize = 54)
        elif same_score_announcement:
            if bigger_score > 0:
                screen.draw.text(f"Personal record matched! ({bigger_score})", centerx=WIDTH/2, top=190, color = "lime", fontsize = 48)
            elif bigger_score == 0:
                screen.draw.text(f"CAN DO BETTER! KEEP GOING! ({bigger_score})", centerx=WIDTH/2, top=190, color = "lime", fontsize = 48)
        elif scored_less_announcement:
            screen.draw.text(f"Below your best: ({bigger_score}) (KEEP GOING!)", centerx=WIDTH/2, top=190, color = "green", fontsize = 48)
        
    ## END GAME OVER SCREEN
    
    #---------------------------------------------
    
    ## START LIFE, SCORE, LEVEL, MAX SCORE DRAW
    
    screen.draw.text(f"Life: {life}", (10, 10), color="green", fontsize=40)
    screen.draw.text(f"Score: {score}", (10, 40), color="green", fontsize=40)
    screen.draw.text(f"Level: {level}", (10, 70), color="green", fontsize=40)
    screen.draw.text(f"Max score: {bigger_score}", (10, 100), color="green", fontsize=40)
    
    ## END LIFE, SCORE, LEVEL, MAX SCORE DRAW
    
    #---------------------------------------------
    
    ## START GAME PAUSE SCREEN
    
    if game_pause:
        screen.draw.text("Game Paused", centerx=WIDTH/2, top=240, color = "red", fontsize = 140)
        screen.draw.text("Press 'ENTER' to resume", centerx=WIDTH/2, top=350, color="green", fontsize=48)
    
    ## END GAME PAUSE SCREEN
    
    #---------------------------------------------
    
    ## START GAME COMMAND ILLUSTRATION
    
    if command_illustration_variable:
        background.draw()
        command_illustration.draw()
        screen.draw.text("Click 'ENTER' when you're ready", (350, 417), color="green", fontsize=35)
    
    ## END GAME COMMAND ILLUSTRATION
    
def update(dt):
    global score, life, bigger_score, GameOver, collision, level, game_pause, playing, riposiziona_aliens, first_run, wait_sec, aliens_spawned, wait_sec_displayed, command_illustration_variable, same_score_announcement, new_score_announcement, scored_less_announcement
    
    ## START PLAYER MOVEMENT ##
    
    if playing and not GameOver and not game_pause and not first_run:
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

        elif (keyboard.up or keyboard.w) and player.y > 225:
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
    
    if not first_run and not command_illustration_variable and not game_pause and not GameOver:
        for i, alien in enumerate(aliens):
            if aliens[i].y > 650:
                if aliens[5].y > 650:
                    score += 1
                riposiziona_aliens(i)
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
    
    elif first_run:
        elapsed = time.time() - wait_sec

        if elapsed >= 0 and elapsed < 1:
            wait_sec_displayed = 1 #3
        elif elapsed >= 1 and elapsed < 2:
            wait_sec_displayed = 2 #2
        elif elapsed >= 2 and elapsed < 3:
            wait_sec_displayed = 3 #1
        elif elapsed >= 3 and elapsed < 4:
            wait_sec_displayed = 4 #START
        elif elapsed >= 4:
            wait_sec_displayed = 0
            first_run = False
            playing = True

    ## FINISH ALIENS MOVEMENT ##

    #--------------------------------------------
    
    ## START LEVEL COUNT
    
    if playing:
        if score < 6:
            level = 1
        elif score > 5 and score < 10:
            level = 2
        elif score > 9 and score < 20:
            level = 3
        elif score > 19 and score < 35:
            level = 4
        elif score > 34:
            level = 5
    
    ## END LEVEL COUNT

    #--------------------------------------------
    
    ## START COLLISION
    
    if playing:
        touching_alien = False
        
        for alien in aliens:
            if player.colliderect(alien.inflate(-40, -40)):
                touching_alien = True
        
        if touching_alien and not collision:
            life -= 1
            collision = True
            
        if not touching_alien:
            collision = False
    
    ## END COLLISION
    
    #--------------------------------------------
    
    ## START GAME OVER FUNCTION
    
    if playing and life == 0:
        if score == bigger_score:
            same_score_announcement = True
        elif score > bigger_score:
            bigger_score = score
            new_score_announcement = True
        elif score < bigger_score:
            scored_less_announcement = True
        playing = False
        GameOver = True

    ## END GAME OVER FUNCTION
    
    #--------------------------------------------
    
    ## START GAME PAUSE FUNCTION
    
    if playing and life == 0:
        if score == bigger_score:
            same_score_announcement = True
        elif score > bigger_score:
            bigger_score = score
            new_score_announcement = True
        elif score < bigger_score:
            scored_less_announcement = True
        playing = False
        GameOver = True

    ## END GAME PAUSE FUNCTION

def on_key_down(key):
    global command_illustration_variable, playing, game_pause, GameOver, level, life, score, first_run, wait_sec, same_score_announcement, new_score_announcement, scored_less_announcement
    
    ## START COMMAND ILLUSTRATION
    
    if command_illustration_variable:
        if keyboard.RETURN:
            command_illustration_variable = False
            first_run = True
            wait_sec = time.time()
        
    ## END COMMAND ILLUSTRATION
    
    #--------------------------------------------
    
    ## START RESTART IN-GAME
    
    if playing:
        if keyboard.r:
            life = 3
            score = 0
            level = 1
            player.pos = (400,540)
            for i in range(len(aliens)):
                riposiziona_aliens(i) 
                
    ## END RESTART IN-GAME
    
    #--------------------------------------------
    
    ## START GAME OVER
    
    if GameOver:
        if keyboard.RETURN:
            life = 3
            score = 0
            level = 1
            player.pos = (400,540)
            for i in range(len(aliens)):
                riposiziona_aliens(i) 
            GameOver = False
            playing = True
            new_score_announcement = False
            same_score_announcement = False
            scored_less_announcement = False
            
    ## END GAME OVER
    
    #--------------------------------------------
    
    ## START GAME PAUSE
    
    if not first_run and not command_illustration_variable and not game_pause and not GameOver:
        if keyboard.escape:
            game_pause = True
    
    if game_pause:
        if keyboard.RETURN:
            game_pause = False
            first_run = True
        
    ## END GAME PAUSE
    
pgzrun.go()
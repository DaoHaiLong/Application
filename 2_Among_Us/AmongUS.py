import pgzrun
import random
import curses

FONT_COLOR = (255, 255, 255)       #màu RGB
WIDTH = 1350
HEIGHT = 700
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED =10
COLORS=["orange","blue"]

currentlevel=1
maxlevel=5
gameoveer= False
wingame=False
ims =[]
animation=[]

def draw():
    global ims,currentlevel,gameoveer,wingame
    screen.clear()
    screen.blit("dark",(0,0))
    if gameoveer:
        display_message("Game Over","Press space to play again")
    elif wingame:
        display_message("You won","Congratulations ,Press space to play again")
    else:
        for im in ims:
            im.draw()
        
def update():
    global ims,currentlevel,gameoveer,wingame
    if len (ims)==0:
         ims=make_impostors(currentlevel)
    if (gameoveer | wingame) and keyboard.space:
        ims =[]
        currentlevel=1
        gameoveer=False
        wingame=False
        

def make_impostors(number_of_impostors):
    colors_to_crea=get_colors_to_create(number_of_impostors)
    new_ims=create_impostors(colors_to_crea)
    layout_impostors(new_ims)
    animate_impostors(new_ims)
    return new_ims

def get_colors_to_create(number_of_impostors):
    colors_to_crea=["red"]
    for i in range(0,number_of_impostors):
        random_color=random.choice(COLORS)
        colors_to_crea.append(random_color)
    return colors_to_crea

def create_impostors(colors_to_crea):
    new_ims=[]
    for color in colors_to_crea:
        im=Actor(color +"-im")
        new_ims.append(im)
    return new_ims

def layout_impostors(impostors_to_layout):
    number_of_gaps=len(impostors_to_layout) +1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(impostors_to_layout)         # dao lon vi tri cua cao ims tren truc x
    for index,im in enumerate(impostors_to_layout):         #bo dem
        new_x_pos=(index+1)*gap_size
        im.x=new_x_pos

def animate_impostors(impostors_to_animate):
    animations=[]
    for ims in impostors_to_animate:
        duration=START_SPEED-currentlevel            # toc do roi cua ima tamg len theo tung level de tang do kho cho game
        ims.anchor=("center","bottom")
        animation=animate(ims,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global gameoveer
    gameoveer=True

def on_mouse_down(pos):
    global currentlevel,ims
    for im in ims:
        if im.collidepoint(pos):
            if "red" in im.image:
                red_impostor_click()
            else:
                handle_game_over()

def red_impostor_click():
    global currentlevel,ims,animations,wingame
    stop_animations(animation)
    if(currentlevel == maxlevel):
        wingame=True
    else:
        currentlevel=currentlevel+1
        ims=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text,fontsize=150,center=CENTER,color=FONT_COLOR)
    screen.draw.text(sub_heading_text,fontsize=30,center=(CENTER_X,CENTER_Y+100),color=FONT_COLOR)
    
pgzrun.go()

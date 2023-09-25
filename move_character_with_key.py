from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
characterIdle = load_image('character.png')


def handle_events():
    global running, dir, jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                jump = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

running = True
x = 800 // 2
frame = 0
dir = 0


while running:
    clear_canvas()
    
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 15
    y=90
    grass.draw(400, 30)
    if(dir>0):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif(dir<0):
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'H', x, y, 100, 100)
    else:
        characterIdle.draw(x,90)
    if(jump):
        while True:
            
    update_canvas()
    delay(0.05)


close_canvas()


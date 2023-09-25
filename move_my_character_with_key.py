from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('charactersheet.png')

frame_up = [
    (11, 3, 41, 53), 
    (78, 3, 42, 60), 
    (11, 3, 41, 53), 
    (218, 3, 42, 60) 
]

frame_right = [
    (23, 287 - 212, 46, 50), 
    (90, 287 - 212, 46, 54), 
    (23, 287 - 212, 46, 50), 
    (223, 287 - 212, 48, 54), 
]

frame_left = [
    (0, 287 - 140, 46, 50), 
    (69, 287 - 140, 48, 54), 
    (0, 287 - 140, 46, 50),  
    (204, 287 - 140, 46, 54), 
]

frame_down = [
    (11, 287 - 68, 46, 50), 
    (75, 287 - 68, 46, 52), 
    (11, 287 - 68, 46, 50),  
    (219, 287 - 68, 46, 52), 
]

def handle_events():
    global running, x, y, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 1
            elif event.key == SDLK_LEFT:
                dir_x = -1
            elif event.key == SDLK_UP:
                dir_y = 1
            elif event.key == SDLK_DOWN:
                dir_y = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                dir_y = 0

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame_index = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    
    handle_events()
    
    
    if (x + dir_x * 15 > 0 and x + dir_x * 15 < TUK_WIDTH): x += dir_x * 15
    if (y + dir_y * 15 > 0 and y + dir_y * 15 < TUK_HEIGHT): y += dir_y * 15
    
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir_y > 0:
        frame = frame_up[frame_index]
        character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2]*2, frame[3]*2)
        frame_index = (frame_index + 1) % len(frame_up)  
    elif dir_y < 0:
        frame = frame_down[frame_index]
        character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2]*2, frame[3]*2)
        frame_index = (frame_index + 1) % len(frame_down)
    elif dir_x > 0:
        frame = frame_right[frame_index]
        character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2]*2, frame[3]*2)
        frame_index = (frame_index + 1) % len(frame_right)
    elif dir_x < 0:
        frame = frame_left[frame_index]
        character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2]*2, frame[3]*2)
        frame_index = (frame_index + 1) % len(frame_left)
    else:
        character.clip_draw(11, 287 - 68, 46, 50, x, y, 92, 100)
        
    update_canvas()
    delay(0.1)

close_canvas()

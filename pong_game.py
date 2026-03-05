import tkinter as tk
import random

#PARAMETERS
WIDTH = 600
HEIGHT = 450

#Create Paddle
def make_player_paddle():
    h = 15
    w = 100

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if 10 <= x <= 90 and y >= 5:
                img.put("white", (x, y))
    return img

#Create Ball
def make_ball():
    pattern = [
        "00001110000",
        "00011111000",
        "00111111100",
        "01111111110",
        "01111111110",
        "01111111110",
        "00111111100",
        "00011111000",
        "00001110000",
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    for y in range(h):
        for x in range(w):
            if pattern [y] [x] == "1":
                img.put("white", (x, y))
    return img
def colors():
    colors = ["green", "orange", "red", "blue", "violet","indigo"]
    return random.choice(colors)
#Create Bricks
def make_brick():
    h = 15
    w = 50

    img = tk.PhotoImage(width = w, height = h)
    
    color = colors()
    for y in range(h):
        for x in range(w):
            if 10 <= x <= 40 and y >= 5:
                img.put(color, (x, y))
    return img


root = tk.Tk()
root.title("BRICK BLAST")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player_img = make_player_paddle()
ball_img = make_ball()
brick_img = make_brick()

#Create Player 
def start():
    global player
    player = canvas.create_image(WIDTH//2, HEIGHT - 40, image = player_img, anchor = "center")
    #ball = canvas.create_image(WIDTH//2, HEIGHT//2, image = ball_img, anchor = "center")

#Brick Formation
ROWS = 4
COLS = 16
CELL = 32

bricks = []

def create_brick_formation():
    bricks.clear()
    start_x = 5
    start_y = 5
    
    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + 1.1 *c * CELL
            y = start_y + r * CELL

            e = canvas.create_image(x, y, image = brick_img, anchor = "nw")

            bricks.append(e)

#Player Controls
def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)

#Binding
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)\

#Ball Movement
balls = []

def create_ball():
    b = canvas.create_image(WIDTH//2, HEIGHT//2, image = ball_img, anchor = "center")

    balls.append(b)

ball_dx = random.randint(4, 7)
ball_dy = random.randint(4, 7)

def move_ball():
    global ball_dx, ball_dy, balls
    hit_right_wall = False
    hit_left_wall = False
    hit_top = False
    hit_paddle = False
    hit_brick = False
    """
    for b in balls:
        bx1, by1, bx2, by2 = canvas.bbox(b)
        px1, py1, px2, py2 = canvas.bbox(player)
    for e in bricks:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)

        if bx2 >= WIDTH - 10 and ball_dx > 0:
            hit_right_wall = True
        if bx1 <= 10 and ball_dx < 0:
            hit_left_wall = True
        if by1 <= 10 and ball_dy <  0:
            hit_top = True
        if by2 >= py1 - 5 and bx1 >= px1 + 5 and bx2 <= px2 - 5 and ball_dy > 0:
            hit_paddle = True
        if ex1 < bx2 and ex2 > bx1 and ey1 < by2 and ey2 > by1 and ball_dy < 0:
            hit_brick = True
    """
    for b in balls:
        bx1, by1, bx2, by2 = canvas.bbox(b)
        px1, py1, px2, _ = canvas.bbox(player)

        # wall / top / paddle checks per ball
        if bx2 >= WIDTH - 10 and ball_dx > 0:
            hit_right_wall = True
        if bx1 <= 10 and ball_dx < 0:
            hit_left_wall = True
        if by1 <= 10 and ball_dy <  0:
            hit_top = True
        if by2 >= py1 - 5 and bx1 >= px1 + 5 and bx2 <= px2 - 5 and ball_dy > 0:
            hit_paddle = True

    # check bricks for this ball
    for e in bricks:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        if ex1 < bx2 and ex2 > bx1 and ey1 < by2 and ey2 > by1 and ball_dy < 0:
            hit_brick = True
            break


    # Reverse directions as needed, then move once per tick
    if hit_right_wall or hit_left_wall:
        ball_dx = -ball_dx
    if hit_top or hit_paddle or hit_brick:
        ball_dy = -ball_dy

    for b in balls:
        canvas.move(b, ball_dx, ball_dy)
    
#Collision
def collision(e, b):
    ex1, ey1, ex2, ey2 = canvas.bbox(e)
    bx1, by1, bx2, by2 = canvas.bbox(b)

    return ex1 < bx2 and ex2 > bx1 and ey1 < by2 and ey2 > by1

#Game Loop
alive = True

def game_loop():
    global alive
    
    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "red", font = ("Arial", 24))
        canvas.create_text(WIDTH//2, HEIGHT//2 + 30, text = "Press 'R' to Restart", fill = "white", font = ("Arial", 16))
        return
    #create_brick_formation()
    move_ball()

    for b in balls[:]:
        for e in bricks[:]:
            if collision(b, e):
                canvas.delete(e)
                if e in bricks:
                    bricks.remove(e)

                break

    for b in balls[:]:
        x1, y1, x2, y2 = canvas.bbox(b)
        if y2 >= HEIGHT:
            balls.remove(b)
            alive = False
            break

    root.after(60, game_loop)


#Start Game and Reset

def reset(event = None):
    global alive, ball_dx, ball_dy
    canvas.delete("all")
    balls.clear()
    bricks.clear()

    alive = True
    ball_dx = random.randint(4, 7)
    ball_dy = random.randint(4, 7)

    create_ball()
    # start the recurring game loop (game_loop schedules itself with after)
    start()
    create_brick_formation()
    game_loop()
    
root.bind("r", reset)

reset()
root.mainloop()

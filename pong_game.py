import tkinter as tk

#PARAMETERS
WIDTH = 600
HEIGHT = 450

#Create Paddle
def make_player_paddle():
    h = 15
    w = 110

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if 10 <= x <= 100 and y >= 5:
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

root = tk.Tk()
root.title("")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player_img = make_player_paddle()
ball_img = make_ball()

#Create Player 
def start():
    global player
    player = canvas.create_image(WIDTH//2, HEIGHT - 40, image = player_img, anchor = "center")
    ball = canvas.create_image(WIDTH//2, HEIGHT//2, image = ball_img, anchor = "center")


#Player Controls
def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)

#Binding
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


#Starting Angle

#Collision with Left Wall

#Collision with Right Wall

#Collision with Paddle

#Collision with Top Wall

#Start Game and Reset
def reset(event = None):
    global alive, enemy_dx
    canvas.delete("all")

    alive = True
    enemy_dx = 4

    start()

root.bind("r", reset)

reset()
root.mainloop()

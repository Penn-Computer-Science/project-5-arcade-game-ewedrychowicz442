import tkinter as tk

#PARAMETERS
WIDTH = 600
HEIGHT = 450

#Player paddles
def make_paddle1():
    h = 
    w = 

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if 6 <= x <= 17 and y >= 6:
                img.put("white", (x, y))
    return img

def make_paddle2():
    h = 
    w = 

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if 
#Ball

root = tk.Tk()
root.title("Title")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player_img = 
enemy_img = 

#Ball goes past paddle

#Score counter

#Ball movement

#Paddle movement

#Ball and paddle collision

#Game 

#Restart

#Game Over

#Win
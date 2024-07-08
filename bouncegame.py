from tkinter import *
import random
import time
ballcolors = ['red', 'yellow','blue']

class Game:
    def __init__(self, canvas):
        self.status = "before"
        self.canvas = canvas
        self.id = canvas.create_text(250, 250, text = "Press i for Instructions\n"
                                     +"Press s to Start", 
                          font= ('Helvetica', 20), fill = 'black', 
                          state = 'normal')
        self.canvas.bind_all('<KeyPress-s>', self.start_game)
        self.canvas.bind_all('<KeyPress-i>', self.show_instructions)
    
    def show_instructions(self, event):
        if event.keysym == 'i':
            self.canvas.itemconfig(self.id, text = "Move paddle with arrow keys\n"
                                   +"Score one point each time ball hits the paddle\n"
                                   +"Game ends when the ball hits the bottom\n"
                                   +"\n"
                                     +"Press s to Start", 
                          font= ('Helvetica', 20), fill = 'black', 
                          state = 'normal')
    
    def start_game(self, event):
        if event.keysym == 's':
            self.status = "playing"
            self.canvas.itemconfig(self.id, state = 'hidden')
    
    def end_game(self):
        self.status = "game over"
        self.canvas.itemconfig(self.id, text = "Game Over!", 
                          font= ('Helvetica', 40), fill = 'red', 
                          state = 'normal')
        
class Player:
    def __init__(self):
        self.score = 0
        self.id = canvas.create_text(50,475,  font= ('Helvetica', 20), text = 'Score: ' + str(self.score))
    
    def increase(self):
        self.score += 1
    
    def draw(self):
        canvas.itemconfig(self.id,text = 'Score: ' + str(self.score))

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,20, fill = color)
        self.canvas.move(self.id, 195, 400)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)

    def move(self, event):
        pos = self.canvas.coords(self.id)
        if event.keysym == 'Left':
            self.canvas.move(self.id,-50,0)
        if event.keysym == 'Right':
            self.canvas.move(self.id,50,0)
     
    def draw(self):
        pass

class Ball:
    def __init__(self, canvas, paddle, game, color):
        self.canvas = canvas
        self.paddle = paddle
        self.game = game
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        if self.game.status == "playing":
            self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1
        if self.hit_paddle(pos, player) == True:
            self.y = self.y * -1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = self.y * -1

    def hit_paddle(self, pos, player):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                player.increase()
                return True
        return False
    
    def color(self, color):
            self.canvas.itemconfig(self.id, fill = color)

tk = Tk()
tk.title('Bounce Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width = 500, height = 500, bd =0, highlightthickness = 0)
canvas.pack()
tk.update()


game = Game(canvas)
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, game, 'red')
player = Player()

i = 0
while True: 
        if ball.hit_bottom is False:
            ball.draw()
            paddle.draw()
            player.draw()
        if ball.hit_bottom is True:
            game.end_game() 
        ball.color(ballcolors[i%len(ballcolors)])
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        i = i+1

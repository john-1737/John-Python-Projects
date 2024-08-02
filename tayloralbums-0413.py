from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
albums = (PhotoImage(file='/Users/johnbellows/John-Projects/Python-Practice/photoimages/taylor_debut.gif'),
          PhotoImage(file='/Users/johnbellows/John-Projects/Python-Practice/photoimages/taylor_fearless.gif'),
          PhotoImage(file='/Users/johnbellows/John-Projects/Python-Practice/photoimages/taylorspeaknow.gif'),
          PhotoImage(file='/Users/johnbellows/John-Projects/Python-Practice/photoimages/taylor_red.gif'))
albumnames = ('Taylor Swift', 'Fearless', 'Speak Now', 'Red')

class image:
    def __init__(self, canvas, player, albums):
        self.player = player
        self.canvas = canvas
        self.id = canvas.create_image(112, 180)
        self.albumlist = list(albums)

    def draw(self, imagenumber):
        if self.player.status == 'Playing':
            self.canvas.itemconfig(self.id, image=self.albumlist[imagenumber])
            self.albumlist = list(albums)
            del self.albumlist[imagenumber]

class text:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player
        self.id = self.canvas.create_text(112, 10, anchor='n', font=('Helvetica', 12))
     
    def draw(self):
        if self.player.status == 'Start':
            self.canvas.itemconfig(self.id, text='Taylor Swift Albums Game!\n'
                                   +'Click the albums with the correct key\n'
                                   +'when they match the album on screen.\n'
                                   +'\n'
                                   +'Click a to start!')  
        if self.player.status == 'Difficulty':
            self.canvas.itemconfig(self.id, text='Select difficulty:\n'
                                   +'1 = Easy 2 = Medium 3 = Hard\n'
                                   +'\n'
                                   +'Click X to exit.')
        if self.player.status == 'PLaying':
            self.canvas.itemconfig(self.id, text='Click X to exit.')        

class player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.status = 'Start'
        self.difficulty = 1
        self.canvas.bind_all('<KeyPress-a>', self.start_game)
        self.canvas.bind_all('<KeyPress-1>', self.difficulty_level)
        self.canvas.bind_all('<KeyPress-2>', self.difficulty_level)
        self.canvas.bind_all('<KeyPress-3>', self.difficulty_level)

    def start_game(self, event):
        if self.status == 'Start':
            if event.keysym == 'a':
                self.status = 'Difficulty'

    def difficulty_level(self,event):
        if self.status == 'Difficulty':
            if event.keysym == '1':
                self.difficulty = 1
                self.status = 'Playing'
            elif event.keysym == '2':
                self.difficulty = 2
                self.status = 'Playing'
            elif event.keysym == '1':
                self.difficulty = 3
                self.status = 'Playing'

tk.update()
plyr = player(canvas)
t = text(canvas, plyr)
i = image(canvas, plyr, albums)
tk.update()
imagenumber = 1
while True:
    imagenumber = random.randrange(len(i.albumlist) - 1)
    i.draw(imagenumber)
    t.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(1)
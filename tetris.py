from tkinter import *
import random
from time import sleep


tk = Tk()
c = Canvas(tk, width=1000, height=750, bg = "black")
c.pack()
c.create_rectangle(275,100,475,600,fill="black",outline="white")

class Block():
    def __init__(self,level,digit):
        self.o = [[355,-20,375,0],[375,-20,395,0],[355,0,375,20],[375,0,395,20]]
        self.i = [[335,-20,355,0],[355,-20,375,0],[375,-20,395,0],[395,-20,415,0]]
        self.s = [[335,-20,355,0],[355,-20,375,0],[355,-40,375,-20],[375,-40,395,-20]]
        self.z = [[375,-20,395,0],[355,-20,375,0],[355,-40,375,-20],[335,-40,355,-20]]
        self.l = [[335,-20,355,0],[335,-40,355,-20],[355,-40,375,-20],[375,-40,395,-20]]
        self.level = level
        self.digit = digit
        self.whole = []
    def create_block(self):
        self.whole.clear()
        if self.digit == 1:
            for i in range(len(self.o)):
                rect = c.create_rectangle(self.o[i][0],self.o[i][1],self.o[i][2],self.o[i][3],fill="white")
                self.whole.append(rect)
        elif self.digit == 2:
            for i in range(len(self.s)):
                rect = c.create_rectangle(self.s[i][0],self.s[i][1],self.s[i][2],self.s[i][3],fill="white")
                self.whole.append(rect)
        elif self.digit == 3:
            for i in range(len(self.i)):
                 rect = c.create_rectangle(self.i[i][0],self.i[i][1],self.i[i][2],self.i[i][3],fill="white")
                 self.whole.append(rect)
        elif self.digit == 4:
            for i in range(len(self.z)):
                rect = c.create_rectangle(self.z[i][0],self.z[i][1],self.z[i][2],self.z[i][3],fill="white")
                self.whole.append(rect)
        else:
            for i in range(len(self.l)):
                rect = c.create_rectangle(self.l[i][0],self.l[i][1],self.l[i][2],self.l[i][3],fill="white")
                self.whole.append(rect)
    def move(self):
        self.permit = True
        for i in range(len(self.whole)):
            coords = c.coords(self.whole[i])
            if coords[3] > 599:
                self.permit = False
        if self.permit == True:
            for i in range(len(self.whole)):
                c.move(self.whole[i],0,10)
                sleep(2/(self.level*10))
        else:pass

def control(event):
    permit_left = True
    permit_right = True

    for i in range(len(block.whole)):
        coords = c.coords(block.whole[i])
        if coords[0] > 455 or coords[2] > 455:
            permit_right = False
        if coords[0] < 295 or coords[2] < 295:
            permit_left = False

    if event.keysym == "Left" and permit_left == True:
        for i in range(len(block.whole)):
            c.move(block.whole[i],-20,0)
            #sleep(2/(level*1000))

    if event.keysym == "Right" and permit_right == True:
        for i in range(len(block.whole)):
            c.move(block.whole[i],20,0)
            #sleep(2/(level*1000))

c.bind_all("<Key>",control)

level = 9

while True:
    block = Block(level,random.randint(1,5))
    block.create_block()
    tk.update()
    while True:
        block.move()
        tk.update()
        if block.permit == False:
            break
        
    
tk.mainloop()
from guizero import App, Text, PushButton
import math, random

def rollDice(button,max):
    button.text = random.randint(1,max)

app = App(title="Dice",width=480,height=320,layout="grid")

cols = 3
rows = 2
diceTypes = [4,6,8,10,12,20]
buttons = {}

columnWidth = math.ceil(480/cols)
rowHeight = math.ceil(320/rows)

x,y = 0,0
for i in diceTypes:
    button = PushButton(app,image="Assets/Sprites/d"+ str(i) +".png",grid=[x,y],width=columnWidth,height=rowHeight)
    button.update_command(rollDice,[button,i])
    buttons[i] = button

    x +=1
    
    if(x == cols): 
        x = 0
        y += 1

app.display()

from guizero import App, Text, PushButton
import math

from DiceFunctions import *

app = App(title="Dice",width=480,height=320,layout="grid",)

columnWidth = math.ceil(480/3)
rowHeight = math.ceil(320/2)

buttonD4 = PushButton(app,command=rollD4,image="Assets/Sprites/d4.png",grid=[0,1],width=columnWidth,height=rowHeight)
buttonD6 = PushButton(app,command=rollD6,image="Assets/Sprites/d6.png",grid=[1,1],width=columnWidth,height=rowHeight)
buttonD8 = PushButton(app,command=rollD8,image="Assets/Sprites/d8.png",grid=[2,1],width=columnWidth,height=rowHeight)

buttonD10 = PushButton(app,command=rollD10,image="Assets/Sprites/d10.png",grid=[0,2],width=columnWidth,height=rowHeight)
buttonD12 = PushButton(app,command=rollD12,image="Assets/Sprites/d12.png",grid=[1,2],width=columnWidth,height=rowHeight)
buttonD20 = PushButton(app,command=rollD20,image="Assets/Sprites/d20.png",grid=[2,2],width=columnWidth,height=rowHeight)

app.display()




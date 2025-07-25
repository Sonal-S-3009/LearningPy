from swampy.World import  World
world = World()
canvas = world.ca(width=100,height=100,background ='White')
bbox = [[-150,-100],[150,100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([25,25],50,outline =None,fill ='red')
world.mainloop()

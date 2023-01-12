from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.red, 
texture="brick", scale=(2,2,2))

def update():                   
    if held_keys['a']:
        cube.rotation_y += 0.25
    if held_keys['d']:
        cube.rotation_y -= 0.25
    if held_keys['s']:
        cube.rotation_x -= 0.25
    if held_keys['w']:
        cube.rotation_x += 0.25        
         

app.run()

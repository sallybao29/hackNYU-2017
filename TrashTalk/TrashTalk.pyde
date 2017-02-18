from Trash import Trash

def setup ():
    size (700, 700)
    global t
    t = Trash(10, 10, "Banana")

def draw ():
    global t
    background (255)
    t.move()
    t.draw()
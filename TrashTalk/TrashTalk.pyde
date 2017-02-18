from TrashBin import TrashBin
from Trash import Trash, Landfill, Paper, Beverage
import random

LANDFILL = 0
PAPER = 1
BEVERAGE = 2

trash = []
labels = {LANDFILL: ["Styro\nfoam", "Pencil", "Diaper"],
          PAPER: ["News\npaper", "Book", "Pizza\nbox", "Egg\ncarton"],
          BEVERAGE: ["Carton", "Bottle", "Foil", "Glass\nBottle", "Jar"]}

current_trash = None

def make_trash():
    k = random.choice(labels.keys())
    label = random.choice(labels[k])
    x = random.randint(100, 600) % width
    if k == LANDFILL:
        trash.append(Landfill(x, 0, label))
    elif k == PAPER:
        trash.append(Paper(x, 0, label))
    elif k == BEVERAGE:
        trash.append(Beverage(x, 0, label))
  
def setup ():
    global bin
    global cycle
    global img
    size (700, 700)
    landfill = TrashBin (100, 500, (153, 76, 0), "Landfill") 
    paper = TrashBin (300, 500, (0, 0, 255), "Paper")
    beverage = TrashBin (500, 500, (0, 153, 0), "Beverage")
    bin = [landfill, paper, beverage]
    img = loadImage ("green-recycling-icon.jpg")
    make_trash()
    cycle = 0


def mouseDragged():
    #find the trash being dragged 
    #set its x and y to mouseX, mouseY instead of doing regular move
    #if player drags above previous Y cor, break control
    pass
    
def mouseReleased():
    #check that thing being dragged is trash
    #find which trashBin mouse was released on
    #if no trashBin, let trash fall normally
    #call recycle
    
def recycle(trashBin, current_trash):
    #check if current_trash is compatible with trashBin
    #if so, remove current_trash from trash (array)
    #add points
    #otherwise, pile it on the trash stack
    pass
                                    

def draw ():
    global bin
    global cycle
    global img
    background (img)
    for stuff in bin:
        stuff.draw ()
    cycle += 1
    if cycle % 50 == 0:
        make_trash()

    for t in trash:
        t.move()
        t.draw()
    if trash[len(trash)-1].get_y() + trash[len(trash)-1].get_height() > height:
        trash.pop()

   
      
    
    
        
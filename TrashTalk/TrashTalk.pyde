from TrashBin import TrashBin
from Trash import Trash, Landfill, Paper, Beverage
import random

LANDFILL = 0
PAPER = 1
BEVERAGE = 2

trash = []
labels = {LANDFILL: ["Styro\nfoam", "Pencil", "Diaper", "Napkin"],
          PAPER: ["News\npaper", "Soft\nBook", "Pizza\nbox", "Egg\ncarton", "Paper\nBag"],
          BEVERAGE: ["Carton", "Bottle", "Foil", "Glass\nBottle", "Jar", "Yogurt\ncup", "Metal\ncan"]}

global overTrash, locked, current_trash
overTrash = False
locked = False
current_trash = None

def make_trash():
    k = random.choice(labels.keys())
    label = random.choice(labels[k])
    x = random.randint(100, 600) 
    if k == LANDFILL:
        trash.append(Landfill(x, 0, label))
    elif k == PAPER:
        trash.append(Paper(x, 0, label))
    elif k == BEVERAGE:
        trash.append(Beverage(x, 0, label))
  
def setup ():
    global cycle
    global img
    global bin
    size (700, 700)
    landfill = TrashBin (100, 500, (153, 76, 0), "Landfill", Landfill) 
    paper = TrashBin (300, 500, (0, 0, 255), "Paper", Paper)
    beverage = TrashBin (500, 500, (0, 153, 0), "Beverage", Beverage)
    bin = [landfill, paper, beverage]
    img = loadImage ("green-recycling-icon.jpg")
    make_trash()
    cycle = 0

def mousePressed ():
    global overTrash
    global locked
    if overTrash is not None:
        locked = True
    else:
        locked = False
    
def mouseDragged():
    global locked
    if locked:
        if mouseY >= current_trash.get_y() + current_trash.get_width ()/2:
            current_trash.set_x (mouseX-current_trash.get_width()/2)
            current_trash.set_y (mouseY-current_trash.get_height()/2)
    
def mouseReleased():
    global bin
    global current_trash
    global locked
    target = None
    if current_trash and locked:
        for b in bin:
            if b.intersects(current_trash):
                target = b
                break
        if target:
            recycle(b, current_trash)
    current_trash = None
    locked = False
            
    
def recycle(trashBin, curr):
    #check if current_trash is compatible with trashBin
    #if so, remove current_trash from trash (array)
    #add points
    #otherwise, pile it on the trash stack
    if isinstance(curr, trashBin.get_type()):
        print "removed " + curr.get_label()
        rem = trash.remove(curr)
        
   
    
def draw_trash(): 
    i = 0
    while i < len(trash):
        trash[i].move(height)
        trash[i].draw()
        if not trash[i].get_visible():
            rem = trash.pop(i)
            #print "removed " + rem._label
        else:
            i += 1                               

def draw ():
    global cycle
    global img
    global bin
    global current_trash
    background (img)
    for stuff in bin:
        stuff.draw ()
    cycle += 1
    if cycle % 50 == 0:
        make_trash()

    draw_trash()

    for k in trash:
        #print (k.get_x ())
        if k.contains(mouseX, mouseY):
            overTrash = True
            current_trash = k
            if not locked:
                fill(0)
            else:
                overTrash = False

   
      
    
    
        
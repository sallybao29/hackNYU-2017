from TrashBin import TrashBin

def setup ():
    global bin
    global img
    size (700, 700)
    landfill = TrashBin (100, 500, (153, 76, 0), "Landfill") 
    paper = TrashBin (300, 500, (0, 0, 255), "Paper")
    beverage = TrashBin (500, 500, (0, 153, 0), "Beverage")
    bin = [landfill, paper, beverage]
    img = loadImage ("green-recycling-icon.jpg")

def draw ():
    global img
    global bin
    background (img)
    for stuff in bin:
        stuff.draw ()
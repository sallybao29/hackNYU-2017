from TrashBin import TrashBin

def setup ():
    global landfill
    global paper
    global beverage
    global bin
    size (700, 700)
    landfill = TrashBin (100, 500, (153, 76, 0), "Landfill") 
    paper = TrashBin (300, 500, (0, 0, 255), "Paper")
    beverage = TrashBin (500, 500, (0, 153, 0), "Beverage")
    bin = [landfill, paper, beverage]

def draw ():
    global landfill
    global paper
    global beverage
    background (255)
    for stuff in bin:
        stuff.draw ()
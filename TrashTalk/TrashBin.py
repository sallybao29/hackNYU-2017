class TrashBin:
    def __init__ (self, x, y, colortuple, label):
        self._x = x
        self._y = y
        self._colortuple = colortuple
        self._label = label
       
    def draw(self):
        fill (*self._colortuple)
        stroke (0, 0, 0) 
        rect (self._x, self._y, 100, 100) 
        fill ( 255, 255, 255) 
        textAlign (CENTER, CENTER)
        textSize (15)
        text (self._label, self._x + 50, self._y + 50)
    

def setup ():
    global landfill
    size (700, 700) 
    landfill = TrashBin (400, 100, (255,248,220), "landfill")
    
def draw ():
    global landfill
    background ( 255, 255 , 255)
    landfill.draw ()
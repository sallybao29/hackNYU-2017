class Trash(object):
    def __init__(self, x, y, label, col=(0,0,0)):
        self._x = x
        self._y = y
        self._width = 70
        self._height = 50
        self._label = label
        self._color = col
        self._dy = 1
     
    def get_height(self):
        return self._height
    
    def get_y(self):
        return self._y
    
    def move(self):
        self._y += self._dy
        
    def draw(self):
        fill(*self._color)
        rect(self._x, self._y, self._width, self._height, 10)
        textSize(20)
        textAlign(CENTER, CENTER)
        textLeading(15)
        fill(255)
        text(self._label, self._x + self._width // 2, self._y + self._height // 2)
        
    def clicked(self):
        pass
        
class Landfill(Trash):
    def __init__(self, x, y, label):
        super(Landfill, self).__init__(x, y, label)
        self._color = (153, 76, 0)
        
         
class Paper(Trash):
    def __init__(self, x, y, label):
        super(Paper, self).__init__(x, y, label)
        self._color = (0, 0, 255)
        
class Beverage(Trash):
    def __init__(self, x, y, label):
        super(Beverage, self).__init__(x, y, label)
        self._color = (0, 153, 0)
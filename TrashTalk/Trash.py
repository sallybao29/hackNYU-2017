class Trash:
    def __init__(self, x, y, label):
        self._x = x
        self._y = y
        self._width = 70
        self._height = 30
        self._label = label
        self._dy = 1
        
    def move(self):
        self._y += self._dy
        
    def draw(self):
        fill(0, 0, 255)
        rect(self._x, self._y, self._width, self._height, 10)
        textSize(20)
        fill(50)
        text(self._label, self._x, self._y + self._height // 2)
        
    def clicked(self):
        pass
        
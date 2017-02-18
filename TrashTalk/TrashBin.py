class TrashBin:
    def __init__ (self, x, y, colortuple, label, type):
        self._x = x
        self._y = y
        self._colortuple = colortuple
        self._type = type 
        self._label = label
        
    def get_type(self):
        return self._type
        
    def intersects(self, trash):
        tw = th = 100
        x = trash.get_x()
        y = trash.get_y()
        w = trash.get_width()
        h = trash.get_height()
        h_overlaps = (x + w > self._x) and (x < self._x + tw)            
        v_overlaps = (self._y < y + h) and (self._y + th > y)
        return h_overlaps and v_overlaps
       
    def draw(self):
        fill (*self._colortuple)
        stroke (0, 0, 0) 
        rect (self._x, self._y, 100, 100) 
        fill ( 255, 255, 255) 
        textAlign (CENTER, CENTER)
        textSize (15)
        text (self._label, self._x + 50, self._y + 50)
    


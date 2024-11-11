class Item:
    _index = 0
    def __init__(self, type, geometry=[0,0], color = None) -> None:
        self.index = Item._index
        self.z_index = self.index
        self.type = type
        self.geometry = geometry
        self.color = color
        Item._index += 1
        
        
    def setColor(self, color):
        self.color = color
        
    def setX(self, geometry):
        self.geometry[0] = geometry
        
    def setY(self, geometry):
        self.geometry[1] = geometry
        

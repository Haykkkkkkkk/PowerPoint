from document import Document
from metaClass_Factory import AddSlide, DelSlide, OpenSlide, Command
from slide import Slide


class SlideEditor:
    _instance = None

    def __new__(cls, _):
        if not cls._instance:
            cls._instance = super(SlideEditor, cls).__new__(cls)
        return cls._instance

    def __init__(self, document: Document) -> None:
        self.document = document

    def add_slide(self, slide: Slide):
        if slide.pos > self.get_lastSlide_index():
            self.push_back_slide(slide)
        
        
    def get_lastSlide_index(self):
        return len(self.document.slides)
    
    def push_back_slide(self, slide : Slide):
        self.document.append(slide)
        print(f"Slide index is too high, adding slide with index : {self.get_lastSlide_index} ")

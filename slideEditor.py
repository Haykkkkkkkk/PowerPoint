from document import Document
from slide import Slide


class SlideEditor:
    _instance = None
    _document = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SlideEditor, cls).__new__(cls)  # Singleton
            cls._document = Document()
        return cls._instance

    def __init__(self) -> None:
        self.document = Document()
        pass

    def add_slide(self, slide: Slide):
        if slide.pos > self.get_lastSlide_index():
            self.push_back_slide()

    def get_lastSlide_index(self):
        return len(SlideEditor._document.slides)

    def push_back_slide(self):
        
        SlideEditor._document.slides.append(Slide(self.get_lastSlide_index()))
        print(f"Slide index is too high, adding slide with index : {self.get_lastSlide_index() -1 } ")
        self.print_document()
        
    def print_document(self):
        print(SlideEditor._document.slides)



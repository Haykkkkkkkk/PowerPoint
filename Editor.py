from document import Document
from slide import Slide


class Editor:
    _instance = None
    _document = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Editor, cls).__new__(cls)  # Singleton
            cls._document = Document()
        return cls._instance


    def __init__(self) -> None:
        self.document = Document()
        pass


    def add_slide(self, slide: Slide):
        if slide.pos > self.get_lastSlide_index():
            self.push_back_slide()
        elif slide.pos < self.get_lastSlide_index():
            self.insert_slide(slide)

        else:
            Editor._document.slides.append(slide)


    def insert_slide(self, slide: Slide):
        Editor._document.slides.insert(slide.pos, slide)
        self.shifting_slides_right(slide)
        print(f"Adding slide with pos {slide.pos}, shifting anothers slides")


    def shifting_slides_right(self, slide):
        for i in range(slide.pos+1, self.get_lastSlide_index()):
            Editor._document.slides[i].pos += 1


    def get_lastSlide_index(self):
        return len(Editor._document.slides)


    def push_back_slide(self):
        Editor._document.slides.append(Slide(self.get_lastSlide_index()))
        print(f"Slide index is too high, adding slide with index : {self.get_lastSlide_index()-1} ")


    def del_slide(self, pos):
        print(f"Deleting slide with pos {pos}")
        if pos >= self.get_lastSlide_index():
            print(f"Slide with pos {pos} doesnt exist")
        else:
            for i in Editor._document.slides:
                if i.pos == pos:
                    Editor._document.slides.remove(i)
            self.shifting_slides_left(pos)


    def shifting_slides_left(self, pos):
        for i in range(pos, self.get_lastSlide_index()):
            Editor._document.slides[i].pos -= 1


    def print_document(self):
        print(Editor._document.slides)

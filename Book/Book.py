import os
import random
from .Pages import Pages

class Book:
    def __init__(self, bookTitle: str, lines: list):
        self.bookTitle = bookTitle
        self.pages = Pages(lines, bookTitle)
        self.title = self.pages.getBookTitle()
        
    def save(self):
        if self.bookTitle == None:
            self.bookTitle = "Book"+str(random.randint(0, 10000))+".xml"
        path = os.path.join(os.environ['APPDATA'], "Nihonium")
        path = os.path.join(path, self.bookTitle)
        with open(path, "w") as f:
            f.write(self.toXML())
                
    def toXML(self):
        xml = ["<Prologue name='" + self.bookTitle + "'></Prologue>"]
        for line in self.pages.toXML():
            xml.append(line)
        return line
        
    def getPages(self):
        return self.pages
        
    def getTitle(self):
        return self.title
        
    @staticmethod
    def create(bookTitle:str = None):
        if bookTitle == None:
            bookTitle = "Book"+str(random.randint(0, 10000))+".xml"
        path = os.path.join(os.environ['APPDATA'], "Nihonium")
        path = os.path.join(path, bookTitle)
        
        prologue = "<Prologue name='" + bookTitle + "'></Prologue>"
        with open(path, "w") as f:
            f.write(prologue)
        """print(f"File created:" +str(file_path))"""
        return Book(bookTitle, [prologue])
    
    @staticmethod
    def importBook(bookTitle:str = None):
        path = os.path.join(os.environ['APPDATA'], "Nihonium")
        path = os.path.join(path, bookTitle)
        lines = []
        with open(path, "r") as f:
            for line in f:
                lines.append(line.strip())
        return Book(bookTitle, lines)
        
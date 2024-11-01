import xml.etree.ElementTree as ET
from Book.Kanji.KanjiCardGroup import KanjiCardGroup
from Book.Kanji.Kanjicard import Kanjicard


class XmlLoader:
    def __init__(self, lines: list, path: str):
        self.kan = []
        self.voc = []
        self.kan_titles = []
        self.path = path
        self.lines = lines
        
    '''def parseMain(self):
        for line in self.lines:
            tree = line.replace(" ", "")
            tree = tree.replace("<Page", "<")
            tree = tree.replace("</Page", "/")
            tree = tree.replace(">", ",'")
            tree = tree.replace("/,'", "'>")
            tree = tree.split(",")
            tree[0] = tree[0].replace("<", "")
            tree[1] = tree[1].replace("'", "")
            tree[1] = tree[1].replace(">", "")
            if(tree[0] == "type='kanji'"):
                self.kan.append(tree[1])
            elif(tree[0] == "type='voc'"):
                self.voc.append(tree[1])
        return (self.kan, self.voc)'''
        
    def parseMain(self):
        self.kan = []
        self.voc = []
        self.kan_titles = []
        tree = ET.parse(self.path)
        root = tree.getroot()
        for child in root:
            element_tag = child.tag.split('}')[-1]
            if element_tag == "Prologue":
                title = "Test"
            if element_tag == "Page":
                if child.attrib['type'] == "kanji":
                    self.kan.append(child.text)
                    self.kan_titles.append(child.attrib['name'])
                elif child.attrib['type'] == "voc":
                    self.voc.append(child.text)
        """Will certainly change to a special data class"""
        return (self.kan, self.voc,title, self.kan_titles )
                    
                    
    def setLines(self, lines: list):
        self.lines = lines
    
    def parseKanjiGroup(self):
        group = KanjiCardGroup("Untitled")
        tree = ET.parse(self.path)
        root = tree.getroot()
        for child in root:
            element_tag = child.tag.split('}')[-1]
            if element_tag == "Title":
                group.setTitle(child.text)
            elif element_tag == "Cards":
                for card in list(child):
                    kanji = card.find('Kanji').text
                    readings = [reading.text for reading in card.findall('Reading')]
                    meaning = [meaning.text for meaning in card.findall('Meaning')]
                    group.add(Kanjicard(kanji, readings, meaning))
        return group
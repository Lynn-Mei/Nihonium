import xml.etree.ElementTree as ET

class XmlLoader:
    def __init__(self, lines: list, path: str):
        self.kan = []
        self.voc = []
        self.path = path
        self.lines = lines
        
    def parseMain(self):
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
            print(tree)
        return (self.kan, self.voc)

    def setLines(self, lines: list):
        self.lines = lines
    
    def parseKanjiGroup(self):
        """group = KanjiCardGroup("Untitled")"""
        tree = ET.parse(self.path)
        root = tree.getroot()
        for child in root:
            element_tag = child.tag.split('}')[-1]
            if element_tag == "Title":
                """group.setTitle(child.text)"""
                print(f"Title: {child.text}")
            elif element_tag == "Cards":
                for card in list(child):
                    kanji = card.find('Kanji').text
                    readings = [reading.text for reading in card.findall('Reading')]
                    meaning = card.find('Meaning').text
                    print(f"Kanji: {kanji}, Readings: {readings}, Meaning: {meaning}")
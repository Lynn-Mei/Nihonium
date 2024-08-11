class XmlLoader:
    def __init__(self, lines: list):
        self.kan = []
        self.voc = []
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
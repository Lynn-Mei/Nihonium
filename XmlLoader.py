class XmlLoader:
    def __init__(self):
        self.kan = []
        self.voc = []
        self.lines = [
            "<Prologue name='Test-book'>11-08-2024</Prologue>",
            "<Page type='kanji'>kan-0000001.xml</Page>",
            "<Page type='kanji'>kan-0000002.xml</Page>",
            "<Page type='kanji'>kan-0000003.xml</Page>",
            "<Page type='kanji'>kan-0000004.xml</Page>",
            "<Page type='kanji'>kan-0000005.xml</Page>",
            "<Page type='voc'>voc-0000001.xml</Page>",
            "<Page type='voc'>voc-0000002.xml</Page>",
            "<Page type='voc'>voc-0000003.xml</Page>",
            "<Page type='voc'>voc-0000004.xml</Page>",
            "<Page type='voc'>voc-0000005.xml</Page>"
            ]
        
    def parse(self):
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
        
load = XmlLoader()
print(load.parse())
'''  ["[type='kanji'", "kan-000001"]  '''
''' Need to add the import of XmlLoader '''

class Pages:
    def __init__(self, lines:list):
        self.KanjiListing = []
        self.VocListing = []
        '''Les KanjiCardGroup seront gardes ici, il faudra eventuellement optimiser pour eviter d'en garder trop '''
        self.kanjigroups = {}
        self.vocgroups = {}
        parser = XmlLoader(lines)
        tempCollection = parser.parseMain()
        self.KanjiListing = tempCollection[0]
        self.VocListing = tempCollection[1]
        
    def openKanjiGroup(self, index: int)->KanjiCardGroup:
        group: KanjiCardGroup = None
        file = self.KanjiListing[index]
        if file in self.kanjigroups.keys():
            group = self.kanjigroups[file]
        else:
            fileLines = self.getGroupFile(file)
            parser = XmlLoader(fileLines)
            group = parser.parseKanjiGroup()
        self.kanjigroups[file] = group
        return group
        
    '''def openVocGroupPage()->VocCardGroup:
        return VocCardGroup()'''
        
    ''' ToDO : Definir le chemin Nihonium en constante '''
    def getGroupFile(self, file:str) -> list:
        path = os.path.join(os.environ['APPDATA'], "Nihonium")
        path = os.path.join(path, file)
        lines = []
        with open(path, "r") as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def toXml()->str:
        return ["to", "code"]
        
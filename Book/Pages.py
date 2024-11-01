import os
from .XmlLoader import XmlLoader
from Book.Kanji.KanjiCardGroup import KanjiCardGroup

class Pages:
    def __init__(self, lines:list, path: str):
        self.KanjiListing = []
        self.VocListing = []
        '''Les KanjiCardGroup seront gardes ici, il faudra eventuellement optimiser pour eviter d'en garder trop '''
        self.kanjigroups = {}
        self.vocgroups = {}
        parser = XmlLoader(lines, path)
        tempCollection = parser.parseMain()
        self.KanjiListing = tempCollection[0]
        self.VocListing = tempCollection[1]
        self.title = tempCollection[2]
        self.KanTitles = tempCollection[3]
        self.pagespath, file_name = os.path.split(path)
        
    def getBookTitle(self):
        return self.title
        
    def getKanjiGroups(self):
        return self.KanTitles
        
    def getKanjiGroupsPaths(self):
        return self.KanjiListing
        
    def openKanjiGroup(self, index: int)->KanjiCardGroup:
        group: KanjiCardGroup = None
        file = self.KanjiListing[index]
        if file in self.kanjigroups.keys():
            group = self.kanjigroups[file]
        else:
            filePath = self.getPathFile(file)
            parser = XmlLoader([], filePath)
            group = parser.parseKanjiGroup()
        self.kanjigroups[file] = group
        return group
        
    '''def openVocGroupPage()->VocCardGroup:
        return VocCardGroup()'''
        
    ''' ToDO : Definir le chemin Nihonium en constante '''
    def getPathFile(self, file:str) -> list:
        '''path = os.path.join(os.environ['APPDATA'], "Nihonium")'''
        path = os.path.join(self.pagespath, file)
        return path
    
    def toXml(self)->str:
        return ["to", "code"]
        
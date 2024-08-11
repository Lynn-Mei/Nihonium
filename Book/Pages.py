''' Need to add the import of XmlLoader '''

class Pages:
    def __init__(self, lines:list):
        self.KanjiListing = []
        self.VocListing = []
        '''Les KanjiCardGroup seront gardes ici, il faudra eventuellement optimiser pour eviter d'en garder trop '''
        self.kanjigroups = []
        self.vocgroups = []
        parser = XmlLoader(lines)
        tempCollection = parser.parseMain()
        self.KanjiListing = tempCollection[0]
        self.VocListing = tempCollection[1]
        
    def openKanjiGroup(index: int)->KanjiCardGroup:
        group: KanjiCardGroup = None
        '''si fichier contenu dans les keep alors revoyer direct'''
        '''ouverture du fichier correspondant a l'index '''
        '''Parsing et creation d'un KanjiCardGroup'''
        '''Ajout a la liste'''
        return group
        
    '''def openVocGroupPage()->VocCardGroup:
        return VocCardGroup()'''
        
    def toXml()->str:
        return ["to", "code"]
        
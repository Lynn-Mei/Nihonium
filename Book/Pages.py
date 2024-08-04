class Pages:
    def __init__(self, lines:list):
        self.KanjiListing = []
        self.VocListing = []
        '''Les KanjiCardGroup seront gardes ici, il faudra eventuellement optimiser pour eviter d'en garder trop '''
        self.kanjigroups = []
        self.vocgroups = []
        for i in range(1, len(lines)):
            '''Coder l'append des lignes aux listes en fonction de leur type (parsing)'''
        self.t = ""
        
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
        
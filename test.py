from Book.Kanji.KanjiDAO import KanjiDAO

dao = KanjiDAO()
for card in dao.getJLPTKanjicards(2):
    print(card)
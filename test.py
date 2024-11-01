from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList

dao = KanjiDAO()
lists: list[KanjiList] = dao.getLists()
print(lists)
lists[0] = dao.fillList(lists[0])
for card in lists[0].getCards():
    print(card)
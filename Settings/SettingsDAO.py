from KnowledgeBase.AppdataHandler import AppdataHandler


class SettingsDAO():
    def __init__(self):
        self.Appdata : AppdataHandler = AppdataHandler()

    def insert_tags(self, tags:list[str]):
        for tag in range(0, len(tags)):
            self.Appdata.execute('''UPDATE Settings SET value = "''' + tags[tag] + '''" WHERE setting = "Tag''' +
                                 str(tag+1) + '''"''')

    def select_tags(self) -> list[str]:
        data:list = self.Appdata.execute('''SELECT * FROM Setting WHERE setting LIKE "%Tag%"''')
        tags: list[str] = []
        for tag in data:
            tags.append(tag[0])
        return tags
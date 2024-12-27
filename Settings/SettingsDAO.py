from KnowledgeBase.AppdataHandler import AppdataHandler


class SettingsDAO():
    def __init__(self):
        self.Appdata : AppdataHandler = AppdataHandler()

    def insert_tags(self, tags:list[str]):
        for tag in range(0, len(tags)):
            self.Appdata.execute('''UPDATE Settings SET value = "''' + tags[tag] + '''" WHERE setting = "Tag''' +
                                 str(tag+1) + '''"''')

    def select_colors(self)-> dict[str,str]:
        data:list = self.Appdata.execute('''SELECT * FROM Settings WHERE setting LIKE "Color-%"''')
        tags: dict[str,str] = {}
        label:str = ""
        for tag in data:
            label = tag[0]
            tags[label.replace("Color-", "")] = tag[1]
        return tags

    def select_tags(self) -> list[str]:
        data:list = self.Appdata.execute('''SELECT * FROM Settings WHERE setting LIKE "%Tag%"''')
        tags: list[str] = []
        for tag in data:
            tags.append(tag[1])
        return tags

    def push_colors(self, color_data: dict[str, str]):
        for color in color_data.keys():
            request: str = ('''UPDATE settings SET value = "'''+ color_data[color] +'''" WHERE setting = "''' +
                            color + '''"''')
            self.Appdata.execute(request)
        print("a")
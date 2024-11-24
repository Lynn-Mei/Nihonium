from .SettingsDAO import SettingsDAO

class NiumColors(metaclass=ColorSett):
    pass

class ColorSettings():
    def __init__(self):
        self.main_color:str = ""
        self.secondary_color:str = ""
        self.tertiary_color: str = ""
        self.hover_color: str = ""
        self.positive_color: str = ""
        self.neutral_color: str = ""
        self.negative_color: str = ""

        self.tags: list[str] = SettingsDAO.select_tags()

    def setAllColors(self, main_colors:(str,str,str), valued_colors:(str,str,str), tags:list[str]):
        self.main_color = main_colors[0]
        self.secondary_color = main_colors[1]
        self.tertiary_color = main_colors[2]

        self.positive_color = valued_colors[0]
        self.neutral_color = valued_colors[1]
        self.negative_color = valued_colors[2]

        for i in range(0, len(tags)):
            self.tags[i] = tags[i]


    def getTagColor(self, index:int)->str:
        return self.tags[index]

    def getTypedColor(self, range:int)->str:
        ret:str = self.neutral_color
        if range > 0:
            ret = self.positive_color
        elif range < 0:
            ret = self.negative_color
        return ret

    def getMainColor(self)->str:
        return self.main_color

    def getSecondColor(self) -> str:
        return self.secondary_color

    def getThirdColor(self) -> str:
        return self.tertiary_color

    def setMainColor(self)->str:
        return self.main_color

    def setSecondColor(self) -> str:
        return self.secondary_color

    def setThirdColor(self) -> str:
        return self.tertiary_color
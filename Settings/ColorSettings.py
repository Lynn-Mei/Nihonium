from re import match

from .SettingsDAO import SettingsDAO


class ColorSettings():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ColorSettings, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'dao'):
            self.dao = SettingsDAO()
            values: dict[str, str] = self.dao.select_colors()
            self.main_color:str = values["Main"]
            self.secondary_color:str = values["Second"]
            self.tertiary_color: str = values["Third"]
            self.hover_color: str = values["Hover"]
            self.positive_color: str = values["Positive"]
            self.neutral_color: str = values["Neutral"]
            self.negative_color: str = values["Negative"]
            self.tags: list[str] = self.dao.select_tags()

    def setAllColors(self, main_colors:(str,str,str,str), valued_colors:(str,str,str), tags:list[str]):
        self.main_color = main_colors[0]
        self.secondary_color = main_colors[1]
        self.tertiary_color = main_colors[2]
        self.hover_color = main_colors[3]

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

    def getHoverColor(self) -> str:
        return self.hover_color

    def setColorFromTag(self, color_tag: str, value: str):
        match(color_tag):
            case "Main":
                self.main_color = value
            case "Second":
                self.secondary_color = value
            case "Third":
                self.tertiary_color = value
            case "Hover":
                self.hover_color = value
            case "Positive":
                self.positive_color = value
            case "Neutral":
                self.neutral_color = value
            case "Negative":
                self.negative_color = value

    def setTagColor(self, ident:int, value: str):
        self.tags[ident] = value

    def push_data(self):
        dao: SettingsDAO = SettingsDAO()
        color_data: dict[str, str] = {
            "Main": self.main_color,
            "Second": self.secondary_color,
            "Third": self.tertiary_color,
            "Hover": self.hover_color,
            "Positive": self.positive_color,
            "Negative": self.negative_color,
            "Neutral": self.neutral_color
        }
        for i in range(0, len(self.tags)):
            color_data["Tag" + str(i+1)] = self.tags[i]
        dao.push_colors(color_data)
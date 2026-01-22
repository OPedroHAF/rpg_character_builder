from app.character import Character
from app.races import (Human, Elf)
from app.classes import (Fighter, Wizard)

class Application:
    def __init__(self):
        self.character = None

    def create_character(self, name):
        self.character = Character(name)

    def set_race(self, race_name):
        races = {
            "Human": Human,
            "Elf": Elf
        }
        self.character.race = races[race_name]()
        self.character.race.apply_bonus(self.character.ability_scores)

    def set_class(self, class_name):
        classes = {
            "Fighter": Fighter,
            "Wizard": Wizard
        }
        self.character.character_class = classes[class_name]()
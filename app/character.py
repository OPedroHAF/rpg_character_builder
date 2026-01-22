from app.ability_scores import AbilityScores

class Character:
    def __init__(self, name: str):
        self.name = name
        self.race = None
        self.character_class = None
        self.ability_scores = AbilityScores()
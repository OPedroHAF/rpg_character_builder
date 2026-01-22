from app.ability_scores import AbilityScores

class Race:
    name = "Unknown"

    def apply_bonus(self, ability_scores: AbilityScores):
        pass

class Human(Race):
    name = "Human"

    def apply_bonus(self, ability_scores):
        ability_scores.strength += 1
        ability_scores.charisma += 1
        ability_scores.constitution += 1
        ability_scores.dexterity += 1
        ability_scores.intelligence += 1
        ability_scores.wisdom += 1

class Elf(Race):
    name = "Elf"

    def apply_bonus(self, ability_scores):
        ability_scores.dexterity += 2



from app.ability_scores import AbilityScores

class Race:
    name = "Unknown"

    def apply_bonus(self, abilities: AbilityScores):
        raise NotImplementedError

class Human(Race):
    name = "Human"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.strength += 1
        abilities.charisma += 1
        abilities.constitution += 1
        abilities.dexterity += 1
        abilities.intelligence += 1
        abilities.wisdom += 1

class Elf(Race):
    name = "Elf"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.dexterity += 2
    
class HighElf(Elf):
    name = "High Elf"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.intelligence += 1
    
class WoodElf(Elf):
    name = "Wood Elf"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.wisdom += 1

class Dwarf(Race):
    name = "Dwarf"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.constitution += 2

class HillDwarf(Dwarf):
    name = "Hill Dwarf"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.wisdom += 1

class MountainDwarf(Dwarf):
    name = "Mountain Dwarf"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.strength += 2

class Halfling(Race):
    name = "Halfling"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.dexterity += 2

class LightFootHalfling(Halfling):
    name = "Light Foot Halfling"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.charisma += 1

class StoutHalfling(Halfling):
    name = "Stout Halfling"  

    def apply_bonus(self, abilities:AbilityScores):
        super().apply_bonus(abilities)
        abilities.constitution += 1

class Dragonborn(Race):
    name = "Dragonborn"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.strength += 2
        abilities.charisma += 1

class Gnome(Race):
    name = "Gnome"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.intelligence += 2

class ForestGnome(Gnome):
    name = "Forest Gnome"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.dexterity += 1

class RockGnome(Gnome):
    name = "Rock Gnome"

    def apply_bonus(self, abilities: AbilityScores):
        super().apply_bonus(abilities)
        abilities.constitution += 1

class HalfElf(Race):
    name = "Half Elf"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.charisma += 2
        abilities.dexterity += 1
        abilities.wisdom += 1

class HalfOrc(Race):
    name = "Half Orc"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.strength += 2
        abilities.constitution += 1

class Tiefling(Race):
    name = "Tiefling"

    def apply_bonus(self, abilities: AbilityScores):
        abilities.charisma += 2
        abilities.intelligence += 1

RACES_REGISTRY = {

    "Human": Human,
    "Elf (High)": HighElf,
    "Elf (Wood)": WoodElf,
    "Dwarf (Hill)": HillDwarf,
    "Dwarf (Mountain)": MountainDwarf,
    "Halfling (Lightfoot)": LightFootHalfling,
    "Halfling (Stout)": StoutHalfling,
    "Dragonborn": Dragonborn,
    "Gnome (Forest)": ForestGnome,
    "Gnome (Rock)": RockGnome,
    "Half-Elf": HalfElf,
    "Half-Orc": HalfOrc,
    "Tiefling": Tiefling,
}
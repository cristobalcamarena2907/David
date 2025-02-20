from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.health = 100

    def getName(self):
        return self.name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def useAbility(self):
        pass

class Warrior(Character):
    def __init__(self, name, strength=10, armor=5):
        super().__init__(name)
        self.strength = strength
        self.armor = armor

    def attack(self):
        damage = self.strength * (self.level * 0.5)
        return f'{self.name} ataca con su espada causando {damage} de daño'

    def useAbility(self):
        return f'{self.name} usa Grito de Guerra aumentando la moral del equipo'

    def useWeapon(self):
        return f'{self.name} blande su espada con maestría'

class Mage(Character):
    def __init__(self, name, mana=100, intelligence=15):
        super().__init__(name)
        self.mana = mana
        self.intelligence = intelligence

    def attack(self):
        damage = self.intelligence * (self.level * 0.8)
        return f'{self.name} lanza una bola de fuego causando {damage} de daño'

    def useAbility(self):
        return f'{self.name} crea un escudo mágico protector'

    def castSpell(self):
        self.mana -= 10
        return f'{self.name} conjura un hechizo poderoso'

class Archer(Character):
    def __init__(self, name, dexterity=12, range=8):
        super().__init__(name)
        self.dexterity = dexterity
        self.range = range

    def attack(self):
        damage = self.dexterity * (self.level * 0.6)
        return f'{self.name} dispara una flecha causando {damage} de daño'

    def useAbility(self):
        return f'{self.name} usa Disparo Múltiple'

    def shootArrow(self):
        return f'{self.name} dispara una flecha precisa'

class Kingdom(ABC):
    @abstractmethod
    def getCharacters(self):
        pass

    @abstractmethod
    def createQuest(self):
        pass

class MedievalKingdom(Kingdom):
    def getCharacters(self):
        return [
            Warrior("Sir Galahad"),
            Mage("Merlin"),
            Archer("Robin Hood")
        ]

    def createQuest(self):
        return "Nueva misión: Defender el castillo del Rey Arthur"

class DarkKingdom(Kingdom):
    def getCharacters(self):
        return [
            Warrior("Caballero Oscuro"),
            Mage("Brujo Maléfico")
        ]

    def createQuest(self):
        return "Nueva misión: Conquistar el reino vecino"

def main():
    medieval_kingdom = MedievalKingdom()
    print("=== Aventura en el Reino Medieval ===")
    print(medieval_kingdom.createQuest())
    
    print("\nPersonajes en acción:")
    for character in medieval_kingdom.getCharacters():
        print(f"\n{character.getName()}:")
        print(character.attack())
        print(character.useAbility())

if __name__ == '__main__':
    main()
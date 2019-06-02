# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
# Ha pasado el test
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -= damage

# Viking
# Ha pasado el test
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
# Ha pasado el test
class Saxon(Soldier):
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
# Ha pasado el test
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, Viking):
        self.viking_army.append(Viking)

    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)

    def viking_attack(self):
        # Hago randint en lugar de choice, para poder eliminarlo luego de la lista con in index en lugar de por el nombre.
        # Y tengo que crear dos variables, para guardar los índices de los soldados.
        random_saxon = random.randint(0,len(self.saxon_army)-1)
        random_viking = random.randint(0,len(self.viking_army)-1)
        # Un saxon aleatorio recibe daño que proviene de la fuerza de un vikingo aleatorio
        res = self.saxon_army[random_saxon].receive_damage(self.viking_army[random_viking].strength)
        if self.saxon_army[random_saxon].health <= 0:
            self.saxon_army.pop(random_saxon) # Lo elimino de la lista con el pop. Si fuera por nombre, usaría remove.
        return res

    def saxon_attack(self):
        # Hago randint en lugar de choice, para poder eliminarlo luego de la lista con in index en lugar de por el nombre.
        # Y tengo que crear dos variables, para guardar los índices de los soldados.
        random_saxon = random.randint(0,len(self.saxon_army)-1)
        random_viking = random.randint(0,len(self.viking_army)-1)
        # Un vikingo aleatorio recibe daño que proviene de la fuerza de un saxon aleatorio
        res = self.viking_army[random_saxon].receive_damage(self.saxon_army[random_saxon].strength)
        if self.viking_army[random_viking].health <= 0:
            self.viking_army.pop(random_viking) # Lo elimino de la lista con el pop. Si fuera por nombre, usaría remove.
        return res

    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxon_army) > 0 and len(self.viking_army) > 0:
            return "Vikings and Saxons are still in the thick of battle."

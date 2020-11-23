"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@classmethod
	def make_unarmed(cls):
		cls.__name = "Unarmed"
		cls.power = 20
		cls.min_level = 0


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defence, level, weapon=None):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defence = defence
		self.weapon = weapon
		self.level = level

	def compute_damage(self, a, d):
		damage = (((((2*a.level)/5)+2) * (a.weapon.power) * (a.attack/d.defence)) + 2) * ((1/16)*random.randint(85, 100))
		return damage



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	defender.max_hp -= Character.compute_damage(attacker, defender)
	print(f'{attacker.__name__} used {attacker.weapon.__name__}')
	print(f'{defender.__name__} took {defender.max_hp.__name__} dmg')



def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass

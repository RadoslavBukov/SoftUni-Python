"""
Test Code	                                                Output
pokemon = Pokemon("Pikachu", 90)                            Pikachu with health 90
print(pokemon.pokemon_details())                            Caught Pikachu with health 90
trainer = Trainer("Ash")                                    Caught Charizard with health 110
print(trainer.add_pokemon(pokemon))                         This pokemon is already caught
second_pokemon = Pokemon("Charizard", 110)                  You have released Pikachu
print(trainer.add_pokemon(second_pokemon))                  Pokemon is not caught
print(trainer.add_pokemon(second_pokemon))                  Pokemon Trainer Ash
print(trainer.release_pokemon("Pikachu"))                   Pokemon count 1
print(trainer.release_pokemon("Pikachu"))                   - Charizard with health 110
print(trainer.trainer_data())
"""
from project.pokemon import Pokemon
from project.trainer import Trainer

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

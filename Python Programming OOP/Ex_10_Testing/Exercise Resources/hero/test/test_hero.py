from unittest import TestCase, main
from hero.project.hero import Hero

class TestHero(TestCase):
    USERNAME = "Username"
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.attacker_hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__hero_init__should_create_proper_obj(self):
        self.assertEqual(self.USERNAME, self.attacker_hero.username)
        self.assertEqual(self.LEVEL, self.attacker_hero.level)
        self.assertEqual(self.HEALTH, self.attacker_hero.health)
        self.assertEqual(self.DAMAGE, self.attacker_hero.damage)

# Test Battle Method
    def test__hero_battle_with_itself__should_raise_exception(self):
        enemy = Hero(self.USERNAME, 5, 20, 30)
        with self.assertRaises(Exception) as error:                             # When we check exceptions with "with"
            self.attacker_hero.battle(enemy)                                             # Operations which raise the exception
        self.assertEqual("You cannot fight yourself", str(error.exception))     # Check the correct error message


    def test__hero_battle_with_health_less_than_0__should_raise_exception(self):
        enemy = Hero("Enemy", 5, 20, 30)
        self.attacker_hero.health = 0
        with self.assertRaises(ValueError) as error:                             # When we check exceptions with "with"
            self.attacker_hero.battle(enemy)                                         # Operations which raise the exception

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))     # Check the correct error message

    def test__hero_battle_with_enemy_health_less_than_0__should_raise_exception(self):
        enemy_username = "Enemy"
        enemy = Hero(enemy_username, 5, 0, 30)

        with self.assertRaises(ValueError) as error:  # When we check exceptions with "with"
            self.attacker_hero.battle(enemy)  # Operations which raise the exception

        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(error.exception))  # Check the correct error message

    def test__hero_battle__same_enemy_damage__should_return_draw(self):
        enemy = Hero("Enemy", self.LEVEL, self.HEALTH, self.DAMAGE)

        result = self.attacker_hero.battle(enemy)
        expected_health = self.HEALTH - (self.LEVEL * self.DAMAGE)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, self.attacker_hero.health)
        self.assertEqual(expected_health, enemy.health)

    def test__hero_battle__attacker_stronger_than_enemy__should_return_win(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = self.attacker_hero.battle(enemy)
        enemy_expected_health = enemy_health - (self.LEVEL * self.DAMAGE)
        enemy_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        attacker_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        attacker_expected_health = self.HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(enemy_expected_level, self.attacker_hero.level)
        self.assertEqual(attacker_expected_damage, self.attacker_hero.damage)
        self.assertEqual(attacker_expected_health, self.attacker_hero.health)

    def test__hero_battle__attacker_weaker_than_enemy__should_return_lose(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero("Attacker", attacker_level, attacker_health, attacker_damage)

        enemy = Hero("Enemy", self.LEVEL, self.HEALTH, self.DAMAGE)

        result = attacker.battle(enemy)

        attacker_expected_health = attacker_health - (self.LEVEL * self.DAMAGE)
        enemy_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(attacker_expected_health, attacker.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    # Test STR Method
    def test__hero_str__should_return_proper_str(self):
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        actual_result = self.attacker_hero.__str__()

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    main()
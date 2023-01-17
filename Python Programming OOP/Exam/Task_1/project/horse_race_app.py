from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        self.valid_horse_type = ["Appaloosa", "Thoroughbred"]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_type:
            return
        if self.__find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__find_horse_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_las_added_horse_by_horse_type(horse_type)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_horse_race_by_type(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        highest_speed = 0
        race = self.__find_horse_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        for jockey in race.jockeys:
            horse = jockey.horse
            if highest_speed < horse.speed:
                highest_speed = horse.speed
                horse_name = horse.name
                jockey_name = jockey.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."

    def __find_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def __find_las_added_horse_by_horse_type(self, horse_type):

        for horse in reversed(self.horses):
            if horse_type == "Appaloosa":
                if isinstance(horse, Appaloosa) and not horse.is_taken:
                    return horse
            elif horse_type == "Thoroughbred":
                if isinstance(horse, Thoroughbred) and not horse.is_taken:
                    return horse

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __find_horse_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
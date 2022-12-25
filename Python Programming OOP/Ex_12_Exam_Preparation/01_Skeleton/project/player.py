class Player:
    player_names = []    # Check if player names are unique with player_names set
    DEFAULT_STAMINA = 100
    MIN_STAMINA = 0
    MAX_STAMINA = 100

    def __init__(self, name, age, stamina = DEFAULT_STAMINA):   # Stamina is optional param, 100 by default
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in self.player_names:
            raise Exception(f"Name {value} is already used!")
        self.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > self.MAX_STAMINA or value < self.MIN_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

# need_sustenance: bool
# Returns if the player's stamina is less than 100. It is read-only, and it should not be able to be set
    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
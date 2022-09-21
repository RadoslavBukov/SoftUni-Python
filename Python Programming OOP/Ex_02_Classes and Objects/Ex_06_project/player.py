class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    # def player_info(self):
    #     result = []
    #     result.append(f"Name: {self.name}")
    #     result.append(f"Guild: {self.guild}")
    #     result.append(f"HP: {self.hp}")
    #     result.append(f"MP: {self.mp}")
    #
    #     for skill, mana in self.skills.items():
    #         result.append(f"==={skill} - {mana}")
    #
    #     return "\n".join(result)

#   player_info with string return
    def player_info(self):
        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"
        for skill, mana in self.skills.items():
            result += f"==={skill} - {mana}\n"

        return result.strip()       # .strip() for removing the last empty row in the final string
from player import Player
from supply.supply import Supply

class Controller:

    def __init__(self):
        self.players_list = []
        self.supplies_list = []
        self.valid_sustenance = ["Food", "Drink"]

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player in self.players_list:
                continue
            self.players_list.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies_list.append(supply)
        #self.supplies_list.extend(supplies)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)
        if player is None:                                  # if player is not find
            return                                          # Ignore the command
        if sustenance_type not in self.valid_sustenance:    # if sustenance is not valid
            return
        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)   # if Stamina + Supply is more than 100(MAX_stamina) it return the lower result
        self.supplies_list.pop(idx)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_namer, second_player_name):
        first_player = self.__find_player_by_name(first_player_namer)
        second_player = self.__find_player_by_name(second_player_name)

        # if first_player.stamina <= 0 and second_player <=0:
        #     return f"Player {first_player} does not have enough stamina.\nPlayer {second_player} does not have enough stamina."
        # if first_player.stamina <= 0:
        #     return f"Player {first_player} does not have enough stamina."
        # if second_player.stamina <= 0:
        #     return f"Player {second_player} does not have enough stamina."

        error_message = ""
        if first_player.stamina <= 0:
            error_message += f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina <= 0:
            error_message += f"Player {second_player.name} does not have enough stamina."
        if error_message:
            return error_message.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina -= first_player.stamina/2
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {second_player.name}"
        first_player.stamina -= second_player.stamina/2
        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {first_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"


    def next_day(self):
        for player in self.players_list:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):

       return "\n".join([str(x) for x in self.players_list]) + "\n" + "\n".join([str(x) for x in self.supplies_list])   #with comprehension
#         result = ''
#         for player in self.players_list:
#             result += str(player) + "\n"
#         for supply in self.supplies_list:
#             result += str(supply) + "\n"
#        return result


    def __find_player_by_name(self, player_name):
        for player in self.players_list:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        # for supply in reversed(self.supplies_list):
        #     if supply.__class__.__name__ == sustenance_type:
        #         return supply
        for idx in range(len(self.supplies_list) -1, -1, -1):
            supply = self.supplies_list[idx]
            if supply.__class__.__name__ == sustenance_type:
                return (idx, supply)
        return (-1, None)
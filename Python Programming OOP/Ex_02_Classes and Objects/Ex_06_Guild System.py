"""
Test Code:
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

Output:
Skill Shield Break added to the collection of the player George
Name: George
Guild: Unaffiliated
HP: 50
MP: 100
===Shield Break - 20

Welcome player George to the guild UGT
Guild: UGT
Name: George
Guild: UGT
HP: 50
MP: 100
===Shield Break - 20

"""
from Ex_06_project.guild import Guild
from Ex_06_project.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
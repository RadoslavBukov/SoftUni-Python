from project.team import Team
from unittest import TestCase, main

class TestTeam(TestCase):

    TEAM_NAME = "Team"
    OTHER_TEAM_NAME = "TeamTwo"
    MEMBER_NAME1 = "Member1"
    MEMBER_NAME2 = "Member2"
    MEMBER_AGE1 = 18
    MEMBER_AGE2 = 22

    def setUp(self) -> None:
        self.team = Team(self.TEAM_NAME)

# Test Init Method
    def test__team_init__should_create_proper_object(self):
        self.assertEqual(self.TEAM_NAME, self.team.name)
        self.assertEqual({}, self.team.members)

    def test__team_init_with_digit_name__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            team = Team("1sa")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test__team_init_with_digit_name__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            team = Team("sa3")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test__team_init_with_special_symbol_name__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            team = Team("!@")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

# Test Add Member Method
    def test__team_add_members__should_add_members(self):
        actual_result = self.team.add_member(Member1=18, Member2=22)
        self.assertEqual({f"{self.MEMBER_NAME1}":18, f"{self.MEMBER_NAME2}":22}, self.team.members)
        expected_result = f"Successfully added: {self.MEMBER_NAME1}, {self.MEMBER_NAME2}"
        self.assertEqual(expected_result, actual_result)

    def test__team_add_exist_member__should_ignore_member2(self):
        self.team.add_member(Member1=18)
        actual_result = self.team.add_member(Member1=18, Member2=22, Member3=33)
        self.assertEqual({f"{self.MEMBER_NAME1}":18, f"{self.MEMBER_NAME2}":22, "Member3":33}, self.team.members)
        expected_result = f"Successfully added: {self.MEMBER_NAME2}, Member3"
        self.assertEqual(expected_result, actual_result)

    def test__team_add_exist_member__should_ignore_member(self):
        self.team.add_member(Member1=18)
        actual_result = self.team.add_member(Member1=18)
        self.assertEqual({f"{self.MEMBER_NAME1}":18}, self.team.members)
        expected_result = f"Successfully added: "
        self.assertEqual(expected_result, actual_result)

# Test Remove Member Method
    def test__team_remove_exist_member__should_remove_members(self):
        self.team.add_member(Member1=18)
        self.team.add_member(Member2=22)
        actual_result = self.team.remove_member(self.MEMBER_NAME1)
        self.assertEqual({f"{self.MEMBER_NAME2}": 22}, self.team.members)
        self.assertEqual(f"Member {self.MEMBER_NAME1} removed", actual_result)

    def test__team_remove_not_exist_member__should_return_massage_without_removing(self):
        self.team.add_member(Member1=18)
        actual_result = self.team.remove_member(self.MEMBER_NAME2)
        self.assertEqual({f"{self.MEMBER_NAME1}": 18}, self.team.members)
        self.assertEqual(f"Member with name {self.MEMBER_NAME2} does not exist", actual_result)

# Test GT Method
    def test__gt_method_first_is_greater__should_return_proper_massage(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        self.team.add_member(Member1=18)
        actual_result = self.team > other_team
        self.assertEqual(True, actual_result)
        actual_result2 = other_team > self.team
        self.assertEqual(False, actual_result2)

    def test__gt_method_equal_teams__should_return_proper_massage(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        self.team.add_member(Member1=18)
        other_team.add_member(Member2=22)
        actual_result = self.team > other_team
        self.assertEqual(False, actual_result)
        actual_result2 = other_team > self.team
        self.assertEqual(False, actual_result2)

    def test__gt_method_second_bigger_teams__should_return_proper_massage(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        other_team.add_member(Member2=22)
        actual_result = self.team > other_team
        self.assertEqual(False, actual_result)
        actual_result2 = other_team > self.team
        self.assertEqual(True, actual_result2)

# Test Len Method
    def test__len_method_with_empty_dict__should_return_proper_len(self):
        length = len(self.team)
        self.assertEqual(0, length)

    def test__len_method_with_not_empty_dict__should_return_proper_len(self):
        self.team.add_member(Member1=18)
        self.team.add_member(Member2=22)
        self.team.add_member(Member3=33)
        self.team.remove_member("Member3")
        length = len(self.team.members)
        self.assertEqual(2, length)

# Test Add Method
    def test__add_method_with_empty_second_team__should_return_only_first_team(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        self.team.add_member(Member1=18)
        self.team.add_member(Member2=22)
        new_team = self.team + other_team
        self.assertEqual(f"{self.team.name}{other_team.name}", new_team.name)
        self.assertEqual(self.team.members, new_team.members)
        self.assertEqual(True, isinstance(new_team, Team))

    def test__add_method_with_two_team__should_return_both_team_members(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        self.team.add_member(Member1=18)
        other_team.add_member(Member2=22)
        other_team.add_member(Member3=33)
        new_team = self.team + other_team
        self.assertEqual(f"{self.team.name}{other_team.name}", new_team.name)
        self.assertEqual({f"{self.MEMBER_NAME1}":18, f"{self.MEMBER_NAME2}":22, "Member3":33}, new_team.members)

    def test__add_method_with_two_team_one_same_member__should_return_both_team_members(self):
        other_team = Team(self.OTHER_TEAM_NAME)
        self.team.add_member(Member1=18)
        other_team.add_member(Member1=18)
        other_team.add_member(Member3=33)
        new_team = self.team + other_team
        new_team_name = new_team.name
        self.assertEqual(f"{self.team.name}{other_team.name}", new_team_name)
        self.assertEqual({f"{self.MEMBER_NAME1}":18, "Member3":33}, new_team.members)

# Test STR Method:
    def test__str_method_empty_team__should_return_proper_message(self):
        actual_result = str(self.team)
        expected_result = f"Team name: {self.TEAM_NAME}"
        self.assertEqual(expected_result, actual_result)

    def test__str_method_with_two_members__should_sort_them_and_return_proper_message(self):
        self.team.add_member(Member1=18)
        self.team.add_member(Member2=22)
        self.team.add_member(Member3=33)
        actual_result = str(self.team)
        expected_result = f"""Team name: {self.TEAM_NAME}
Member: Member3 - 33-years old
Member: {self.MEMBER_NAME2} - 22-years old
Member: {self.MEMBER_NAME1} - 18-years old"""
        self.assertEqual(expected_result, actual_result)

    def test__str_method_with_two_members_equal_age__should_sort_them_and_return_proper_message(self):
        self.team.add_member(Member2=18)
        self.team.add_member(Member1=18)
        self.team.add_member(Member3=22)
        actual_result = str(self.team)
        expected_result = f"""Team name: {self.TEAM_NAME}
Member: Member3 - 22-years old
Member: {self.MEMBER_NAME1} - 18-years old
Member: {self.MEMBER_NAME2} - 18-years old"""
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
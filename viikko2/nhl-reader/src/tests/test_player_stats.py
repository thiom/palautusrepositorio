import unittest
from player_stats import PlayerStats
from player import Player


def make_player(name, nationality, team, goals, assists):
    return Player({
        "name": name,
        "nationality": nationality,
        "team": team,
        "goals": goals,
        "assists": assists,
        "games": 82,
        "id": hash(name),
    })


class PlayerReaderStub:
    def get_players(self):
        return [
            make_player("Semenko", "CAN", "EDM", 4, 12),       #  4+12 = 16
            make_player("Selanne", "FIN", "ANA", 48, 45),      # 48+45 = 93
            make_player("Kurri", "FIN", "EDM", 37, 53),        # 37+53 = 90
            make_player("Koivu", "FIN", "MTL, ANA", 20, 50),   # 20+50 = 70
            make_player("Gretzky", "CAN", "EDM", 35, 89),      # 35+89 = 124
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def names(self, players):
        return [player.name for player in players]

    def test_nationalities_are_unique_in_order_of_appearance(self):
        self.assertEqual(self.stats.nationalities(), ["CAN", "FIN"])

    def test_top_scorers_by_nationality_sorted_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(self.names(players), ["Selanne", "Kurri", "Koivu"])

    def test_top_scorers_by_unknown_nationality_is_empty(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("SWE"), [])

    def test_top_goal_scorers_sorted_by_goals(self):
        players = self.stats.top_goal_scorers(3)

        self.assertEqual(self.names(players), ["Selanne", "Kurri", "Gretzky"])

    def test_top_goal_scorers_zero_returns_empty(self):
        self.assertEqual(self.stats.top_goal_scorers(0), [])

    def test_top_goal_scorers_more_than_players_returns_all(self):
        self.assertEqual(len(self.stats.top_goal_scorers(10)), 5)

    def test_teams_are_split_unique_and_sorted(self):
        self.assertEqual(self.stats.teams(), ["ANA", "EDM", "MTL"])

    def test_top_scorers_by_team_sorted_by_points(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(self.names(players), ["Gretzky", "Kurri", "Semenko"])

    def test_top_scorers_by_team_includes_traded_players(self):
        self.assertEqual(
            self.names(self.stats.top_scorers_by_team("ANA")),
            ["Selanne", "Koivu"],
        )
        self.assertEqual(
            self.names(self.stats.top_scorers_by_team("MTL")), ["Koivu"]
        )

    def test_top_scorers_by_unknown_team_is_empty(self):
        self.assertEqual(self.stats.top_scorers_by_team("BOS"), [])

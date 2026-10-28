import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_finds_player_by_partial_name(self):
        player = self.stats.search("Gretz")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_for_missing_player(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_returns_players_of_team(self):
        names = [player.name for player in self.stats.team("EDM")]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("PHI"), [])

    def test_top_returns_best_player_first(self):
        top = self.stats.top(1)

        self.assertEqual(top[0].name, "Gretzky")

    def test_top_returns_players_ordered_by_points(self):
        names = [player.name for player in self.stats.top(3)]

        self.assertEqual(names[:3], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_points_is_same_as_default(self):
        default_names = [player.name for player in self.stats.top(3)]
        points_names = [player.name for player in self.stats.top(3, SortBy.POINTS)]

        self.assertEqual(points_names, default_names)

    def test_top_by_goals_returns_players_ordered_by_goals(self):
        names = [player.name for player in self.stats.top(3, SortBy.GOALS)]

        self.assertEqual(names[:3], ["Lemieux", "Yzerman", "Kurri"])

    def test_top_by_assists_returns_players_ordered_by_assists(self):
        names = [player.name for player in self.stats.top(3, SortBy.ASSISTS)]

        self.assertEqual(names[:3], ["Gretzky", "Yzerman", "Lemieux"])

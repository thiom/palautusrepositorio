DEUCE_THRESHOLD = 3
POINTS_TO_WIN = 4
ADVANTAGE_MARGIN = 1

SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def _is_tied(self):
        return self.player1_points == self.player2_points

    def _is_endgame(self):
        return max(self.player1_points, self.player2_points) >= POINTS_TO_WIN

    def _score_name(self, points):
        return SCORE_NAMES[points]

    def _even_score(self):
        if self.player1_points >= DEUCE_THRESHOLD:
            return "Deuce"
        return f"{self._score_name(self.player1_points)}-All"

    def _leader(self):
        if self.player1_points > self.player2_points:
            return "player1"
        return "player2"

    def _advantage_or_win_score(self):
        point_difference = abs(self.player1_points - self.player2_points)
        if point_difference == ADVANTAGE_MARGIN:
            return f"Advantage {self._leader()}"
        return f"Win for {self._leader()}"

    def _running_score(self):
        player1_score = self._score_name(self.player1_points)
        player2_score = self._score_name(self.player2_points)
        return f"{player1_score}-{player2_score}"

    def get_score(self):
        if self._is_tied():
            return self._even_score()
        if self._is_endgame():
            return self._advantage_or_win_score()
        return self._running_score()

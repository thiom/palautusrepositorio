def _player_teams(player):
    """Palauttaa listan pelaajan joukkueista (kauden aikana vaihtaneilla useita)"""
    return [team.strip() for team in player.team.split(",")]


class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def nationalities(self):
        return list(dict.fromkeys(
            player.nationality for player in self._reader.get_players()
        ))

    def top_scorers_by_nationality(self, nationality):
        players = [
            player for player in self._reader.get_players()
            if player.nationality == nationality
        ]
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä"""
        players = self._reader.get_players()
        return sorted(players, key=lambda player: player.goals, reverse=True)[:how_many]

    def teams(self):
        """Palauttaa kauden joukkueet aakkosjärjestyksessä"""
        return sorted({
            team
            for player in self._reader.get_players()
            for team in _player_teams(player)
        })

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pistemäärän mukaan laskevassa järjestyksessä"""
        players = [
            player for player in self._reader.get_players()
            if team in _player_teams(player)
        ]
        return sorted(players, key=lambda player: player.points, reverse=True)

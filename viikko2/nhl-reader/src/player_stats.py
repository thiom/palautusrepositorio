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

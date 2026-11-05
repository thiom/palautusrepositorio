import requests
from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self._url = url
        self._players = None

    def get_players(self):
        if self._players is None:
            response = requests.get(self._url, timeout=10).json()
            self._players = [Player(player_dict) for player_dict in response]
        return self._players

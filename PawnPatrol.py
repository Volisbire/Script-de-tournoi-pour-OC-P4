from typing import List
from tinydb import TinyDB
from Matchs import Matchs
from Players import Player
from Tournament import Tournoi


class PawnPatrol:
    def __init__(self):
        self.player_list = []

        self.tournament: Tournoi
        self.db = TinyDB("db.json")

    def add_player(self, player):
        self.player_list.append(player)
        self.db.insert(player.serialize())

    def register_tournament(self, entry_tournament_name, entry_place, entry_dated,
                            entry_tournament_type_string, entry_comments):
        player_list = self.player_list
        self.tournament = Tournoi(entry_tournament_name, entry_place, entry_dated, player_list,
                                  entry_tournament_type_string, entry_comments)

    def next_round(self):
        self.tournament.next_round()

    def fake_players(self):
        self.player_list = [Player("john1", "titor1", "210781", "M", 8),
                            Player("john2", "titor2", "210781", "M", 2),
                            Player("john3", "titor3", "210781", "M", 3),
                            Player("john4", "titor4", "210781", "M", 4),
                            Player("john5", "titor5", "210781", "M", 5),
                            Player("john6", "titor6", "210781", "M", 6),
                            Player("john7", "titor7", "210781", "M", 7),
                            Player("john8", "titor8", "210781", "M", 1)
                            ]

    def get_match_round(self, round_number) -> List[Matchs]:
        return self.tournament.rounds[round_number].matchs

    def get_round_number(self):
        return self.tournament.nbrturns

    def save(self):
        self.db.insert(self.tournament.serialize())

    def fin_de_tour(self):
        self.tournament.rounds[len(self.tournament.rounds) - 1].end_round()

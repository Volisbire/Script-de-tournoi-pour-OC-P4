import Players


class Matchs:
    def __init__(self, player1: Players, player2: Players):
        self.tuplematch = ([player1, 0], [player2, 0])

    def player1_win(self):
        self.tuplematch[0][0].add_point(1)
        self.tuplematch[0][1] = 1

    def player2_win(self):
        self.tuplematch[1][0].add_point(1)
        self.tuplematch[1][1] = 1

    def draw(self):
        self.tuplematch[0][0].add_point(0.5)
        self.tuplematch[1][0].add_point(0.5)
        self.tuplematch[0][1] = 0.5
        self.tuplematch[1][1] = 0.5
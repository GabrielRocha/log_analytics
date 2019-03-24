class Race:
    def __init__(self, laps):
        self.laps = laps

    @property
    def max_laps(self):
        return max([lap.number for lap in self.laps])

    def __repr__(self):
        return f'Race - {self.max_laps} Laps'

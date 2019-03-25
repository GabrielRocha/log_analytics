class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.laps = []
        self.laps_behind_first_place = None

    @property
    def race_time(self):
        minutes, seconds = divmod(self.race_time_seconds, 60)
        return "%02d:%f" % (minutes, seconds)

    @property
    def race_time_seconds(self):
        return sum(lap.lap_time_seconds for lap in self.laps)

    @property
    def best_lap(self):
        return min(self.laps, key=lambda x: x.lap_time_seconds)

    @property
    def average_speed(self):
        sum_speed = sum([float(lap.average_speed.replace(',', '.')) for lap in self.laps])
        return sum_speed/len(self.laps)

    def __repr__(self):
        return self.name

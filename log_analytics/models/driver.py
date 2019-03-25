class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.laps = []

    @property
    def race_time(self):
        time = sum(lap.lap_time_seconds for lap in self.laps)
        minutes, seconds = divmod(time, 60)
        return "%02d:%f" % (minutes, seconds)

    @property
    def best_lap(self):
        return min(self.laps, key=lambda x: x.lap_time_seconds)

    @property
    def average_speed(self):
        sum_speed = sum([float(lap.average_speed.replace(',', '.')) for lap in self.laps])
        return sum_speed/len(self.laps)

    def __repr__(self):
        return self.name

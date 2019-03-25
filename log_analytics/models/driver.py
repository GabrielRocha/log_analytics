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
        return min([lap for lap in self.laps], key=lambda x: x.lap_time_seconds)

    def __repr__(self):
        return self.name

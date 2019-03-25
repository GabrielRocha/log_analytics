class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.laps = []

    @property
    def race_time(self):
        time = 0
        for lap in self.laps:
            _minutes, _seconds = lap.lap_time.split(':')
            time += int(_minutes)*60 + float(_seconds)
        minutes, seconds = divmod(time, 60)
        return "%02d:%f" % (minutes, seconds)

    def __repr__(self):
        return self.name

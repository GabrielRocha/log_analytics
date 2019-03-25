class Lap:
    def __init__(self, number, lap_time, average_speed):
        self.number = number
        self.lap_time = lap_time
        self.average_speed = average_speed

    @property
    def lap_time_seconds(self):
        _minutes, _seconds = self.lap_time.split(':')
        return int(_minutes) * 60 + float(_seconds)

    def __repr__(self):
        return f'{self.number} - {self.lap_time}'

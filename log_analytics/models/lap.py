class Lap:
    def __init__(self, number, lap_time, average_speed):
        self.number = number
        self.lap_time = lap_time
        self.average_speed = average_speed

    def __repr__(self):
        return f'{self.number} - {self.lap_time}'

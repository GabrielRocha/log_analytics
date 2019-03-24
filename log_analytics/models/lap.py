from log_analytics.models.driver import Driver


class Lap:
    def __init__(self, date_time, driver, number, lap_time, average_speed):
        self.date_time = date_time
        self.driver = Driver(*driver.split(' – '))
        self.number = number
        self.lap_time = lap_time
        self.average_speed = average_speed

    def __repr__(self):
        return f'{self.number} - {self.driver} - {self.lap_time}'

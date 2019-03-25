from log_analytics.models.driver import Driver
from log_analytics.models.lap import Lap


class Race:
    FINAL_LAP = 4

    def __init__(self, laps):
        self.laps = laps
        self._build_drivers()

    def _build_drivers(self):
        self.drivers = {}
        for lap in self.laps:
            driver = Driver(*lap[0].split(' – '))
            lap = Lap(*lap[1:])
            if driver.id not in self.drivers:
                driver.laps.append(lap)
                self.drivers[driver.id] = driver
            else:
                self.drivers[driver.id].laps.append(lap)
            if lap.number == '4':
                break

    def __repr__(self):
        return f'Race - {id(self)}'

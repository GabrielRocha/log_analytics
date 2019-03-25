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
            driver_id, driver_name = lap[0].split(' – ')
            lap = Lap(*lap[1:])
            if driver_id not in self.drivers:
                driver = Driver(driver_id, driver_name)
                driver.laps.append(lap)
                self.drivers[driver_id] = driver
            else:
                self.drivers[driver_id].laps.append(lap)
            if lap.number == '4':
                break

    def result(self):
        final_positions = []
        drivers = list(self.drivers.values())
        lap = self.FINAL_LAP
        while lap > 0 and drivers:
            positions = [driver for driver in drivers if len(driver.laps) == lap]
            final_positions += sorted(positions, key=lambda x: x.race_time)
            [drivers.remove(driver) for driver in positions]  # Remove the driver that finished the race
            lap -= 1
        return enumerate(final_positions, start=1)

    def __repr__(self):
        return f'Race - {id(self)}'

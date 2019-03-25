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

    def result(self):
        final_positions = sorted(self.drivers.values(), key=lambda x: x.race_time)
        first = final_positions[0]
        for driver in final_positions[1:]:
            if self.FINAL_LAP == len(driver.laps):
                driver.laps_behind_first_place = f'+{driver.race_time_seconds - first.race_time_seconds:.3f} seconds'
            else:
                driver.laps_behind_first_place = f'+{self.FINAL_LAP - len(driver.laps)} Lap(s)'
        return enumerate(final_positions, start=1)

    @property
    def best_lap(self):
        return min(
            [driver for driver in self.drivers.values()],
            key=lambda x: x.best_lap.lap_time_seconds
        )

    def __repr__(self):
        return f'Race - {id(self)}'

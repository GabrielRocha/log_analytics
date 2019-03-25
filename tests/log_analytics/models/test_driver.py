from log_analytics.models.driver import Driver
from log_analytics.models.lap import Lap


def test_driver_object():
    driver = Driver('033', 'R.BARRICHELLO')
    assert driver.name == 'R.BARRICHELLO'
    assert driver.id == '033'
    assert driver.__repr__() == 'R.BARRICHELLO'


def test_driver_race_time():
    driver = Driver('033', 'R.BARRICHELLO')
    driver.laps = [
        Lap('1', '1:03.716', '43,675'),
        Lap('2', '1:03.716', '43,675')
    ]
    assert driver.race_time == '02:7.432000'


def test_driver_best_lap():
    driver = Driver('033', 'R.BARRICHELLO')
    driver.laps = [
        Lap('1', '1:13.716', '43,675'),
        Lap('2', '1:03.716', '43,675')
    ]
    assert driver.best_lap.number == '2'
    assert driver.best_lap.lap_time == '1:03.716'


def test_driver_average_speed():
    driver = Driver('033', 'R.BARRICHELLO')
    driver.laps = [
        Lap('1', '1:13.716', '63,675'),
        Lap('2', '1:03.716', '43,675')
    ]
    assert driver.average_speed == 53.675

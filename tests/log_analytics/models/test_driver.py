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

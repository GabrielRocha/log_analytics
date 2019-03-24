from log_analytics.models.lap import Lap
from log_analytics.models.race import Race


def test_race_object():
    lap = Lap('23:51:18.576', '033 – R.BARRICHELLO', '1', '1:03.716', '43,675')
    race = Race([lap])
    assert len(race.laps) == 1
    assert race.laps[0].date_time == '23:51:18.576'
    assert race.laps[0].driver.name == 'R.BARRICHELLO'
    assert race.laps[0].driver.id == '033'
    assert race.laps[0].number == '1'
    assert race.laps[0].lap_time == '1:03.716'
    assert race.laps[0].average_speed == '43,675'
    assert race.max_laps == '1'
    assert race.__repr__() == 'Race - 1 Laps'

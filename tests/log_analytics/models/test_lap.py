from log_analytics.models.lap import Lap


def test_lap_object():
    lap = Lap('23:51:18.576', '033 – R.BARRICHELLO', '3', '1:03.716', '43,675')
    assert lap.date_time == '23:51:18.576'
    assert lap.driver.name == 'R.BARRICHELLO'
    assert lap.driver.id == '033'
    assert lap.number == '3'
    assert lap.lap_time == '1:03.716'
    assert lap.average_speed == '43,675'
    assert lap.__repr__() == '3 - R.BARRICHELLO - 1:03.716'

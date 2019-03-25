from log_analytics.models.lap import Lap


def test_lap_object():
    lap = Lap('3', '1:03.716', '43,675')
    assert lap.number == '3'
    assert lap.lap_time == '1:03.716'
    assert lap.average_speed == '43,675'
    assert lap.__repr__() == '3 - 1:03.716'


def test_lap_time_seconds():
    lap = Lap('3', '1:03.716', '43,675')
    assert lap.lap_time_seconds == 63.716

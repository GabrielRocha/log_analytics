import pytest

from log_analytics.helper import split_log_to_columns, build_race


@pytest.mark.parametrize('line', [
    '23:51:18.576      033 – R.BARRICHELLO\t\t          3\t\t1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO          3\t\t1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO\t\t          3  1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO          3  1:03.716                        43,675',
])
def test_split_log_to_columns(line):
    new_list = split_log_to_columns(line)
    assert new_list == ['23:51:18.576', '033 – R.BARRICHELLO', '3', '1:03.716', '43,675']


def test_build_race():
    content = '\n23:51:18.576      033 – R.BARRICHELLO\t\t          3\t\t1:03.716                        43,675\n'
    race = build_race(content)
    assert len(race.laps) == 1
    assert race.laps[0].date_time == '23:51:18.576'
    assert race.laps[0].driver.name == 'R.BARRICHELLO'
    assert race.laps[0].driver.id == '033'
    assert race.laps[0].number == '3'
    assert race.laps[0].lap_time == '1:03.716'
    assert race.laps[0].average_speed == '43,675'

from log_analytics.models.race import Race


def test_race_object():
    lap = [['033 – R.BARRICHELLO', '1', '1:03.716', '43,675']]
    race = Race(lap)
    assert len(race.laps) == 1
    assert race.drivers['033'].name == 'R.BARRICHELLO'
    assert race.drivers['033'].id == '033'
    assert race.drivers['033'].laps[0].number == '1'
    assert race.drivers['033'].laps[0].lap_time == '1:03.716'
    assert race.drivers['033'].laps[0].average_speed == '43,675'
    assert race.__repr__() == f'Race - {id(race)}'


def test_race_object_with_laps_less_than_4():
    lap = [
        ['033 – R.BARRICHELLO', '1', '1:03.716', '43,675'],
        ['038 – F.MASSA', '1', '2:03.716', '43,675'],
        ['033 – R.BARRICHELLO', '4', '1:03.716', '43,675'],
        ['038 – F.MASSA', '2', '1:03.716', '43,675'],
    ]
    race = Race(lap)
    assert len(race.laps) == 4
    assert race.drivers['033'].name == 'R.BARRICHELLO'
    assert race.drivers['033'].id == '033'
    assert len(race.drivers['033'].laps) == 2
    assert race.drivers['038'].name == 'F.MASSA'
    assert race.drivers['038'].id == '038'
    assert len(race.drivers['038'].laps) == 2
    assert race.drivers['038'].race_time == '03:7.432000'


def test_race_result():
    lap = [
        ['033 – R.BARRICHELLO', '1', '1:03.716', '43,675'],
        ['038 – F.MASSA', '1', '2:03.716', '43,675'],
        ['033 – R.BARRICHELLO', '4', '1:03.716', '43,675'],
        ['038 – F.MASSA', '2', '1:03.716', '43,675'],
    ]
    race = Race(lap)
    result = list(race.result())
    assert result[0][0] == 1
    assert result[0][1].name == 'R.BARRICHELLO'
    assert result[1][0] == 2
    assert result[1][1].name == 'F.MASSA'
    assert result[1][1].laps_behind_first_place == '+2 Lap(s)'


def test_race_best_lap():
    lap = [
        ['033 – R.BARRICHELLO', '1', '1:03.716', '43,675'],
        ['038 – F.MASSA', '1', '2:03.716', '43,675'],
        ['033 – R.BARRICHELLO', '4', '1:03.716', '43,675'],
        ['038 – F.MASSA', '2', '1:03.716', '43,675'],
    ]
    race = Race(lap)
    driver = race.best_lap
    assert driver.name == 'R.BARRICHELLO'
    assert driver.best_lap.lap_time == '1:03.716'

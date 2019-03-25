from log_analytics import analysis


def test_read_log(dir_file):
    file = f'{dir_file}/resource/simple_log'
    content = analysis.read_log(file)
    assert content == 'Here'


def test_final_result(dir_file):
    file = f'{dir_file}/resource/race.log'
    race = analysis.build_race(file)
    assert len(race.laps) == 2
    assert race.drivers['033'].name == 'R.BARRICHELLO'
    assert race.drivers['033'].id == '033'
    assert race.drivers['033'].laps[0].number == '3'
    assert race.drivers['033'].laps[0].lap_time == '1:03.716'
    assert race.drivers['033'].laps[0].average_speed == '43,675'
    assert race.drivers['033'].race_time == '02:7.432000'

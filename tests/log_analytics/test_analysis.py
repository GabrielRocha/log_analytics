from log_analytics import analysis


def test_read_log(dir_file):
    file = f'{dir_file}/resource/simple_log'
    content = analysis.read_log(file)
    assert content == 'Here'

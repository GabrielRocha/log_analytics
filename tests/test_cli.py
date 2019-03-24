import cli


def test_show_log_content(runner, dir_file):
    result = runner.invoke(cli.show_log, ['--file', f'{dir_file}/resource/simple_log'])
    assert result.exit_code == 0
    assert result.output == 'Here\n'

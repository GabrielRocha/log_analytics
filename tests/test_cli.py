import cli


def test_show_log_content_command(runner, dir_file):
    result = runner.invoke(cli.show_log, ['--file', f'{dir_file}/resource/simple_log'])
    assert result.exit_code == 0
    assert result.output == 'Here\n'


def test_race_result_command(runner, dir_file):
    result = runner.invoke(cli.race_result, ['--file', f'{dir_file}/resource/race.log'])
    assert result.exit_code == 0
    assert result.output == ' **Posição Chegada**    **Código Piloto**   **Nome Piloto**   ' \
                            '  **Qtde Voltas Completadas**   **Tempo Total de Prova**\n' \
                            '---------------------  -------------------  ----------------- ' \
                            ' -----------------------------  --------------------------\n' \
                            '          1                    033          R.BARRICHELLO          ' \
                            '          2                02:7.432000\n'

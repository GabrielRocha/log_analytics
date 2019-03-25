import cli


def test_show_log_content_command(runner, dir_file):
    result = runner.invoke(cli.show_log, ['--file', f'{dir_file}/resource/simple_log'])
    assert result.exit_code == 0
    assert result.output == 'Here\n'


def test_race_result_command(runner, dir_file):
    result = runner.invoke(cli.race_result, ['--file', f'{dir_file}/resource/race.log'])
    assert result.exit_code == 0
    assert result.output == ' **Posição Chegada**   ' \
                            ' **Código Piloto**  ' \
                            ' **Nome Piloto**    ' \
                            ' **Qtde Voltas Completadas**  ' \
                            ' **Tempo Total de Prova**    ' \
                            ' **Velocidade Média**  ' \
                            ' **Tempo atrás do Primeiro**\n' \
                            '---------------------  ' \
                            '-------------------  ' \
                            '-----------------  ' \
                            '-----------------------------  ' \
                            '--------------------------  ' \
                            '----------------------  ' \
                            '-----------------------------\n' \
                            '          1           ' \
                            '         033      ' \
                            '    R.BARRICHELLO          ' \
                            '          4          ' \
                            '      04:12.864000                ' \
                            '        43.675\n' \
                            '          2           ' \
                            '         038   ' \
                            '       F.MASSA                ' \
                            '          4          ' \
                            '      04:28.864000                ' \
                            '        48.675      ' \
                            '    +16.000 seconds\n'


def test_best_lap_command(runner, dir_file):
    result = runner.invoke(cli.best_lap, ['--file', f'{dir_file}/resource/race.log'])
    assert result.exit_code == 0
    assert result.output == ' **Código Piloto**   **Nome Piloto**     **Número da Melhor Volta**' \
                            '   **Tempo da Melhor Volta**\n' \
                            '-------------------  -----------------  ----------------------------  ' \
                            '---------------------------\n'\
                            '        038          F.MASSA                         2                1:02.716\n' \
                            '        033          R.BARRICHELLO                   3                1:01.716\n'


def test_race_best_lap_command(runner, dir_file):
    result = runner.invoke(cli.race_best_lap, ['--file', f'{dir_file}/resource/race.log'])
    assert result.exit_code == 0
    assert result.output == ' **Código Piloto**   **Nome Piloto**     **Número da Melhor Volta**' \
                            '   **Tempo da Melhor Volta**\n' \
                            '-------------------  -----------------  ---------------------------- ' \
                            ' ---------------------------\n'\
                            '        033          R.BARRICHELLO                   3                1:01.716\n'

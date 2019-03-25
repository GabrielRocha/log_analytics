import click
from tabulate import tabulate

from log_analytics import analysis


@click.group()
def main():
    ...


@main.command(help='Show the content log file')
@click.option('--file', help='File name with path')
def show_log(file):
    click.echo(analysis.read_log(file))


@main.command(help='The final result of race')
@click.option('--file', help='File name with path')
def race_result(file):
    result = [
        [
            position,
            driver.id,
            driver.name,
            len(driver.laps),
            driver.race_time,
            driver.average_speed,
            driver.laps_behind_first_place
        ]
        for position, driver in analysis.build_race(file).result()
    ]
    click.echo(tabulate(
        result,
        headers=[
            '**Posição Chegada**',
            '**Código Piloto**',
            '**Nome Piloto**',
            '**Qtde Voltas Completadas**',
            '**Tempo Total de Prova**',
            '**Velocidade Média**',
            '**Voltas atrás do Primeiro**'
        ],
        numalign='center'
    ))


@main.command(help='The best lap of each driver')
@click.option('--file', help='File name with path')
def best_lap(file):
    result = [
        (driver.id, driver.name, driver.best_lap.number, driver.best_lap.lap_time)
        for driver in analysis.build_race(file).drivers.values()
    ]
    click.echo(tabulate(
        result,
        headers=[
            '**Código Piloto**',
            '**Nome Piloto**',
            '**Número da Melhor Volta**',
            '**Tempo da Melhor Volta**',
        ],
        numalign='center'
    ))


@main.command(help='The race best lap')
@click.option('--file', help='File name with path')
def race_best_lap(file):
    driver = analysis.build_race(file).best_lap
    result = [(driver.id, driver.name, driver.best_lap.number, driver.best_lap.lap_time)]
    click.echo(tabulate(
        result,
        headers=[
            '**Código Piloto**',
            '**Nome Piloto**',
            '**Número da Melhor Volta**',
            '**Tempo da Melhor Volta**',
        ],
        numalign='center'
    ))


if __name__ == '__main__':
    main()

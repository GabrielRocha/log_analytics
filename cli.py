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
        (position, driver.id, driver.name, len(driver.laps), driver.race_time)
        for position, driver in analysis.build_race(file).result()
    ]
    click.echo(tabulate(
        result,
        headers=[
            '**Posição Chegada**',
            '**Código Piloto**',
            '**Nome Piloto**',
            '**Qtde Voltas Completadas**',
            '**Tempo Total de Prova**'
        ],
        numalign='center'
    ))


if __name__ == '__main__':
    main()

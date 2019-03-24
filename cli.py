import click

from log_analytics import analysis


@click.group()
def main():
    ...


@main.command(help='Show the content log file')
@click.option('--file', help='File name with path')
def show_log(file):
    click.echo(analysis.read_log(file))


if __name__ == '__main__':
    main()

from log_analytics.helper import split_log_to_columns
from log_analytics.models.race import Race


def read_log(log_file):
    with open(log_file, 'r') as log:
        return log.read()


def build_race(log_file):
    content = read_log(log_file)
    rows = content.split('\n')
    laps = [split_log_to_columns(row)[1:] for row in rows[1:] if row]
    return Race(laps)

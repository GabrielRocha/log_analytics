import re

from log_analytics.models.lap import Lap
from log_analytics.models.race import Race

COLUMNS_REGEX = re.compile('\  +|\t+\ +|\t+')


def build_race(content):
    rows = content.split('\n')
    laps = [Lap(*split_log_to_columns(row)) for row in rows[1:] if row]
    return Race(laps)


def split_log_to_columns(item):
    return COLUMNS_REGEX.split(item)

import re

COLUMNS_REGEX = re.compile(r'  +|\t+ +|\t+')


def split_log_to_columns(item):
    return COLUMNS_REGEX.split(item)

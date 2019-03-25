import pytest

from log_analytics.helper import split_log_to_columns


@pytest.mark.parametrize('line', [
    '23:51:18.576      033 – R.BARRICHELLO\t\t          3\t\t1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO          3\t\t1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO\t\t          3  1:03.716                        43,675',
    '23:51:18.576      033 – R.BARRICHELLO          3  1:03.716                        43,675',
])
def test_split_log_to_columns(line):
    new_list = split_log_to_columns(line)
    assert new_list == ['23:51:18.576', '033 – R.BARRICHELLO', '3', '1:03.716', '43,675']

from log_analytics.models.driver import Driver


def test_driver_object():
    driver = Driver('033', 'R.BARRICHELLO')
    assert driver.name == 'R.BARRICHELLO'
    assert driver.id == '033'
    assert driver.__repr__() == 'R.BARRICHELLO'

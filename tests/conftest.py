import pytest
import time
from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver = drivermethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('\nAfter Method')

import pytest


@pytest.fixture(scope="session")
def presetupwork():
    print("I presetup browser instance from conftest file")

##scope = "session" will execute only once per session of pytest execution. 1 Pyest session execution may consider all the test files within a directory


import pytest


@pytest.fixture(scope="module")
def prework():
    print("I set up module instance")
## we are declaring the above function to be reusable and set the frequency of execution by using fixtures
##scope = "class" will get execute only once if any function has a linkage within that class
##scope = "module" will get executed only once per test file
##scope = "function" will get executed everytime before each and every test function

@pytest.fixture(scope="module")
def Firstprework():
    print("I am working with other fixtures and setting up module instance")
    return "pass"

@pytest.fixture(scope="function")
def Secondprework():
    print("I am working with Firstprework fixtures and setting up tear down validation")
    yield
    print("Final Tear down Validation")
## Yield KW is used to pause the execution at the point where it is declared and executes the test case first before it executes the further lines of code of its native function

def test_initialcheck(prework):
    print("First Test Case")
def test_Secondcheck(prework):
    print("Second Test Case")

## Below Test cases are linked with the function defined in conftest.py file to check the globalization usage

def test_conftescase1(presetupwork):
    print("I am TC1 linked with conftest file")

def test_conftescase2(presetupwork):
    print("I am TC2 linked with conftest file")

## Below Test_Cases are written to understand the concept of working with 2 fixtures with 'assertions' and 'Yield' keyword and how it works

def test_asertyld_TC1(Firstprework):
    print("I am TC1 working with 1 fixture with assertions")
    assert Firstprework == "pass"

def test_asertyld_TC2(Firstprework, Secondprework):
    print("I am TC2 working with 2 fixtures with assertions and Yield KW")
    assert Firstprework == "pass"

@pytest.mark.skip
def test_checkskipTC(Firstprework, Secondprework):
    print("I am TC which is skipped")
    assert Firstprework == "pass"

@pytest.mark.smoke
def test_taggedTC(Secondprework):
    print("I am a tagged TC")

## Important note :
# In order to execute the test cases from the command prompt please use the below mcommands:
# Execute file and see the output with logs: python -m pytest test_Section4_Basic_Pytest_Understanding.py -s
# Execute all the test cases from the framework: python -m pytest-s
# Execute a test case from a specific file: python -m pytest test_Section4_Basic_Pytest_Understanding.py::test_asertyld_TC1 -s
# To skip a test case add this at the top of the test case function: @pytest.mark.skip
# To add a tag to the test case add this at the top of the test case function: @pytest.mark.smoke and to execute run cmd: python -m pytest  -m smoke -s
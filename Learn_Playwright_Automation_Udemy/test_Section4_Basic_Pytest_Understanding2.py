import pytest


def test_Thirdcheck(presetupwork):
    print("Third Test Case")


@pytest.mark.smoke
def test_taggedTC2(presetupwork):
    print("I am a tagged TC from a different file")
from task import task
import pytest

def test_task():

    set_1 = {"banana", "cherry", "grape", "mango", "papaya", "lemon"}
    set_2 = {"apple", "pineapple", "orange", "strawberry", "raspberry", "blueberry", "melon"}

    assert task() == [set_1, set_2]
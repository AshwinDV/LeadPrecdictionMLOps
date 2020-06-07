from app import index
from validation import validation_test


def test_index():
    assert index() == "<h1>Lead conversion prediction app</h1>"
    assert validation_test() > 0.6
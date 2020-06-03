from app import index


def test_index():
    assert index() == "<h1>Lead conversion prediction app</h1>"
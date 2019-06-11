def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} Does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} Does not contain {1}".format(collection, item)
    
def test_between(a, b, c):
    assert a <= b <= c, "{0} Is between {1} and {2}".format(a, b, c)
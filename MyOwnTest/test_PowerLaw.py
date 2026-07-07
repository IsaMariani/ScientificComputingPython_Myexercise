from PowerLaw import expected_S, expected_ratio

def test_expected_S():
    assert expected_S(1.3e9, 5e9, 1, 0) == 1.0

def test_extected_ratio():
    res = expected_ratio(4,2)

    exp = 2

    assert res == exp


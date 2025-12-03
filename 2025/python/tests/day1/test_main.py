from day1.main import calculate, calculate_level2


def test_calculate_should_return_3():
    input = ["L68",
             "L30",
             "R48",
             "L5",
             "R60",
             "L55",
             "L1",
             "L99",
             "R14",
             "L82",
             ]

    result = calculate(input)
    assert result == 3


def test_calculate_should_return_1():
    input = ["L68",
             "R210",
             "R8",
             ]

    result = calculate(input)
    assert result == 1

def test_calculate_goes_below_0():
    input = ["L68",
             "L310",
             "R28",
             ]

    result = calculate(input)
    assert result == 1



def test_calculate_level2_should_return_6():
    input = ["L68",
             "L30",
             "R48",
             "L5",
             "R60",
             "L55",
             "L1",
             "L99",
             "R14",
             "L82",
             ]

    result = calculate_level2(input)
    assert result == 6



def test_calculate_level2():
    input = ["L68",
             "L82",
             ]
    result = calculate_level2(input)
    assert result == 2

def test_calculate_level2_goes_below_0():
    input = ["L68",
             "L310",
             "R28",
             ]

    result = calculate_level2(input)
    assert result == 5

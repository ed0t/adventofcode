from day2.main import check_input, process, check_value


def test_main_with_sample_input():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # assert process(input) == 1227775554
    assert process(input) == 4174379265

def test_contains_invalid_ids_at_the_boundaries():
    input = "11-22"
    ids = check_input(input)
    assert 11 in ids
    assert 22 in ids

def test_contains_invalid_ids_within_range():
    input = "95-115"
    ids = check_input(input)
    assert 99 in ids

def test_contains_invalid_ids_as_pair():
    input = "998-1012"
    ids = check_input(input)
    assert 1010 in ids

    input = "1188511880-1188511890"
    ids = check_input(input)
    assert 1188511885 in ids

def test_no_invalid_ids():
    input = "1698522-1698528"
    ids = check_input(input)
    assert ids == []

def test_check_value_with_even_amount_of_same_digit():
    assert check_value(1111) == 1111


def test_check_value_with_odd_amount_of_same_digit():
    assert check_value(11111) == 11111


    

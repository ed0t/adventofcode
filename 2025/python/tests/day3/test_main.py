from day3.main import process_line


def test_finds_top_two_numbers():
    assert process_line("987654321111111", -1) == 98
    assert process_line("811111111111119", -1) == 89
    assert process_line("234234234234278", -1) == 78
    assert process_line("818181911112111", -1) == 92


def test_find_top_12_digit_number():
    assert process_line("234234234234278", -11) == 434234234278
    assert process_line("987654321111111", -11) == 987654321111
    assert process_line("818181911112111", -11) == 888911112111
    assert process_line("811111111111119", -11) == 811111111119

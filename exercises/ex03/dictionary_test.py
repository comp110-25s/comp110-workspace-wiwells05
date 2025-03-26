"""exercise 03 - Dictionary Tests"""

__author__: str = "730774516"


from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_1() -> None:
    """test the invert function from dictionary.py with a use case"""
    test_dict: dict[str, str] = {
        "A": "1",
        "B": "2",
        "C": "3",
    }  # testing a normal use of the function
    assert invert(test_dict) == {
        "1": "A",
        "2": "B",
        "3": "C",
    }, print("ERROR: output did not match expected output")


def test_invert_use_2() -> None:
    """test the invert function from dictionary.py with a use case"""
    test_dict: dict[str, str] = {
        "A": "3",
        "B": "2",
        "C": "1",
    }  # testing another normal use of the function
    assert invert(test_dict) == {
        "3": "A",
        "2": "B",
        "1": "C",
    }, print("ERROR: output did not match expected output")


def test_invert_edge() -> None:
    """test the invert function from dictionary.py with an edge case (empty dict)"""
    test_dict: dict[str, str] = (
        {}
    )  # testing the function when given an empty dictionary
    assert invert(test_dict) == {}, print("ERROR: output did not match expected output")


def test_count_use_1() -> None:
    """test the count function from dictionary.py with a use case"""
    test_list: list[str] = [
        "A",
        "B",
        "C",
        "C",
    ]  # testing the function with a very standard list
    assert count(test_list) == {
        "A": 1,
        "B": 1,
        "C": 2,
    }, print("ERROR: output did not match expected output")


def test_count_use_2() -> None:
    """test the count function from dictionary.py with a use case"""
    test_list: list[str] = [
        "A",
        "A",
        "A",
        "A",
    ]  # testing with another standard list but this time all values are the same
    assert count(test_list) == {"A": 4}, print(
        "ERROR: output did not match expected output"
    )


def test_count_edge() -> None:
    """test the count function from dictionary.py with an edge case"""
    test_list: list[str] = []  # testing with an empty list
    assert count(test_list) == {}, print("ERROR: output did not match expected output")


def test_favorite_color_use_1() -> None:
    """test the favorite color function from dictionary.py with a use case"""
    test_dict: dict[str, str] = {
        "Amy": "Green",
        "John": "Blue",
        "Carter": "Green",
    }  # testing with a standard dictionary
    assert favorite_color(test_dict) == "Green", print(
        "ERROR: output did not match expected output"
    )


def test_favorite_color_use_2() -> None:
    """test the favorite color function from dictionary.py with a use case"""
    test_dict: dict[str, str] = {
        "Amy": "Green",
        "John": "Blue",
        "Carter": "Red",
    }  # testing that the first encountered color wins in the case of a tie
    assert favorite_color(test_dict) == "Green", print(
        "ERROR: output did not match expected output"
    )


def test_favorite_color_edge() -> None:
    """test the favorite color function from dictionary.py with an edge case"""
    test_dict: dict[str, str] = {}  # testing with an empty dictionary
    assert favorite_color(test_dict) == "", print(
        "ERROR: output did not match expected output"
    )


def test_bin_len_use_1() -> None:
    """test the bin_len function from dictionary.py with a use case"""
    test_list: list[str] = [
        "The",
        "Big",
        "Dog",
        "Jumps",
    ]  # testing with a standard list
    assert bin_len(test_list) == {3: {"The", "Big", "Dog"}, 5: {"Jumps"}}, print(
        "ERROR: output did not match expected output"
    )


def test_bin_len_use_2() -> None:
    """test the bin_len function from dictionary.py with a use case"""
    test_list: list[str] = [
        "The",
        "Big",
        "Dog",
        "Dog",
    ]  # testing with a standard list but all words are of equal length
    assert bin_len(test_list) == {3: {"The", "Big", "Dog", "Dog"}}, print(
        "ERROR: output did not match expected output"
    )


def test_bin_len_edge() -> None:
    """test the bin_len function from dictionary.py with an edge case"""
    test_list: list[str] = []  # testing with an empty list
    assert bin_len(test_list) == {}, print(
        "ERROR: output did not match expected output"
    )

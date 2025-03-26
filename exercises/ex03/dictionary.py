"""exercise 03 - Dictionary Functions"""

__author__: str = "730774516"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """take a dictionary and return a dictionary with keys and values swapped"""
    inverse_dict: dict[str, str] = {}
    for key in given_dict:
        if given_dict[key] in inverse_dict:
            raise KeyError("cannot have duplicate keys")
        inverse_dict[given_dict[key]] = key

    return inverse_dict


def count(given_list: list[str]) -> dict[str, int]:
    """count the appearances of an item in a list and store results in a dictionary"""
    count_dict: dict[str, int] = {}
    for i in given_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict


def favorite_color(given_colors: dict[str, str]) -> str:
    """returns the name of the favorite color that appears most frequently"""
    color_list: list[str] = list(given_colors.values())
    color_list.append("")
    counted_dict: dict[str, int] = count(color_list)
    popular_color: str = color_list[0]
    for key in counted_dict:
        if counted_dict[key] > counted_dict[popular_color]:
            popular_color = key

    return popular_color


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    """bins a list of strings by word length"""
    len_dict: dict[int, set[str]] = {}
    for i in word_list:
        if len(i) in len_dict:
            len_dict[len(i)].add(i)
        else:
            len_dict[len(i)] = set()
            len_dict[len(i)].add(i)
    return len_dict

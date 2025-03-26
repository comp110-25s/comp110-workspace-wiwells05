"""exercise 03 - Dictionary Functions"""

__author__: str = "730774516"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """take a dictionary and return a dictionary with keys and values swapped"""
    inverse_dict: dict[str, str] = {}
    for key in given_dict:
        if given_dict[key] in inverse_dict:  # check to see if the key already exists
            raise KeyError("cannot have duplicate keys")
        inverse_dict[given_dict[key]] = (
            key  # the key here essentially evaluates to the original value and then
            # assigns the previous key to the value
        )

    return inverse_dict


def count(given_list: list[str]) -> dict[str, int]:
    """count the appearances of an item in a list and store results in a dictionary"""
    count_dict: dict[str, int] = {}
    for i in given_list:
        if (
            i in count_dict
        ):  # check if the str is already accounted for, if so, add to the count
            count_dict[i] += 1
        else:
            count_dict[i] = 1  # if not then create a new key with value 1

    return count_dict


def favorite_color(given_colors: dict[str, str]) -> str:
    """returns the name of the favorite color that appears most frequently"""
    color_list: list[str] = list(
        given_colors.values()
    )  # take a list of values from the dict so that it can go into the count function
    color_list.append(
        ""
    )  # append empty list so in the case of an empty list, the code will still execute
    counted_dict: dict[str, int] = count(color_list)  # use the count function
    popular_color: str = color_list[
        0
    ]  # give the function a baseline color to compare to later
    for key in counted_dict:
        if (
            counted_dict[key] > counted_dict[popular_color]
        ):  # check if the count of the key is greater than the first encountered key
            # or popular color. this also naturally breaks ties by order of appearance
            popular_color = key  # if the count is higher for a key, that key then
            # becomes the new popular color

    return popular_color


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    """bins a list of strings by word length"""
    len_dict: dict[int, set[str]] = {}
    for i in word_list:
        if len(i) in len_dict:
            len_dict[len(i)].add(
                i
            )  # if an integer key for the length of the word already exists, then add
            # the word to the set for that key
        else:  # if it doesn't already exist,
            len_dict[len(i)] = set()  # make an empty set
            len_dict[len(i)].add(i)  # and add the word to it
    return len_dict

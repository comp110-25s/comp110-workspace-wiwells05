"""exercise 01 - Tea Party. Plan a tea party"""

__author__: str = "730774516"


def main_planner(guests: int) -> None:
    """entry point to program; return cost, # tea bags, # treats for amount of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """return number of tea bags need for an amount of guests"""
    return people * 2


def treats(people: int) -> int:
    """return number of treats for an amount of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """return the cost of treats and tea for a tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

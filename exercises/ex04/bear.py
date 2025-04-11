"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initialize bear class."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increase age by one and decrease hunger score by one."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger score by number of fish."""
        self.hunger_score += num_fish

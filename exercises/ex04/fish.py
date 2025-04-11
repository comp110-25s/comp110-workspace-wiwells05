"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self) -> None:
        """Initialize fish class."""
        self.age = 0

    def one_day(self) -> None:
        """Increase age by one."""
        self.age += 1

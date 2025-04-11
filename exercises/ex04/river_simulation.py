"""File to run river simulations."""

from .river import River

my_river: River = River(2, 10)


my_river.one_river_week()

""" Containing classes of the climate data of a state"""
from typing import Tuple, List
import datetime
from priority_queue import PriorityQueue, EmptyPriorityQueueError
import csv


class Temperature:
    """A class that containing the climate data of given state.

    Instance Attributes:
     - data: A priority queue that store the temperature data in form of (datetime.date, data)
    """
    data: PriorityQueue

    def __init__(self) -> None:
        """Initialize the class with a empty priority queue."""
        self.data = PriorityQueue()

    def read_data(self, filename: str, date_col_name: str, temp_col_name: str) -> None:
        """Read a csv file and extract the date and temperature data from the file."""
        # TODO: Finish this function.


class Precipitation:
    """A class that store a precipitation data of a state.

    Instance Attributes:
     - data: A priority queue that store the precipitation data in form of (datetime.date, float)
     """
    data: PriorityQueue

    def __init__(self) -> None:
        """Initialize the class with a empty priority queue."""
        self.data = PriorityQueue()

    def read_data(self, filename: str, date_col_name: str, pre_col_name: str) -> None:
        """Read a csv file and extract the date and precipitation data in to queue."""
        # TODO: Finih this function.


class WildFire:
    """"A class that store the wild fire data of a given state.

    Instance Attributes:
     -
     """




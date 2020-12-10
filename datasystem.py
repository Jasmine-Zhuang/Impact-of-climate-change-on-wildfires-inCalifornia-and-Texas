"""Containing a class that contain data system class"""
from climate import Temperature, Precipitation, WildFire
from typing import Optional


class DataSystem:
    """A class that keep track of the climate data.

    Instance attributes:
     - temperature: the temperature data.
     - precipitation: the precipitation data
     - wildfire: the data of wildfire
     """
    temperature: Optional[Temperature]
    precipitation: Optional[Precipitation]
    wildfire: Optional[WildFire]

    def __init__(self) -> None:
        """Initialize  a new data system

        The system starts with no entities.
        """
        self.temperature = None

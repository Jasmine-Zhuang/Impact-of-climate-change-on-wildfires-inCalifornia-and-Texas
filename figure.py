"""Show the figures of the project."""
import datetime
from matplotlib import pyplot as plt


def get_time_list(begin: int, end: int) -> list:
    """Return a list of months from the year of begin to the year of end"""
    time_list = []
    for year in range(begin, end + 1):
        for month in range(1, 13):
            time_list.append(datetime.date(year, month, 1))

    return time_list


def figure_dot(title: str, x_label: str, x: list, y_label: str, y: list) -> None:
    """Draw a dot figure."""
    plt.plot(x, y, '.')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def figure_line(title: str, x_label: str, x: list, y_label: str, y: list) -> None:
    """Draw a line figure."""
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

from math import sin

def D(year: int, day_of_year: int) -> float:
    """
    Calculate the Day variable for the two sine waves required by the equation of time

    D can be calculated as follows:
    ```
    D = 6.24004077 + 0.01720197(365.25(y - 2000) + d)
    ```
    where y represents the current year and d the number of days since January 1st

    For more information, visit the `wikipedia page <https://en.wikipedia.org/wiki/Equation_of_time>`_.

    :param year: the current year
    :param day_of_year: the number of days since January 1st
    :return: the value of D
    """
    return 6.24004077 + (0.01720197 * ((365.25 * (year - 2000)) + day_of_year - 0.5))


def equation_of_time(year: int, day_of_year: int) -> float:
    """
    Approximate the equation of time

    The equation of time can be approximated by a sum of two sine waves as follows:
    Δt = -7.659sin(D) + 9.863sin(2D + 3.5932)
    where D represents the Day Constant

    For more information, visit the `wikipedia page <https://en.wikipedia.org/wiki/Equation_of_time>`_.

    :param year: the current year
    :param day_of_year: the number of days since January 1st
    :return: the value of Δt
    """
    day_variable = D(year, day_of_year)
    return (-7.659 * sin(day_variable)) + (9.863 * sin((2 * day_variable) + 3.5932))

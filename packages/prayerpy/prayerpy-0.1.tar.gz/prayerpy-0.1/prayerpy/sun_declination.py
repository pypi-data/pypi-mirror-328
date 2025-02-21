from .degree_geometry import asin, cos, sin


def sun_declination(day_of_year: int) -> float:
    """
    Calculate the declination of the Sun, denoted δ☉, for a given day of the year.
    The declination of the sun is the angle between the rays of the Sun and the plane of the Earth's equator

    δ☉ can be calculated as follows:
    ```
    δ☉ = -arcsin[0.39779cos(0.98565°(N + 10) + 1.914°sin(0.98565°(N - 2)))]
    ```
    where N is the number of days since midnight UT as January 1 begins, i.e. the days part of the ordinal date - 1

    For more information, visit the `wikipedia page <https://en.wikipedia.org/wiki/Position_of_the_Sun>`_.

    :param day_of_year: the number of days since January 1st
    :return: the declination of D
    """
    n = day_of_year - 1
    return 0 - asin(0.39779 * cos((0.98565 * (n + 10)) + (1.914 * sin(0.98565 * (n - 2)))))

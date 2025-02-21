from .equation_of_time import equation_of_time
from .sun_declination import sun_declination
from .degree_geometry import acos, acot, cos, sin, tan
from .config import Config
from math import sqrt


def T(day_of_year:int, alpha:float, config: Config) -> float:
    """
    Calculate the time of the sun at angle alpha for a given day of the year.

    T can be calculated as follows:
    ```
    T = acos((0 - sin(α) - (sin(θ) * sin(λ)))/(cos(θ) * cos(λ))) / 15.0
    ```
    where θ is the latitude in degrees, λ is the sun's declination in degrees, and α is the angle in degrees.

    For more information, visit the `wikipedia page <https://en.wikipedia.org/wiki/Salah_times>`_.

    :param day_of_year: the number of days since January 1st
    :param alpha: the angle at which the sun should be
    :param config: the location config to use for calculations
    :return: the time of the sun at angle alpha
    """
    _lambda = sun_declination(day_of_year)
    _teta = config.latitude
    return acos((0 - sin(alpha) - (sin(_teta) * sin(_lambda)))/(cos(_teta) * cos(_lambda))) / 15.0

def altitude_corrections(config: Config) -> float:
    if config.altitude < 0:
        return -0.0347 * sqrt(0 - config.altitude)
    return 0.0347 * sqrt(config.altitude)

def midday(year:int, day_of_year:int, config: Config) -> float:
    """
    Calculates the midday time, designated Tm, i.e. when the local true solar time reaches noon.

    Tm can be calculated as follows:
    ```
    Tm = 12 - Δt + Z - (λ/15)
    ```
    where Δt is the equation of time, λ is the longitude in degrees, and Z is the timezone in hours.

    The first term is the 12 o'clock noon, the second term accounts for the difference between true
    and mean solar times, and the third term accounts for the difference between the local mean solar 
    time and the timezone.
    For more information, visit the `wikipedia page <https://en.wikipedia.org/wiki/Salah_times>`_.

    :param year: the gregorian year
    :param day_of_year: the number of days since January 1st
    :param config: the location config to use for calculations
    :return: the midday time
    """
    _z = config.tz
    _lambda = config.longitude
    return 12 - (equation_of_time(year, day_of_year) / 60.0) + _z - (_lambda / 15.0)


def sunrise(day_of_year:int, midday:float, config: Config) -> float:
    return midday - T(day_of_year, altitude_corrections(config) + 0.833, config)
def sunset(day_of_year:int, midday:float, config: Config) -> float:
    return midday + T(day_of_year, altitude_corrections(config) + 0.833, config)

def fajr(day_of_year:int, midday:float, config: Config) -> float:
    return midday - T(day_of_year, config.fajr_angle, config)
def isha(day_of_year:int, midday:float, config: Config) -> float:
    return midday + T(day_of_year, config.isha_angle, config)

def asr(day_of_year:int, midday:float, config: Config) -> float:
    A = 0 - acot(config.asr_ratio + tan(config.latitude - sun_declination(day_of_year)))
    return midday + T(day_of_year, A, config)

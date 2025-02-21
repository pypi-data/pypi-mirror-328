from math import floor
from datetime import date
from .config import Config
from .prayer_time import midday, sunrise, sunset, fajr, isha, asr

class Time:
    def __init__(self, hours:float):
        self._hours = hours

    def __str__(self):
        hours = int(floor(self._hours))
        minutes = int(floor((self._hours - hours) * 60))
        seconds = int(floor((self._hours - hours - minutes / 60.0) * 3600))
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def milliseconds(self):
        return self._hours * 3600000

    def hours(self):
        return self._hours

    def pretty(self):
        return self.__str__()

class PrayerTimes:
    fajr:Time
    sunrise:Time
    dhuhr:Time
    midday:Time
    asr:Time
    maghrib:Time
    sunset:Time
    isha:Time

    def __init__(self, fajr:Time, sunrise:Time, midday:Time, asr:Time, sunset:Time, isha:Time):
        self.fajr = fajr
        self.sunrise = sunrise
        self.dhuhr = self.midday = midday
        self.asr = asr
        self.maghrib = self.sunset = sunset
        self.isha = isha

    def __str__(self):
        return '{' + f'"Fajr": "{self.fajr.pretty()}", "Sunrise": "{self.sunrise.pretty()}", "Dhuhr": "{self.dhuhr.pretty()}", "Asr": "{self.asr.pretty()}", "Maghrib": "{self.maghrib.pretty()}", "Isha": "{self.isha.pretty()}"' + '}'

def compute(date: date, **kwargs):
    """
    Compute the prayer times for a given date.

    The Compute method accepts config values to customize the result according to your location and jurisprudence.

    :param date: the date (year, month, day)
    :param latitude: the latitude of the location in degrees, defaults to 0.0
    :param longitude: the longitude of the location in degrees, defaults to 0.0
    :param altitude: the altitude of the location in meters, defaults to 0.0
    :param tz: the timezone offset to consider in hours, e.g. UTC+1 is 1, defaults to 0
    :param fajr_angle: the fajr convention angle of the sun in degrees, defaults to 18 according to the Muslim World League
    :param isha_angle: the isha convention angle of the sun in degrees, defaults to 17 according to the Muslim World League
    :param asr_ratio: the ratio is 1 or 2 depending on jurisprudence, defaults to 1.
    :return: a PrayerTimes object containing the calculated prayer times
    :rtype: PrayerTimes
    """

    config = Config(**kwargs)

    # Calculate the day of the year
    year = date.year
    day_of_year = date.timetuple().tm_yday

    # Calculate the time in hours
    dhuhr = midday(year, day_of_year, config)

    return PrayerTimes(
        fajr=Time(fajr(day_of_year, dhuhr, config)),
        sunrise=Time(sunrise(day_of_year, dhuhr, config)),
        midday=Time(dhuhr),
        asr=Time(asr(day_of_year, dhuhr, config)),
        sunset=Time(sunset(day_of_year, dhuhr, config)),
        isha=Time(isha(day_of_year, dhuhr, config))
    )

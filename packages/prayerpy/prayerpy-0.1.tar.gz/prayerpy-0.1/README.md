# prayerpy

`prayerpy` is a Python library designed to compute prayer times for Muslims based on the date and various configuration parameters such as latitude, longitude, altitude, and timezone. This library provides accurate prayer times according to Islamic conventions.

## Features

- Calculate prayer times for Fajr, Sunrise, Dhuhr, Asr, Maghrib, and Isha.
- Configurable parameters for latitude, longitude, altitude, timezone, and sun angles.
- Easy-to-use API for integration into other applications.
- Built with math and science, no external APIs are used.

## Installation

You can install `prayerpy` using pip:

```sh
pip install prayerpy
```

## Usage

Here is a simple example of how to use `prayerpy` to compute prayer times:
```py
from datetime import date
from prayerpy import compute

# Define the configuration parameters
config = {
    'latitude': 12.345,
    'longitude': 67.890,
    'altitude': 120
}

# Compute prayer times for today
prayer_times = compute(date.today(), **config)

# Print all the prayer times
print(prayer_times)
```

Here is a another example using all configured parameters:

```py
from datetime import date
from prayerpy import compute

# Define the configuration parameters
config = {
    'latitude': 12.345,
    'longitude': 67.890,
    'altitude': 120,
    'tz': 1,
    'fajr_angle': 18.0,
    'isha_angle': 17.0,
    'asr_ratio': 1.0
}

# Compute prayer times for today
prayer_times = compute(date.today(), **config)

# Print all the prayer times
print(prayer_times)
```

Here is a another example to display time of a single prayer:

```py
from datetime import date
from prayerpy import compute

# Define the configuration parameters
config = {
    'latitude': 12.345,
    'longitude': 67.890,
    'altitude': 120
}

# Compute prayer times for today
prayer_times = compute(date.today(), **config)

# Get prayer time of a single prayer
fajr = prayer_times.fajr

# Print the time in HH:MM:SS format 
print(fajr.pretty())

# Print the time as number of milliseconds since midnight 
print(fajr.milliseconds())
```

## Configuration Parameters

| Parameter | Type | Description | Default Value |
| --- | --- | --- | --- |
| `latitude` | *float* | Latitude of the location in degrees. | 0.0 |
| `longitude` | *float* | Longitude of the location in degrees. | 0.0 |
| `altitude` | *float* | Altitude of the location in meters. | 0.0 |
| `tz` | *float* | Timezone offset in hours (e.g., UTC+1 is 1). | 0.0 |
| `fajr_angle` | *float* | The Fajr convention angle of the sun in degrees. | 18.0 |
| `isha_angle` | *float* | The Isha convention angle of the sun in degrees. | 17.0 |
| `asr_ratio` | *float* | The ratio for Asr prayer time calculation. | 1.0 |

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/galalem/python/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on [GitHub](https://github.com/galalem/python)

## Contact

For any questions or inquiries, please contact the author at [khalil.galalem@gmail.com](mailto:khalil.galalem@gmail.com)

## Useful Wiki Links

+ [Salah Times](https://en.wikipedia.org/wiki/Salah_times)
+ [Equation of time](https://en.wikipedia.org/wiki/Equation_of_time)
+ [Sun Declination](https://en.wikipedia.org/wiki/Position_of_the_Sun)
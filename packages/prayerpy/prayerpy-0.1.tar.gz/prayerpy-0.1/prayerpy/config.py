class Config:
    latitude:float = 0.0
    longitude:float = 0.0
    altitude:float = 0.0
    tz:float = 0.0

    fajr_angle:float = 18.0
    isha_angle:float = 17.0
    asr_ratio:float = 1.0

    def __init__(self, latitude:float=0, longitude:float=0, altitude:float=0, tz:float=0, fajr_angle:float = 18.0, isha_angle:float = 17.0, asr_ratio:float = 1.0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.tz = tz
        self.fajr_angle = fajr_angle
        self.isha_angle = isha_angle
        self.asr_ratio = asr_ratio
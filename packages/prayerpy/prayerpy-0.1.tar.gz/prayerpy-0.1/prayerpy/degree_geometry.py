import math

def sin(degrees:float) -> float:
    """
    Calculate the sine of an angle in degrees
    :param degrees: the angle in degrees
    :return: the sine of the given angle
    """
    return math.sin(math.radians(degrees))

def cos(degrees:float) -> float:
    """
    Calculate the cosine of an angle in degrees
    :param degrees: the angle in degrees
    :return: the cosine of the given angle
    """
    return math.cos(math.radians(degrees))

def tan(degrees:float) -> float:
    """
    Calculate the tangent of an angle in degrees
    :param degrees: the angle in degrees
    :return: the tangent of the given angle
    """
    return math.tan(math.radians(degrees))

def acos(value:float) -> float:
    """
    Calculate the arc cosine of a value in degrees
    :param value: the cosine of the angle
    :return: the arc cosine of the given value in degrees
    """
    return math.degrees(math.acos(value))

def asin(value:float) -> float:
    """
    Calculate the arc sine of a value in degrees
    :param value: the sine of the angle
    :return: the arc sine of the given value in degrees
    """
    return math.degrees(math.asin(value))

def acot(value:float) -> float:
    """
    Calculate the arc cotangent of a value in degrees
    :param value: the cotangent
    :return: the arc cotangent of the given value in degrees
    """
    return math.degrees(math.atan(1.0/value))

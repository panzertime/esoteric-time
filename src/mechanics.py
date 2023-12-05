from math import sin, cos, acos, degrees, radians
from collections import namedtuple
from os import environ

import requests
# Turn off the warning about Python not recognizing self-signed firewall certificates
requests.packages.urllib3.disable_warnings() 

Position = namedtuple("Position", "lat lon")

# add a singleton Location variable. Change getLocation to return this variable unless it is unset, reset if so
#loc = environ.get("AQUARIAN_PLACE", None)
#_memoLocation = None if loc == None else Position(float(loc.split(",")[0]), float(loc.split(",")[1]))
#_memoLocation = None

def computeCelestialAngle(A: Position, B: Position):
    # cos(𝐴)=sin(Dec1)sin(Dec2)+cos(Dec1)cos(Dec2)cos(RA1−RA2)
    # Declination (DEC) is the celestial sphere's equivalent of 
    # latitude and it is expressed in degrees, as is latitude. 
    # For DEC, + and - refer to north and south, respectively. 
    # The celestial equator is 0° DEC, and the poles are +90° and -90°. 
    # Right ascension (RA) is the celestial equivalent of longitude.
    anglesCosine = (sin(radians(A.lat)) * sin(radians(B.lat))) + (cos(radians(A.lat)) * cos(radians(B.lat)) * cos(radians(A.lon) - radians(B.lon)))
    return degrees(acos(anglesCosine))

def arePlanetsAligned(A: Position, B: Position, *args, **kwargs):
    # .8 degrees is pretty close and gives us like a 50-hour period
    # of "alignment" for Mars and Jupiter.
    # 1 degree is about 4 days of "alignment"
    # .5 degrees is about 36 hours of "alignment"
    window = kwargs.get("window", .8)
    angle = computeCelestialAngle(A, B)
    return True if angle < window else False

def getLocation():
    # try env var first
    # if not set, try online
    # if that fails return 0,0
    loc = environ.get("AQUARIAN_PLACE", None)
    if loc is None:
        try:
            r = requests.get("https://ipinfo.io", verify=False)
            pos = r.json()["loc"].split(",")
            return Position(float(pos[0]), float(pos[1]))
        except:
            return Position(0.0, 0.0)
    else:
        pos = loc.split(",")
        return Position(pos[0], pos[1])

from math import sin, cos, acos, degrees, radians
from collections import namedtuple
from os import environ

import requests
# Turn off the warning about Python not recognizing self-signed firewall certificates
requests.packages.urllib3.disable_warnings() 

Position = namedtuple("Position", "lat lon")

# add a singleton Location variable. Change getLocation to return this variable unless it is unset, reset if so
__memoLocation = None

def computeCelestialAngle(A, B):
    # cos(𝐴)=sin(Dec1)sin(Dec2)+cos(Dec1)cos(Dec2)cos(RA1−RA2)
    # Declination (DEC) is the celestial sphere's equivalent of latitude and it is expressed in degrees, as is latitude. 
    # For DEC, + and - refer to north and south, respectively. 
    # The celestial equator is 0° DEC, and the poles are +90° and -90°. 
    # Right ascension (RA) is the celestial equivalent of longitude.
    anglesCosine = (sin(radians(A.lat)) * sin(radians(B.lat))) + (cos(radians(latA)) * cos(radians(latB)) * cos(radians(lonA) - radians(lonB)))
    return degrees(acos(anglesCosine))

def arePlanetsAligned(A: Position, B: Position):
    angle = computeCelestialAngle(A.lat, B.lat, A.lon, B.lon)

def getLocation():
    if __memoLocation is None:
        try:
            r = requests.get("https://ipinfo.io", verify=False)
            loc = r.json()["loc"].split(",")
            __memoLocation = Position()
        except:
            loc = environ.get("AQUARIAN_PLACE", "0,0").split(",")
            __memoLocation = Position(float(loc[0]), float(loc[1]))
    return __memoLocation

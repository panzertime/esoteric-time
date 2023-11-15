from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const, object
from collections import namedtuple
from datetime import datetime

from mechanics import Position
import mechanics

PHILOSOPHY = ["This is the dawning of the Age of Aquarius",
              "When the Moon is in the seventh house and Jupiter aligns with Mars", 
              "then peace will guide the planets and love will steer the stars"]

Alignment = namedtuple("Alignment", "jupiterPos, marsPos, moonHouse")

def objectToPosition(orb: object):
    return Position(orb.lat, orb.lon)

def currentDateTime():
    stamp = datetime.utcnow()
    return Datetime("/".join([str(stamp.year),str(stamp.month),str(stamp.day)]), 
                    ":".join([str(stamp.hour), str(stamp.minute)]), 
                    utcoffset=0)

def positionToGeoPos(pos: Position):
    return GeoPos(pos.lat, pos.lon)

def computeCurrentAlignment():
    chart = Chart(currentDateTime(), 
                  positionToGeoPos(mechanics.getLocation()), 
                  IDs=[const.JUPITER, const.MARS, const.MOON])
    jupiter = objectToPosition(chart.get(const.JUPITER))
    mars = objectToPosition(chart.get(const.MARS))
    moonHouse = chart.houses.getObjectHouse(chart.get(const.MOON)).num()
    return Alignment(jupiter, mars, moonHouse)

def isMomentAquarian(moment: Alignment):
    if moment.moonHouse != 7:
        return False
    if mechanics.computeCelestialAngle(moment.marsPos, moment.jupiterPos) > .8:
        return False
    return True

import ephem
import geocoder
import math

greenwich = ephem.Observer()
sun = ephem.Sun(greenwich)
SunLongitude = math.degrees(sun.ra - greenwich.sidereal_time())
SunLongitude += 360 if SunLongitude < -180 else 0
SunLongitude -= 360 if SunLongitude > 180 else 0
SunLatitude = math.degrees(sun.dec)

MyLongitude, MyLatitude = geocoder.ip('me').latlng[0], geocoder.ip('me').latlng[1]

Distance = ((SunLongitude - MyLongitude) ** 2 + (SunLatitude - MyLatitude) ** 2) ** 0.5

print("The Distance From Us And The SubSolar Point Is:", (Distance / 360) * math.pi * 2 * 6371, "Km")
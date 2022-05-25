"""
Test Code	                                        Output
town = Town("Sofia")                                Town: Sofia | Latitude: 42° 41' 51.04" N | Longitude: 23° 19' 26.94" E
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
"""

class Town:
    latitude = 0
    longitude = 0

    def __init__(self, name):
        self.name = name

    def set_latitude(self,latitude):
        self.latitude = latitude
        Town.latitude = self.latitude

    def set_longitude(self,longitude):
        self.longitude = longitude
        Town.longitude = self.longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {Town.latitude} | Longitude: {Town.longitude}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)


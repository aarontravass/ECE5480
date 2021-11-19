# lat/long to physical address
# Test geopy.geocoders Nominatim
#
# https://pypi.org/project/geopy/
# Eg, install: conda install -c conda-forge geopy (from https://anaconda.org/conda-forge/geopy)

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='my_application')
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)


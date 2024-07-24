from input.google_maps import GoogleMapsAPI
from entrypoint import get_api_key
import matplotlib.pyplot as plt


def test_get_google_maps_api_smoke_test():
	start_coords = (-15.899523, 34.888095)  # dorpje van Koen
	end_coords = (-15.904528, 34.891689)  # dorpje van Koen
	api_key = get_api_key('credentials.txt')
	google_maps_api = GoogleMapsAPI()
	map_image = google_maps_api.get_static_map_image(api_key=api_key, start_coords=start_coords, end_coords=end_coords,maptype="satellite")

	plt.imshow(map_image)
	plt.axis('off')
	plt.savefig("satellite_image.png")

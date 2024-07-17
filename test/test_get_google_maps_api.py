import pytest
from google_maps import GoogleMapsAPI
from image_handler import ImageHandler
from entrypoint import get_api_key


def test_get_google_maps_api_smoke_test():
	# start_coords = (52.5562125, 4.8469403)  # De Rijp
	# end_coords = (52.5550823, 4.8489198)
	start_coords = (-15.8034, 34.9511)  # Start coordinates (South-West Corner Blantyre)
	end_coords = (-15.6750, 35.1080)  # End coordinates (North-East Corner Blantyre)
	start_coords = (-15.899523, 34.888095) # dorpje van Koen
	end_coords = (-15.904528, 34.891689) # dorpje van Koen
	api_key=get_api_key('credentials.txt')
	google_maps_api = GoogleMapsAPI()
	image_handler = ImageHandler(start_coords=start_coords, end_coords=end_coords)
	map_image = google_maps_api.get_static_map_image(api_key=api_key, start_coords=start_coords, end_coords=end_coords,maptype="roadmap")
	import matplotlib.pyplot as plt
	plt.imshow(map_image)
	plt.axis('off')
	plt.savefig("map_image.png")
	image_handler.save_image(map_image=map_image, save_path="../images/map_image.png")
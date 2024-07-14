import requests
import math


class GoogleMapsAPI:
	def get_static_map_image(self, api_key, start_coords, end_coords, zoom=18):
		# Calculate the center point
		center_lat = (start_coords[0] + end_coords[0]) / 2
		center_lng = (start_coords[1] + end_coords[1]) / 2

		# Calculate the distance between the start and end coordinates to determine the image size
		def haversine(coord1, coord2):
			R = 6371  # Earth radius in km
			lat1, lng1 = coord1
			lat2, lng2 = coord2
			dlat = math.radians(lat2 - lat1)
			dlng = math.radians(lng2 - lng1)
			a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng/2) * math.sin(dlng/2)
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
			distance = R * c
			return distance

		distance = haversine(start_coords, end_coords)
		image_size = int(min(distance * 1000 / (2**zoom), 640))  # Convert to image size and cap at 640 (max for free tier)
		image_size=20000 # TODO fix why this image size becomes 0, is the maths in this function wrong?
		# Construct the URL for the static map API request
		url = (
			f"https://maps.googleapis.com/maps/api/staticmap?"
			f"center={center_lat},{center_lng}&"
			f"zoom={zoom}&"
			f"size={image_size}x{image_size}&"
			f"maptype=satellite&"
			f"key={api_key}"
		)

		response = requests.get(url)
		if response.status_code != 200:
			raise ValueError(f"Error: {response.status_code}, {response.text}")
		return response.content

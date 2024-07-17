import numpy as np

from google_maps import GoogleMapsAPI
from image_handler import ImageHandler
from house_detector import HouseDetector
from counter import ByPixelCounter



def main():
    start_coords = (-15.899523, 34.888095)
    end_coords = (-15.904528, 34.891689)
    maps_api = GoogleMapsAPI()
    counter = ByPixelCounter()
    api_key = get_api_key('credentials.txt')
    map_image = maps_api.get_static_map_image(api_key, start_coords, end_coords, maptype="roadmap", zoom=18)
    n_people = counter.count_people(map_image)
    print(f"{n_people} people live in this map area.")


def get_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.readline().strip()
    return api_key


if __name__ == '__main__':
    main()

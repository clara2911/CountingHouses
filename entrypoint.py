from google_maps import GoogleMapsAPI
from imagehandler import ImageHandler


def main():
    image_handler = ImageHandler()
    maps_api = GoogleMapsAPI()

    api_key = get_api_key('credentials.txt')
    start_coords = (-15.8034, 34.9511)  # Start coordinates (South-West Corner Blantyre)
    end_coords = (-15.6750, 35.1080)  # End coordinates (North-East Corner Blantyre)
    start_coords = (-14.0140, 33.7325)  # Start coordinates (South-West Corner Lilongwe)
    end_coords = (-13.9280, 33.8540)  # End coordinates (North-East Corner Lilongwe)

    map_image = maps_api.get_static_map_image(api_key, start_coords, end_coords)
    # image_handler.show_image(map_image=map_image) #TODO Still throws an error 'image with type... cannot be converted to float
    image_handler.save_image(map_image=map_image, start_coords=start_coords, end_coords=end_coords)


def get_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.readline().strip()
    return api_key


if __name__ == '__main__':
    main()

from google_maps import GoogleMapsAPI


def main():
    api_key = get_api_key('credentials.txt')
    start_coords = (-13.9626, 33.7741)  # Example start coordinates
    end_coords = (-13.9621, 33.7745)  # Example end coordinates
    maps_api = GoogleMapsAPI()
    map_image = maps_api.get_static_map_image(api_key, start_coords, end_coords)
    with open("satellite_image.png", "wb") as f:
        f.write(map_image)
    print("Satellite image saved as satellite_image.png")


def get_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.readline().strip()
    return api_key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



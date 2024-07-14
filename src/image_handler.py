import os
import matplotlib.pyplot as plt


class ImageHandler:

	def save_image(self, map_image, start_coords, end_coords):
		os.makedirs("images", exist_ok=True)
		image_filepath = os.path.join("images", f"satellite_image_{start_coords}_{end_coords}.png")
		with open(image_filepath, "wb") as f:
			f.write(map_image)
		print(f"Satellite image saved as {image_filepath}")

	def show_image(self, map_image):

		plt.imshow(map_image)
		plt.show()

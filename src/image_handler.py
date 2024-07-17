import os
import matplotlib.pyplot as plt
import cv2


class ImageHandler:
	def __init__(self, start_coords, end_coords):
		self.start_coords = start_coords
		self.end_coords = end_coords

	def save_image(self, map_image, save_path=None):
		if save_path is not None:
			image_filepath = save_path
		else:
			os.makedirs("images", exist_ok=True)
			image_filepath = os.path.join("images", f"satellite_image_{self.start_coords}_{self.end_coords}.png")
		cv2.imwrite(image_filepath, map_image)
		print(f"Satellite image saved as {image_filepath}")

	def show_image(self, map_image):
		plt.title(f"Satellite image of {self.start_coords} to {self.end_coords}")
		plt.imshow(map_image)
		plt.show()

	def save_and_show_detected_houses_image(self, image):
		# Save and display the result
		output_image_path = os.path.join('images', f'detected_houses_{self.start_coords}_{self.end_coords}.png')
		cv2.imwrite(output_image_path, image)
		print(f"Detected houses image saved as {output_image_path}")

		# Display the image with bounding boxes
		plt.figure(figsize=(10, 10))
		plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
		plt.axis('off')
		plt.show()

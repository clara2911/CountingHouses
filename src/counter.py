import numpy as np


class ByPixelCounter:

	def __init__(self):
		self.n_pixels_per_human = 20
		self.range = (92, 94)

	def count_people(self, image):
		pixel_matrix = np.array(image)
		# Define the RGB ranges

		# Check which pixels fall within the specified RGB ranges
		within_range = np.logical_and.reduce((
			pixel_matrix[:, :] >= self.range[0], pixel_matrix[:, :] <= self.range[1]
		))

		# Calculate the percentage of pixels within the range
		n_people = int(np.sum(within_range)/self.n_pixels_per_human)
		return n_people


class ByGreyBlobCounter:
	pass

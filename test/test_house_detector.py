import pytest
from house_detector import HouseDetector


def test_load_model_smoke_test():
	house_detector = HouseDetector()
	model = house_detector.load_model()
	assert model is not None
from house_detection.yolo_house_detector import YOLOHouseDetector


def test_load_model_smoke_test():
	house_detector = YOLOHouseDetector()
	model = house_detector.load_model()
	assert model is not None
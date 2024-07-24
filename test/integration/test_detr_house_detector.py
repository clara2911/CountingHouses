from input.google_maps import GoogleMapsAPI
from entrypoint import get_api_key
import matplotlib.pyplot as plt

from transformers import AutoImageProcessor


def test_huggingface_auth():
	checkpoint = "facebook/detr-resnet-50"
	AutoImageProcessor.from_pretrained(checkpoint)

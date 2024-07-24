from abc import ABC, abstractmethod


class HouseDetector(ABC):

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def detect_houses(self, model, image_path):
        pass

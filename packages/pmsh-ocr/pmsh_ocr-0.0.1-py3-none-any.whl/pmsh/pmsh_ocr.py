import os

from .detect import Detector
from .recognize import Recognizer

class PMSHOCR:
    def __init__(self, ratio_threshold=0.00001):
        self.detector = Detector(ratio_threshold)
        model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
        self.recognizer = Recognizer(model_dir)

    def inference(self, image, ref_text=None):
        box = self.detector.inference(image)
        if box is None:
            return None
        
        text_image = image[box[1]:box[3], box[0]:box[2]]
        result = self.recognizer.inference(text_image, ref_text)
        result['box'] = box
        return result

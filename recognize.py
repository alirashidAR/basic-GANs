import keras_ocr
import tensorflow
from process import image

pipe = keras_ocr.pipeline.Pipeline()

def recognize(image):
    predictions = pipe.recognize([image])
    return predictions
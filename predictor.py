import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from google.colab import drive
import PIL
import os
from transformers import ViTFeatureExtractor, ViTForImageClassification

class AgePredictor:
  def __init__(self):
    # Init model, transforms
    self.model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
    self.transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')

  def predict_age(self, img_path):
    # Get example image from official fairface repo + read it in as an image
    im = Image.open(img_path)

    # Transform our image and pass it through the model
    inputs = self.transforms(im, return_tensors='pt')
    output = self.model(**inputs)

    # Predicted Class probabilities
    proba = output.logits.softmax(1)

    # Predicted Classes
    preds = proba.argmax(1)

    #Label for Prediction
    return self.model.config.id2label[2]
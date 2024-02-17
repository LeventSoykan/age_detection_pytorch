from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

class AgePredictor:
    def __init__(self):
        # Init model, transforms
        self.model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
        self.transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')

    def predict_age(self, image):
        # Transform our image and pass it through the model
        inputs = self.transforms(image, return_tensors='pt')
        output = self.model(**inputs)

        # Predicted Class probabilities
        proba = output.logits.softmax(1)

        # Predicted Classes
        preds = proba.argmax(1)

        # Label for Prediction
        return self.model.config.id2label[preds.item()]


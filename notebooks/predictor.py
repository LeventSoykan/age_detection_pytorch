from PIL import Image
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

            # Label for Prediction
            return self.model.config.id2label[preds.item()]

    if __name__ == '__main__':
        predictor = AgePredictor()
        print(predictor.predict_age('data/0-2/1_0_0_20161219204512212.jpg'))


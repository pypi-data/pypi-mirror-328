import os
import requests
from .train import train_text_classifier
from .model_utils import load_trained_model

API_BASE = "https://classify.ngmkt.site/api"

class TextClassifier:
    def __init__(self, labels, api_key, model_name="facebook/bart-large-mnli"):
        """
        Initialize the TextClassifier.

        Args:
        - labels (list): A list of labels for classification.
        - api_key (str): API key for authentication.
        - model_name (str): Pretrained model name.
        """
        self.labels = labels
        self.api_key = api_key
        self.model_name = model_name
        self.model, self.tokenizer = load_trained_model(model_name, len(labels))

        # Verify API Key
        if not self._validate_api_key():
            raise ValueError("Invalid API Key. Please check your subscription.")

    def _validate_api_key(self):
        """Check if the API key is valid."""
        response = requests.post(f"{API_BASE}/validate-key", json={"api_key": self.api_key})
        return response.json().get("valid", False)

    def _log_usage(self, text, prediction):
        """Log usage data to the API."""
        data = {
            "api_key": self.api_key,
            "text": text,
            "prediction": prediction
        }
        requests.post(f"{API_BASE}/log", json=data)

    def train(self, train_file, test_file, output_dir="./model_output"):
        """Train the model locally."""
        train_text_classifier(self.labels, train_file, test_file, self.model_name, output_dir)

    def predict(self, text):
        """Predict the label for a given text."""
        # Check if user exceeded their quota
        response = requests.post(f"{API_BASE}/check-usage", json={"api_key": self.api_key})
        if not response.json().get("allowed", True):
            raise ValueError("API call limit reached. Upgrade your plan.")

        # Run Prediction
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        prediction = outputs.logits.argmax(dim=-1).item()
        label = self.labels[prediction]

        # Log this request
        self._log_usage(text, label)

        return label

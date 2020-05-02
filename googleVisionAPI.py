import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def search_labels(image_address):
    # Instantiates a client
    credentials = service_account.Credentials.from_service_account_file(
        "/Users/bluish/Documents/credentials/google-api.json")
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # The name of the image file to annotate
    file_name = image_address
        # os.path.join(os.path.dirname(__file__), 'resources/oreo-cake.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    unwanted_labels = ['Food', 'Cuisine', 'Ingredient', 'Dish', 'Dessert']
    for label in labels:
        print(label.description)
        if label.description not in unwanted_labels:
            return label.description
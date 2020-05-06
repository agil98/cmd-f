import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def search_labels(location, image_address):
    # Instantiates a client
    credentials = service_account.Credentials.from_service_account_file(
        "/Users/bluish/Documents/credentials/google-api.json")
    client = vision.ImageAnnotatorClient(credentials=credentials)

    if location == 'local':
        # The name of the image file to annotate
        file_name = image_address

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
    else:
        print('online')
        image = vision.types.Image()
        image.source.image_uri = image_address

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    res = 0
    intial_catergory = ['Food', 'Cuisine', 'Ingredient', 'Dish']
    for label in labels:
        print(label.description)
        if label.description in intial_catergory:
            res = 1102

    if res is 1102:
        unwanted_labels = ['Food', 'Cuisine', 'Ingredient', 'Dish', 'Dessert', 'Pizza', 'Meat', 'Meal', 'Recipe', 'Produce']
        for label in labels:
            print(label.description)
            if label.description not in unwanted_labels:
                return label.description
    else:
        return "not food"

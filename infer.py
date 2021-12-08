# Gradient Deployments: Fashion-MNIST Example
#
# This is part of our basic deployments example (https://github.com/gradient-ai/Deployments) that shows
#
# 1: Create and train a TensorFlow deep learning model using Workflows
# 2: Deploy the model using Deployments
# 3: Send inference data to the model and receive correct output
#
# This script is part of step 3 and is called from the Workflow. It sends inference data to tthe model.
# It is based on content from our Workflows tutorial at https://github.com/gradient-ai/fashionmnist
#
# Last updated: Dec 07th 2021

from tensorflow import keras
import numpy as np
import os
import json
import requests

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

test_images = test_images / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

SERVE_URL = os.getenv("SERVE_URL")

data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:5].tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post(SERVE_URL, data=data, headers=headers)

print (json_response.text)
predictions = json.loads(json_response.text)['predictions']

for i in range(0,5):
  print('\nThe model predicted this as a {}, and it was actually a {}'.format(class_names[np.argmax(predictions[i])], class_names[test_labels[i]]))

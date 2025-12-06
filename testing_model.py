import cv2
import numpy as np
from keras.models import load_model
import os

# Load trained model
model = load_model("Skin_Disease_Detection_Model.h5")

# Path to your test image
image_path = r"E:\project\DermalScan-AI\test2.jpg"

# Validate file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"❌ Image not found: {image_path}")

# Load and preprocess the image
img = cv2.imread(image_path)
img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Labels (order must match model training)
class_names = ["Wrinkles", "Darkspots", "Clearskin", "Puffyeyes"]

# Predict
prediction = model.predict(img)
label = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print("\n=========================")
print(f" Predicted Class: {label}")
print(f" Confidence: {confidence:.2f}%")
print("=========================")

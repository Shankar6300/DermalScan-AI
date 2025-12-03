import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Path to dataset
DATASET_PATH = "dataset"

# Categories inside dataset folder
CATEGORIES = ["Wrinkles", "Darkspots", "Clearskin", "Puffyeyes"]

# Target number of images per category
TARGET_COUNT = 500

# Augmentation generator
datagen = ImageDataGenerator(
    rotation_range=25,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    brightness_range=[0.7, 1.3],
    fill_mode="nearest"
)

# Function to load and resize an image
def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    return img

print("\n===== BALANCING DATASET =====\n")

for category in CATEGORIES:
    folder = os.path.join(DATASET_PATH, category)

    # List all valid image files
    images = [
        f for f in os.listdir(folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    current_count = len(images)
    print(f"{category}: {current_count} images")

    if current_count >= TARGET_COUNT:
        print(f"✔ {category} already balanced. Skipping.\n")
        continue

    # Number of new images required
    needed = TARGET_COUNT - current_count
    print(f"→ Need {needed} more images. Augmenting...")

    save_count = 0

    # Loop through existing images and generate augmented images
    for img_name in images:
        img_path = os.path.join(folder, img_name)
        img = load_image(img_path)

        aug_iter = datagen.flow(img, batch_size=1)

        for i in range(10):  # 10 aug images per original
            if save_count >= needed:
                break

            aug_img = next(aug_iter)[0]
            save_path = os.path.join(folder, f"aug_{img_name}_{i}.jpg")
            cv2.imwrite(save_path, cv2.cvtColor(aug_img, cv2.COLOR_RGB2BGR))
            save_count += 1

        if save_count >= needed:
            break

    print(f"✔ {category} balanced: {TARGET_COUNT} images\n")

print("\n===== ALL CATEGORIES BALANCED SUCCESSFULLY =====")

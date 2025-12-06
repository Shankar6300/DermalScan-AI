import os
import shutil
import random

source = "Dataset"
dest = "Skin_Dataset_Split"

folders = ["Wrinkles", "Darkspots", "Clearskin", "Puffyeyes"]
splits = ["train", "val", "test"]

# Create folders
for split in splits:
    for folder in folders:
        os.makedirs(os.path.join(dest, split, folder), exist_ok=True)

# Split files
for folder in folders:
    files = [
        f for f in os.listdir(os.path.join(source, folder))
        if f.lower().endswith((".jpg", ".png", ".jpeg"))
    ]

    random.shuffle(files)

    train_end = int(0.7 * len(files))
    val_end = int(0.9 * len(files))

    for i, file in enumerate(files):
        src_path = os.path.join(source, folder, file)

        if i < train_end:
            dst = os.path.join(dest, "train", folder)
        elif i < val_end:
            dst = os.path.join(dest, "val", folder)
        else:
            dst = os.path.join(dest, "test", folder)

        shutil.copy(src_path, os.path.join(dst, file))

print("\n📌 Dataset successfully split into Train, Validation, Test!")

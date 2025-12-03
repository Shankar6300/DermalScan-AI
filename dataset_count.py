import os

base_path = "Dataset"

folders = ["Wrinkles", "Darkspots", "Clearskin", "Puffyeyes"]

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    count = len([f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".png", ".jpeg"))])
    print(f"{folder}: {count} images")

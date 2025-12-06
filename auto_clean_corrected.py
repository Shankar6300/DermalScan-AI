import cv2
import os

DATASET_PATH = "Dataset"  # Corrected to match the actual folder name (capital D)
CATEGORIES = ["Wrinkles", "Darkspots", "Clearskin", "Puffyeyes"]

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def is_face_present(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return False
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    return len(faces) > 0

def clean_dataset():
    for category in CATEGORIES:
        folder = os.path.join(DATASET_PATH, category)
        if not os.path.exists(folder):
            print(f"Folder not found: {folder}")
            continue
        files = os.listdir(folder)

        print(f"\nChecking: {category}")

        for f in files:
            path = os.path.join(folder, f)

            # remove corrupt / unreadable images
            img = cv2.imread(path)
            if img is None:
                print(f"Removed (corrupt): {path}")
                os.remove(path)
                continue

            # remove tiny images
            if img.shape[0] < 100 or img.shape[1] < 100:
                print(f"Removed (too small): {path}")
                os.remove(path)
                continue

            # remove images with no face detected
            if not is_face_present(path):
                print(f"Removed (no face): {path}")
                os.remove(path)
                continue

clean_dataset()
print("\nCleaning complete.")

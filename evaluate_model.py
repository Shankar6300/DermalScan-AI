import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

# Load model
model = tf.keras.models.load_model("Skin_Disease_Detection_Model.h5")

# Required variables
img_size = (224, 224)
batch_size = 32

# Validation/Test Image Generator
datagen_val = ImageDataGenerator(rescale=1/255)

# Load Test Dataset
test_data = datagen_val.flow_from_directory(
    "Skin_Dataset_Split/test",
    target_size=img_size,
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=False
)

# Evaluate the model
loss, accuracy = model.evaluate(test_data)
print(f"\n📌 Model Accuracy on Test Data: {accuracy * 100:.2f}%")
print(f"📌 Model Loss: {loss:.4f}")

# Optional: Predict on batch
predictions = model.predict(test_data)
print("\nSample Predictions Ready")

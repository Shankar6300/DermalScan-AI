from keras.preprocessing.image import ImageDataGenerator

img_size = (224, 224)
batch_size = 32

datagen_train = ImageDataGenerator(rescale=1/255)
datagen_val = ImageDataGenerator(rescale=1/255)

train_data = datagen_train.flow_from_directory(
    "Skin_Dataset_Split/train",
    target_size=img_size,
    batch_size=batch_size,
    class_mode="categorical"
)

val_data = datagen_val.flow_from_directory(
    "Skin_Dataset_Split/val",
    target_size=img_size,
    batch_size=batch_size,
    class_mode="categorical"
)

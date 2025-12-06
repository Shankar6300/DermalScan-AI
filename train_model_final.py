from build_model import model
from load_data import train_data, val_data

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=20
)

model.save("Skin_Disease_Detection_Model.h5")

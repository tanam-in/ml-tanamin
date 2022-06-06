from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

BUCKET_NAME = "tanamin_model"
category=["Bean", "Bitter_Gourd", "Broccoli", "Cabbage", "Capsicum", "Carrot", "Cauliflower", "Cucumber", "Papaya", "Potato", "Pumpkin", "Tomato"]

model = None

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def deteksi(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/model_Xception_13Classes.h5",
            "/tmp/model_Xception_13Classes.h5",
        )
        model = tf.keras.models.load_model("/tmp/model_Xception_13Classes.h5") #load model

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((224, 224)) 
    )

    image = image/255 
    
    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    # New Update here
    counter = 0
    for values in predictions:
        for value in values:
            if value > 0.90:
                counter = 1
    
    if counter == 1:
        index = category.index(predicted_category)
        predicted_category = category[np.argmax(predictions[0])]
        accuracy = predictions[0][index]

        return {"id": index, "name": predicted_category, "accuracy" : accuracy}
    else:
        return None

    



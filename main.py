import requests
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from google.cloud import storage
import numpy as np
import json

# ini aku gatau gimana cara dapetin datanya nanti
# download path model here : https://drive.google.com/file/d/1fv66TZQZGOWYeky2Lr3DnLu596ARvY_x/view?usp=sharing
# rubah atau tambahin bagian requestnya data dan lainnya (kurang mengerti)


path_to_model='./model_Xception_13Classes.h5' # Path model tempat simpan model
model = load_model(path_to_model) # Load Model
file = './browkoli.jpg' # Lokasi file yang akan dideteksi

category={
    0: 'Bean', 
    1: 'Bitter_Gourd', 
    2: "Broccoli", 
    3: 'Cabbage', 
    4: 'Capsicum', 
    5: 'Carrot', 
    6: 'Cauliflower',
    7: 'Cucumber', 
    8: 'Papaya', 
    9: 'Potato', 
    10: 'Pumpkin', 
    11: "Tomato"
}

def predict_image(filename,model):
    img_ = image.load_img(filename, target_size=(224, 224))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0) 
    img_processed /= 255.   
    
    prediction = model.predict(img_processed)
    index = np.argmax(prediction)
    
    name_class = category[index]

    value = {
        'id' : int(index),
        'name' : name_class
    }

    return json.dumps(value)

predict_image(file,model)
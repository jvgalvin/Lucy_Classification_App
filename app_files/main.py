import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def getPrediction(filename):

    model = load_model("/Users/johngalvin/Desktop/GitHub/Tensorflow/workspace/Lucy-Classification/models/model.h5")
    image = load_img('/Users/johngalvin/Desktop/GitHub/Tensorflow/workspace/Lucy-Classification/uploads/'+filename, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    pred = model.predict(image)
    if pred[0][0] > pred[0][1]:
        label = ("lucy", pred[0][0])
    else:
        label = ("another frenchie", pred[0][1])

    return (label[0], label[1]*100)
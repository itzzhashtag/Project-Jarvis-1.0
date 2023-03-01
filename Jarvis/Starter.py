from Brain import Reply
from time import sleep
from Listen import Listen
from Speak import Speak
from tkinter import messagebox 

def Test():
    import tensorflow as tf
    from tensorflow import keras
    mnist = tf.keras.datasets.fashion_mnist
    (trainings_modules,trainings_labels),(tast_images,test_lables)=mnist.load_data()
    model=tf.keras.models.Sequential([tf.keras.layers.Flatten(),tf.keras.layers.Dense(128,activation=tf.nn.softmax)])
    model.compile(optimizer=tf.optimizers.Adam(),loss='sparse_categorial_crossentropy',metrics=['accuracy'])

def Start():
    
    query=Listen()
    reply=Reply(query)
    Speak(reply)
    messagebox.showinfo("JarvisOS",reply)
while True:
    Start()
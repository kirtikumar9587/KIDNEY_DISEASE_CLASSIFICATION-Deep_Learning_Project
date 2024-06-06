#from tf download vgg16 model
#4.create component
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf 
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

#define class prepareBseModel

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    #
    #this will download vgG16 from the tf #get input shape from params #
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

#also save this model after it is saved
        self.save_model(path=self.config.base_model_path, model=self.model)

   #this is another static model that is _prepare_full_model

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        #after that flatten the layer and then create a custom dense layer
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        #this is full model where input os model.input and output is prediction
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        #configure model for the training
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        #at end returning full model
        full_model.summary()
        return full_model
    
    #this full model also need to save in this call prepare base full modeland giving paramter and save it.
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
 #this is static function nad save model operation

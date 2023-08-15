'''

Contains the indiviual image feature network and audio feature network.

'''

# create the individual networks for image and audio to get the feature encodings
def image_feat_network(input_dim_img):

  base_model = tf.keras.applications.VGG16(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')

  base_model.trainable = False

  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Input(shape=IMG_SHAPE))
  
  model.add(base_model)
  model.add(tf.keras.layers.Flatten())

  model.add(tf.keras.layers.Dense(128, activation='relu',kernel_regularizer='l2'))
  model.add(tf.keras.layers.Dropout(0.5))

  model.add(tf.keras.layers.Dense(N_CLASSES, activation='softmax'))

  return model

def audio_feat_network(input_dim_aud):

  IMAGE_HEIGHT , IMAGE_WIDTH , N_CHANNELS = input_dim_aud # input shape

  model = tf.keras.models.Sequential()

  model.add(tf.keras.layers.Input(shape=(IMAGE_HEIGHT ,IMAGE_WIDTH, N_CHANNELS)))
  model.add(tf.keras.layers.Conv2D(32, 3, strides=2, padding='same', activation='relu'))

  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
  model.add(tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'))

  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
  model.add(tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'))

  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
  model.add(tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'))

  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

  (x,y,z,w) = model.output_shape
  model.add(Reshape((y*z,w),input_shape=(-1,y,z,w)))

  model.add(Bidirectional(LSTM(20, return_sequences=True),input_shape=(-1,y*z,w)))
  model.add(tf.keras.layers.Flatten())
  
  model.add(tf.keras.layers.Dense(256, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.3))

  model.add(tf.keras.layers.Dense(128, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.3))
  
  model.add(tf.keras.layers.Dense(32, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.3))

  model.add(tf.keras.layers.Dense(N_CLASSES, activation='softmax'))
  model.summary()
  
  return model

def multimodal_network(input_dim):

  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Input(shape = input_dim))

  model.add(tf.keras.layers.Dense(128 , activation = 'relu'))
  model.add(tf.keras.layers.Dense(64 , activation = 'relu'))
  model.add(tf.keras.layers.Dense(32 , activation = 'relu'))

  return model
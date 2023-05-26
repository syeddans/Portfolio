import tensorflow as tf
import segmentation_models as sm
import glob
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


# BACKBONE = 'resnet34'
# preprocess_input = sm.get_preprocessing(BACKBONE)
# images_path = "C:/Users/syeddans/Desktop/Training/image"
# masks_path = "C:/Users/syeddans/Desktop/Training/label"

SIZE_X = 256 #Resize images (height  = X, width = Y)
SIZE_Y = 256

# train_images = []
# for directory_path in glob.glob(images_path):
#     for img_path in glob.glob(os.path.join(directory_path, "*.tif")):
#         img = cv2.imread(img_path, cv2.IMREAD_COLOR)
#         img = cv2.resize(img, (SIZE_Y, SIZE_X))
#         train_images.append(img)
#         #train_labels.append(label)
# #Convert list to array for machine learning processing
# train_images = np.array(train_images)
# print(train_images)
#
# #Capture mask/label info as a list
# train_masks = []
# for directory_path in glob.glob(masks_path):
#     for mask_path in glob.glob(os.path.join(directory_path, "*.tif")):
#         mask = cv2.imread(mask_path, 0)
#         mask = cv2.resize(mask, (SIZE_Y, SIZE_X))
#         train_masks.append(mask)
#         #train_labels.append(label)
# #Convert list to array for machine learning processing
# train_masks = np.array(train_masks)
#
# X = train_images
# Y = train_masks
# Y = np.expand_dims(Y, axis=3)
#
# from sklearn.model_selection import train_test_split
# x_train, x_val, y_train, y_val = train_test_split(X, Y, test_size=0.2, random_state=42)
#
# # preprocess input
# x_train = preprocess_input(x_train)
# x_val = preprocess_input(x_val)
#
# # define model
# model = sm.Unet(BACKBONE, encoder_weights='imagenet')
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['mse'])
#
# print(model.summary())
#
# history=model.fit(x_train,
#           y_train,
#           batch_size=8,
#           epochs=400,
#           verbose=1,
#           validation_data=(x_val, y_val))
#
# #accuracy = model.evaluate(x_val, y_val)
# #plot the training and validation accuracy and loss at each epoch
# loss = history.history['loss']
# val_loss = history.history['val_loss']
# epochs = range(1, len(loss) + 1)
# plt.plot(epochs, loss, 'y', label='Training loss')
# plt.plot(epochs, val_loss, 'r', label='Validation loss')
# plt.title('Training and validation loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()
#
# model.save('unet.h5')

from tensorflow import keras
model = keras.models.load_model('unet.h5', compile=False)
#Test on a different image
#READ EXTERNAL IMAGE...
test_img = cv2.imread('1.100164.jpg', cv2.IMREAD_COLOR)
test_img = cv2.resize(test_img, (SIZE_Y, SIZE_X))
test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2BGR)
test_img = np.expand_dims(test_img, axis=0)

prediction = model.predict(test_img)

#View and Save segmented image
prediction_image = prediction.reshape(256,256,1)
plt.imshow(prediction_image, cmap='gray')
plt.show()
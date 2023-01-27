#!/usr/bin/env python
# coding: utf-8

# In[23]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# In[24]:


(xTrain, yTrain), (xTest, yTest) = tf.keras.datasets.fashion_mnist.load_data()
print("xTrain shape: ", xTrain.shape, "yTrain shape: ", yTrain.shape)


# In[25]:


plt.imshow(xTrain[6000])


# In[26]:


#normalize data
xTrain = xTrain.astype('float32') / 255
xTest = xTest.astype('float32') / 255


# In[27]:


#Split into training and validation sets
(xTrain, xValid) = xTrain[5000:], xTrain[:5000]
(yTrain, yValid) = yTrain[5000:], yTrain[:5000]


# In[28]:


#Reshape the input from (28, 28) to (28, 28, 1)
w, h = 28, 28
xTrain = xTrain.reshape(xTrain.shape[0], w, h, 1)
print(xTrain.shape)
xValid = xValid.reshape(xValid.shape[0], w, h, 1)
xTest = xTest.reshape(xTest.shape[0], w, h, 1)


# In[29]:


#One-hot endcode the labels
#There are 10 different categories
yTrain = tf.keras.utils.to_categorical(yTrain, 10)
yValid = tf.keras.utils.to_categorical(yValid, 10)
yTest = tf.keras.utils.to_categorical(yTest, 10)


# In[30]:


#Create model
model = tf.keras.Sequential()

#Get input shape in first layer of the NN
model.add(tf.keras.layers.Conv2D(filters = 64, kernel_size = 2, padding = 'same', activation = 'relu', input_shape = (28, 28, 1)))
#Adding a stride length of 1 to maxpool layers helps!
model.add(tf.keras.layers.MaxPooling2D(pool_size=2, strides = 1))
model.add(tf.keras.layers.Dropout(0.3))
#Second layer
model.add(tf.keras.layers.Conv2D(filters = 32, kernel_size = 2, padding = 'same', activation = 'relu'))
#Adding a stride length of 1 to maxpool layers helps!
model.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides = 1))
model.add(tf.keras.layers.Dropout(0.3))
#Add third layer -- attempt to get test accuracy above 92% (right now at 91%) -- accuracy down to 88%
'''
model.add(tf.keras.layers.Conv2D(filters = 16, kernel_size = 2, padding = 'same', activation = 'relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size = 2))
model.add(tf.keras.layers.Dropout(0.3))
'''
#Output layer
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation = 'softmax'))


# In[31]:


#Summary
model.summary()


# In[32]:


#Compile model
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


# In[33]:


from keras.callbacks import ModelCheckpoint
checkpointer = ModelCheckpoint(filepath = 'model.weights.best.hdf5', verbose = 1, save_best_only = True)
#Train the model
model.fit(xTrain, yTrain, batch_size = 64, epochs = 10, validation_data = (xValid, yValid), callbacks = [checkpointer])


# In[34]:


#Load model with best validation accuracy
model.load_weights("model.weights.best.hdf5")
#Test accuracy
score = model.evaluate(xTest, yTest, verbose = 0)
print('\n', 'Test accuracy: ', score[1])


# In[35]:


# ## 2. Representing a Convolutional NN as a Fully-Connected NN
'''
Implement!
• Convolution layer with 64 filters, each 3x3, stride of 1 (i.e., apply the filter at all pixel locations),
no padding.
• Max pool with a pooling width of 2x2, stride of 2, no padding.
• ReLU.
• Flatten the 64 feature maps into one long vector.
• Fully-connected layer to map into a 1024-dimensional vector.
• ReLU.
• Fully-connected layer to map into a 10-dimensional vector.
• Softmax.
'''

model_p2 = tf.keras.Sequential()

#Get input shape in first layer of the NN
model_p2.add(tf.keras.layers.Conv2D(filters = 64, kernel_size = 3, strides = 1, padding = 'valid', input_shape = (28, 28, 1)))
model_p2.add(tf.keras.layers.MaxPooling2D(pool_size=2, strides = 2, padding = 'valid'))
model_p2.add(tf.keras.layers.ReLU())
model_p2.add(tf.keras.layers.Flatten())
model_p2.add(tf.keras.layers.Dense(1024))
model_p2.add(tf.keras.layers.ReLU())
model_p2.add(tf.keras.layers.Dense(10))
model_p2.add(tf.keras.layers.Softmax())

#Summary
model_p2.summary()


# In[48]:


#Compile model
model_p2.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

from keras.callbacks import ModelCheckpoint
checkpointer = ModelCheckpoint(filepath = 'model_p2.weights.best.hd5', verbose = 1, save_best_only = True)
#Train the model
model_p2.fit(xTrain, yTrain, batch_size = 64, epochs = 5, validation_data = (xValid, yValid), callbacks = [checkpointer])


# In[51]:


model_p2.load_weights('model_p2.weights.best.hd5')

model_p2.trainable_variables


# In[50]:


#Test accuracy
score = model_p2.evaluate(xTest, yTest, verbose = 0)
print('\n', 'Test accuracy: ', score[1])


# In[53]:


# predicting 1 random sample test data to compare later with numpy forward propagation
yhat1 = model_p2.predict(xTest[998:999,:,:,:])[0]
print(yhat1)


# In[17]:


# Define the text labels
fashion_mnist_labels = ["T-shirt/top",  # index 0
                        "Trouser",      # index 1
                        "Pullover",     # index 2 
                        "Dress",        # index 3 
                        "Coat",         # index 4
                        "Sandal",       # index 5
                        "Shirt",        # index 6 
                        "Sneaker",      # index 7 
                        "Bag",          # index 8 
                        "Ankle boot"]   # index 9


# In[18]:


# Plot a random sample of 10 test images, their predicted labels and ground truth
figure = plt.figure(figsize=(20, 8))
for i, index in enumerate(np.random.choice(xTest.shape[0], size=15, replace=False)):
    ax = figure.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    # Display each image
    ax.imshow(np.squeeze(xTest[index]))
    predict_index = np.argmax(yhat[index])
    true_index = np.argmax(yhat[index])
    # Set the title for each image
    ax.set_title("{} ({})".format(fashion_mnist_labels[predict_index], 
                                  fashion_mnist_labels[true_index]),
                                  color=("green" if predict_index == true_index else "red"))


# In[54]:


'''
2. Extract the weights from the model after training it. See model.summary() and model.trainable variables,
where model is the TensorFlow model you trained.
'''
for layer in range(len(model_p2.layers)):
    print("layer", [layer], "weights", model_p2.layers[layer].weights)
    # model_p2.layers[layer].weights
    
# print("layer 1 weights", model_p2.layers[0].weights)
# print("layer 2 weights", model_p2.layers[1].weights)
# print("layer 3 weights", model_p2.layers[2].weights)



# In[55]:


def extract_w_b(model):
    # Extract W1, b1, W2, b2, W3, b3 from model.

    img_sz = 28
    filter_sz = 3
    channels = 64
    W1 = np.zeros((channels*(img_sz-2)*(img_sz-2), img_sz*img_sz))
    b1 = np.zeros((channels*(img_sz-2)*(img_sz-2)))
    start = 0
    convolution_weights = np.array(model_p2.get_weights()[0]) # 3x3x1x64
    convolution_bias = np.array(model.get_weights()[1]) # 64x1
    for rows in range(img_sz-2):
        for column in range(img_sz-2):
            for filter in range(channels):
                for depth in range(filter_sz):
                    start_ind = (rows + depth)*img_sz + column
                    stop_ind = start_ind + filter_sz
                    W1[start, start_ind:stop_ind] = convolution_weights[depth,:,0,filter]
                    b1[start] = convolution_bias[filter]
                start = start + 1

    b1 = np.atleast_2d(b1).T
    W2 = model.get_weights()[2].T
    b2 = np.atleast_2d(model.get_weights()[3]).T
    W3 = model.get_weights()[4].T
    b3 = np.atleast_2d(model.get_weights()[5]).T
    
    return W1, b1, W2, b2, W3, b3
    


# In[56]:


extract_w_b(model_p2)


# In[57]:


def fully_connected(W, b, x):
    h = np.dot(W,x)+b
    return h


# In[58]:


def max_pooling(x, poolingWidth):
    M, N, P = x.shape
  
    K = poolingWidth[0]
    L = poolingWidth[1]

    MK = M // K
    NL = N // L
    return (x[:MK*K, :NL*L, ...].reshape((MK, K, NL, L) + x.shape[2:]).max(axis=(1, 3)))


# In[59]:


def softmax(x):
    num = np.exp(x - np.max(x))
    deno = np.sum(num)
    y_hat = (num/(deno))
    return y_hat


# In[60]:


def relu(x):
    return np.maximum(x,0)


# In[61]:


def accuracy(y,y_hat):
    #print("this is y",y.shape)
    #print("this is yhat", yhat.shape)
    y = np.atleast_2d(np.argmax(y,axis=0)).T
    y_hat = np.atleast_2d(np.argmax(y_hat,axis=0)).T
    accu = 100*np.sum(np.equal(y,y_hat))/y.shape[0]
    return accu


# In[63]:


W1, b1, W2, b2, W3, b3 = extract_w_b(model_p2)
dim = np.reshape(xTest[998],(-1,1))
h1 = fully_connected(W1, b1, dim)
#print("H1 :", h1.shape)
h10 = h1.reshape(26,26,64)
h11 = max_pooling(h10, poolingWidth=(2,2))
#print("After MaxPooling :", h11.shape)
h12 = relu(h11)
#print("1st ReLU:", h12.shape)
h13 = np.atleast_2d(h12.flatten()).T
#print("After Flattening :", h13.shape)
h2 = fully_connected(W2, b2, h13)
#print("Dense_1 :", h2.shape)
h21 = relu(h2)
#print("2nd ReLU :", h21.shape)
h3 = fully_connected (W3, b3, h21)
#print("Dense_2 :", h3.shape)


# In[64]:


# Working on the same test data xTest[998]

yhat = softmax(h3)
#print(yhat.Shape) 
yhat2 = yhat
yhat2 = yhat.reshape(-1)
print(yhat2)


# In[66]:


print("This is from Tensorflow Model",yhat1)
print("This is from Numpy Model", yhat2)

print("This value shows similarity between two layers",accuracy(yhat2,yhat1))


# In[68]:


plt.plot(yhat1, linewidth=10)
plt.plot(yhat2, linewidth=3)
plt.show()


# In[ ]:





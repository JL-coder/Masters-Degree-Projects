import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from cmath import inf
import scipy.optimize

# For this assignment, assume that every hidden layer has the same number of neurons.

NUM_HIDDEN_LAYERS = 3
NUM_INPUT = 784
NUM_HIDDEN = 10
NUM_OUTPUT = 10


def softmax(z):
    nn = np.exp(z)
    dd = np.sum(nn, axis=0, keepdims=True)
    outZ=nn/dd
    return outZ

def relu(input):
    relu = input.copy()
    relu[relu < 0] = 0
    return relu

def relu_diff(input):
    #below 0 it is 0
    Relu_diff = input.copy()
    Relu_diff[Relu_diff <= 0] = 0
    # Relu_diff[Relu_diff < 0] = 0
    Relu_diff[Relu_diff > 0] = 1
    # Relu_diff[Relu_diff >= 0] = 1
    return Relu_diff


# Unpack a list of weights and biases into their individual np.arrays.
def unpack(weightsAndBiases, hidden_num, H_Layers):
    Ws = []
    start = 0
    end = NUM_INPUT * hidden_num
    W = weightsAndBiases[start:end]
    Ws.append(W)

    for i in range(H_Layers - 1):
        start = end
        end = end + hidden_num * hidden_num
        W = weightsAndBiases[start:end]
        Ws.append(W)

    start = end
    end = end + hidden_num * NUM_OUTPUT
    W = weightsAndBiases[start:end]
    Ws.append(W)

    Ws[0] = Ws[0].reshape(hidden_num, NUM_INPUT)
    for i in range(1, H_Layers):
        # Convert from vectors into matrices
        Ws[i] = Ws[i].reshape(hidden_num, hidden_num)
    Ws[-1] = Ws[-1].reshape(NUM_OUTPUT, hidden_num)

    # Bias terms
    bs = []
    start = end
    end = end + hidden_num
    b = weightsAndBiases[start:end]
    bs.append(b)

    for i in range(H_Layers - 1):
        start = end
        end = end + hidden_num
        b = weightsAndBiases[start:end]
        bs.append(b)

    start = end
    end = end + NUM_OUTPUT
    b = weightsAndBiases[start:end]
    bs.append(b)

    return Ws, bs


def forward_prop(X, Y, weightsAndBiases, hidden_num, H_Layers):
    HH = []
    ZZ = []


    Ws, bs = unpack(weightsAndBiases, hidden_num, H_Layers)
    h = X   #for first layer
    
 
    for i in range(H_Layers):

        b=bs[i].reshape(-1, 1)
        Z = np.dot(Ws[i], h) + b
        ZZ.append(Z)
        #pass z to h
        h = relu(Z)
        HH.append(h)

    bl= bs[-1].reshape(-1, 1)
    zz = np.dot(Ws[-1], HH[-1]) + bl
    ZZ.append(zz)

    # soft = np.exp(z)
    # hard = np.sum(soft, axis=0, keepdims=True)
    # outZ=soft/hard


    yhat = softmax(zz)
    # loss = np.mean(np.log(yhat) * Y)
    # print(loss)

    loss = np.sum(np.log(yhat) * Y)

    loss = (-1/Y.shape[1]) * loss

    # Return loss, pre-activations, post-activations, and predictions
    return loss, ZZ, HH, yhat


def back_prop(X, Y, weightsAndBiases, hidden_num, H_Layers):
    loss, zs, hs, yhat = forward_prop(X, Y, weightsAndBiases, hidden_num, H_Layers)
    dJdWs = []  # Gradients w.r.t. weights
    dJdbs = []  # Gradients w.r.t. biases

    
    Ws, bs = unpack(weightsAndBiases, hidden_num, H_Layers)
    # print("Ws[0].shape,Ws[1].shape,Ws[2].shape,Ws[3].shape",Ws[0].shape,Ws[1].shape,Ws[2].shape,Ws[3].shape)
    # Ws[0].shape,Ws[1].shape,Ws[2].shape,Ws[3].shape (10, 784) (10, 10) (10, 10) (10, 10)
    # print("bs[0].shape,bs[1].shape,bs[2].shape,bs[3].shape",bs[0].shape,bs[1].shape,bs[2].shape,bs[3].shape)
    # bs[0].shape,bs[1].shape,bs[2].shape,bs[3].shape (10,) (10,) (10,) (10,)
    G = yhat - Y
    # print("g.shape",g.shape)
    # g.shape (10, 16)


    for i in range(H_Layers, -1, -1):

         # For grads of b 

        if i != H_Layers:               #at last layer G =Yhat-Y
            dhdzs = relu_diff(zs[i])
            G = dhdzs * G

        djdb_term = np.sum(G, axis=1) / Y.shape[1]
        dJdbs.append(djdb_term)

        # For grads of W 

        if i == 0:
            fst_layer=np.dot(G, X.T) / Y.shape[1]  #at first layer we multiply with input values X 
            dJdWs.append(fst_layer)
            
        else:
            dJdWs.append(np.dot(G, hs[i - 1].T) / Y.shape[1])    #G term multipled with privious term h thats why i-1  
     
        G = np.dot(Ws[i].T, G)  #updated G for next layer
    
    # print("dJdbs  dJdWs",dJdbs,dJdWs)
    # print("dJdbs  dJdWs",dJdbs[0].shape,dJdWs[0].shape)
    # dJdbs  dJdWs (10,) (10, 10)
    # print("dJdbs  dJdWs",dJdbs[1].shape,dJdWs[1].shape)
    # dJdbs  dJdWs (10,) (10, 10)
    # print("dJdbs  dJdWs",dJdbs[2].shape,dJdWs[2].shape)
    # dJdbs  dJdWs (10,) (10, 10)
    # print("dJdbs  dJdWs",dJdbs[3].shape,dJdWs[3].shape)
    # dJdbs  dJdWs (10,) (10, 784)
    # print("dJdbs.shape  dJdWs.shape",len(dJdbs),len(dJdWs))
    # dJdbs.shape  dJdWs.shape 4 4

    dJdbs.reverse() #Generated list is from last layer to first layer 
    dJdWs.reverse() #reverse to makes it first to end layer
    # Concatenate gradients
    return np.hstack([dJdW.flatten() for dJdW in dJdWs] + [dJdb.flatten() for dJdb in dJdbs])


def accuracy(yhat, y):
    yhat=yhat.T
    y=y.T
    # print("yhat.shape,y.shape",yhat.shape,y.shape)
    Yhat=np.argmax(yhat,1)
    Y=np.argmax(y,1)
    accuracy = 100*np.sum(Y == Yhat)/y.shape[0]
    # print("yhat.shape,y.shape",Yhat.shape,Y.shape)
    # print("accuracy",accuracy)
    return accuracy


def Update_W_B(W, B,gradW, gradB,epsilon,alpha,trainY):

    for i in range(len(W)):
        W[i]=W[i]-(epsilon*gradW[i])+(alpha * W[i] /trainY.shape[1])
        B[i]=B[i]-(epsilon*gradB[i])
    return W,B

def train(trainX, trainY, weightsAndBiases, hidden_num, H_Layers, epsilon,alpha):

    trajectory = []

    bp = back_prop(trainX, trainY, weightsAndBiases, hidden_num, H_Layers)
    gradW, gradB = unpack(bp, hidden_num, H_Layers)
    W, B = unpack(weightsAndBiases, hidden_num, H_Layers)
    W,B=Update_W_B(W, B,gradW, gradB,epsilon,alpha,trainY)


    weightsAndBiases = np.hstack([w.flatten() for w in W] + [b.flatten() for b in B])
    trajectory.append(weightsAndBiases)

    return weightsAndBiases, trajectory

def SGD(train_X,train_Y,epochs,batch_size,weightsAndBiases, hidden_num, H_Layers, learning_rate,alpha,valid_X,valid_Y):
    print("epochs",epochs)
    TRAJECT = []
    for epoch in range(epochs):
        print("epoch",epoch)
                                   
        N_batches=int((len(train_X.T)/batch_size))
     
        init=0
        end=batch_size

        # print("train_X.shape, train_Y.shape",train_X.shape, train_Y.shape)

        for i in range(N_batches):
        
            mini_batch=train_X[:,init:end]
            
                            
            y_mini_batch=train_Y[:,init:end]
            # print("mini_batch.shape, y_mini_batch.shape",mini_batch.shape, y_mini_batch.shape)

            # print("batch_list[0][i].shape, batch_list[1][i].shape",batch_list[0][i].shape, batch_list[1][i].shape)
            # mini_batch.shape, y_mini_batch.shape (784, 16) (10, 16)
            # batch_list[0][i].shape, batch_list[1][i].shape (784, 16) (10, 16)


            weightsAndBiases, trajectory = train(mini_batch, y_mini_batch, weightsAndBiases, hidden_num, H_Layers, learning_rate,alpha)
            
            init=end
            end=end+batch_size
            if i % 10 == 0:   # sampled every 50 batches to get how the weights evolve 
                    TRAJECT.extend(trajectory)  #stored all trej on mini batched to TRAJECT

        loss, yyy, zzz, yhat = forward_prop(valid_X, valid_Y, weightsAndBiases, hidden_num, H_Layers)
        acc = accuracy(yhat, valid_Y)
        print("Loss on epoch: ", loss,"Accuracy: ",acc)
        # print(TRAJECT)
    
    return weightsAndBiases, TRAJECT



def findBestHyperparameters(trainX, trainY, testX, testY):

    Hidden_layers_list=[3,4,5]
    hidden_numbers_list = [50,30,40]
    mini_batch_size_list=[16,50,100]
    epsilon_list=[0.1,0.01,0.05,0.001]
    epochs_list=[50,75,100]
    alpha_list=[0.00001,0.0001,0.00002]


    # Hidden_layers_list=[3]
    # hidden_numbers_list = [50]
    # mini_batch_size_list=[50]
    # epsilon_list=[0.01]
    # epochs_list=[50]
    # alpha_list=[0.00001]  #87.26
 

    change_order_idx = np.random.permutation(trainX.shape[1])
    trainX = trainX[:, change_order_idx]
    trainY = trainY[:, change_order_idx]

    indx_values = np.random.permutation(trainX.shape[1])
    train_X=trainX[:,indx_values[:int(trainX.shape[1]*0.8)]]
    valid_X=trainX[:,indx_values[int(trainX.shape[1]*0.8):]]
    train_Y=trainY[:,indx_values[:int(trainX.shape[1]*0.8)]]
    valid_Y=trainY[:,indx_values[int(trainX.shape[1]*0.8):]]

    # print("train_x, train_y, valid_x, valid_y ",train_X.shape, train_Y.shape,valid_X.shape, valid_Y.shape )

    L_min=inf
    acc_max=10

    for H_Layers in Hidden_layers_list:
        for hidden_num in hidden_numbers_list:
            for epochs in epochs_list:
                for batch_size in mini_batch_size_list:
                    for learning_rate in epsilon_list:
                        for alpha in alpha_list:

                            print("H_Layers=", H_Layers, "hidden_num=", hidden_num,"Batch_size=", batch_size )
                            print("learning rate=",learning_rate,"epochs=", epochs,"alpha=", alpha)
                            
                            weightsAndBiases = initWeightsAndBiases(hidden_num, H_Layers)

                            weightsAndBiases, TRAJECT=SGD(train_X,train_Y,epochs,batch_size,weightsAndBiases, hidden_num, H_Layers, learning_rate,alpha,valid_X,valid_Y)
        
                            loss, yyy, zzz, yhat = forward_prop(valid_X, valid_Y, weightsAndBiases, hidden_num, H_Layers)
                          

                            if loss<L_min:
                                L_min=loss
                                bestHyperparameters=[H_Layers,hidden_num,epochs,batch_size,learning_rate,alpha]

                            acc = accuracy(yhat, valid_Y)
                           

                            if acc> acc_max:
                                Best_accuracy=acc
                                acc_max=acc


    best_H_Layers = bestHyperparameters[0]
    best_hidden_num = bestHyperparameters[1]
    best_epochs = bestHyperparameters[2]
    best_batch_size = bestHyperparameters[3]
    best_learning_rate = bestHyperparameters[4]
    best_alpha = bestHyperparameters[5]


    weightsAndBiases = initWeightsAndBiases(best_hidden_num, best_H_Layers)
    weightsAndBiases, trajectory=SGD(train_X,train_Y,best_epochs,best_batch_size,weightsAndBiases, best_hidden_num, best_H_Layers, best_learning_rate,best_alpha,testX, testY)
    loss, yyy, zzz, yhat = forward_prop(testX, testY, weightsAndBiases,  best_hidden_num, best_H_Layers)

    print("\nBest Hyper Parameters:  \nBest_Hidden_Layers:",best_H_Layers,"\nBest_hidden_num: ",best_hidden_num,"\nBest_epochs: ",best_epochs,"\nBest_batch_size: ",best_batch_size)
    print("Best_learning_rate: ",best_learning_rate,"\nBest_alpha: ",best_alpha)
    print("Best_accuracy on validation data :",Best_accuracy)

    print("\nloss value on best hyperparameters: ", loss)
    acc = accuracy(yhat, testY)
    print("\nAccuracy on Test data: ",acc)
    print("\n")
    
    return bestHyperparameters, TRAJECT, H_Layers, hidden_num



def initWeightsAndBiases(hidden_num, H_Layers) :
    Ws = []
    bs = []

    np.random.seed(0)
    W = 2 * (np.random.random(size=(hidden_num, NUM_INPUT)) / NUM_INPUT ** 0.5) - 1. / NUM_INPUT ** 0.5
    Ws.append(W)
    b = 0.01 * np.ones(hidden_num)
    bs.append(b)

    for i in range( H_Layers- 1):
        W = 2 * (np.random.random(size=(hidden_num,hidden_num)) / hidden_num ** 0.5) - 1. / hidden_num ** 0.5
        Ws.append(W)
        b = 0.01 * np.ones(hidden_num)
        bs.append(b)

    W = 2 * (np.random.random(size=(NUM_OUTPUT,hidden_num)) / hidden_num ** 0.5) - 1. / hidden_num ** 0.5
    Ws.append(W)
    b = 0.01 * np.ones(NUM_OUTPUT)
    bs.append(b)
    return np.hstack([W.flatten() for W in Ws] + [b.flatten() for b in bs])


def plotSGDPath (trainX, trainY, trajectory,H_Layers, hidden_num):
    # TODO: change this toy plot to show a 2-d projection of the weight space
    # along with the associated loss (cross-entropy), plus a superimposed 
    # trajectory across the landscape that was traversed using SGD. Use
    # sklearn.decomposition.PCA's fit_transform and inverse_transform methods.



    def toyFunction (x1, x2):
        a=[x1,x2]
        WtAndBia= pca.inverse_transform(a)  # to get it back original
        loss, zs, hs, yhat=forward_prop(trainX, trainY, WtAndBia, hidden_num, H_Layers)
        return loss


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    pca = PCA(n_components=2)  # 2 components
    data=pca.fit_transform(trajectory)  #reduce dims


    axis1 = np.arange(-40, 40, 2)  # Just an example
    axis2 = np.arange(-40, 40, 2) # Just an example
    Xaxis, Yaxis = np.meshgrid(axis1, axis2)
    Zaxis = np.zeros((len(axis1), len(axis2)))
    for i in range(len(axis1)):
        for j in range(len(axis2)):
            Zaxis[i,j] = toyFunction(Xaxis[i,j], Yaxis[i,j])
    ax.plot_surface(Xaxis, Yaxis, Zaxis, alpha=0.6)  

    # Now superimpose a scatter plot showing the weights during SGD.
    Xaxis =data[:, 0]   # Just an example
    Yaxis =data[:, 1]   # Just an example
    Zaxis = np.zeros(len(Xaxis))
    for i in range(len(Xaxis)):
        Zaxis[i] = toyFunction(Xaxis[i], Yaxis[i])
    ax.scatter(Xaxis, Yaxis, Zaxis, color='r')

    plt.show()



if __name__ == "__main__":
    # TODO: Load data and split into train, validation, test sets
    X_tr = np.reshape(np.load("fashion_mnist_train_images.npy"), (-1, 28*28))/255
    trainX=X_tr.T
    ytr = np.load("fashion_mnist_train_labels.npy")
    train_Y=ytr
    X_te = np.reshape(np.load("fashion_mnist_test_images.npy"), (-1, 28*28))/255
    testX=X_te.T
    yte = np.load("fashion_mnist_test_labels.npy")
    test_Y=yte

    #onehot encoding
    trainY=np.zeros((train_Y.size,train_Y.max()+1))
    testY=np.zeros((test_Y.size,test_Y.max()+1))
    trainY[np.arange(train_Y.size),train_Y]=1
    testY[np.arange(test_Y.size),test_Y]=1
    trainY=trainY.T
    testY=testY.T
    # print("trainX, trainY, testX, testY",trainX.shape, trainY.shape, testX.shape, testY.shape)
    

    weightsAndBiases = initWeightsAndBiases(NUM_HIDDEN,NUM_HIDDEN_LAYERS)


    print("===========scipy.optimize.check_grad==========")
    print(scipy.optimize.check_grad(
        lambda wab: forward_prop(np.atleast_2d(trainX[:, 0:5]), np.atleast_2d(trainY[:, 0:5]), wab, NUM_HIDDEN, NUM_HIDDEN_LAYERS)[0], \
        lambda wab: back_prop(np.atleast_2d(trainX[:, 0:5]), np.atleast_2d(trainY[:, 0:5]), wab, NUM_HIDDEN, NUM_HIDDEN_LAYERS), \
        weightsAndBiases))
    print("==============================================\n")


    # weightsAndBiases, trajectory = train(trainX, trainY, weightsAndBiases, testX, testY)
    bestHyperparameters,trajectory, H_Layers, hidden_num = findBestHyperparameters(trainX, trainY, testX, testY)


    change_order_idx = np.random.permutation(trainX.shape[1])
    trainX = trainX[:, change_order_idx]
    trainY = trainY[:, change_order_idx]

    # print("trajectory.shapet",trajectory)
    # # print("trajectory.shapet",trajectory[0].shape)
    # print("trajectory.shapet",type(trajectory[0]))
    # print("trajectory.shapet",len(trajectory[0]))
    # print("trainX.shape,trainY.shape",trainX.shape,trainY.shape)
  
    plotSGDPath(trainX[:, 0:5000], trainY[:, 0:5000], trajectory, H_Layers, hidden_num)
    


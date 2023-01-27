
from cmath import inf
import numpy as np

def gradient_w_b(X,w,b,Y,alpha):
    #X.T  60000*784  w=784*10   
    Z=np.dot(X.T,w)+b        #Z=60000*10   b=1*10
    # print("Z.shape",Z.shape)
    eZ=np.exp(Z)             #eZ=60000*10
    # print("eZ",eZ.shape)
    eZ_mean=np.reshape(np.sum(eZ,axis=1),(-1,1))
    # print("eZ_mean.shape",eZ_mean.shape)
    Yhat=eZ/eZ_mean   #Yhat=60000*10

    error=Yhat-Y
    # print("error shape",error.shape)
    # penalty=(alpha/X.size)*w
    penalty=alpha*w

    # print("penalty shape",penalty.shape)
    
    # grad_w=(np.dot(X,error))/X.shape[0]+penalty
    grad_w=(np.dot(X,error))/X.shape[1]+penalty
    # print("X.shape[0]",X.shape[1])
    # print("grad_w shape",grad_w.shape)

    # grad_b=(-np.mean(Y-Yhat))
    grad_b=np.array([(-(np.sum((Y-Yhat),0))/X.shape[1])])

    # print("grad_b.shape",grad_b.shape)

    return [grad_w,grad_b]


def fCE(X,Y,w,b,alpha):
    # print("fCE b shape",b.shape)
    # print("fCE np.dot(X.T,w) ",np.dot(X.T,w).shape)
    Z=np.dot(X.T,w)+b        
    eZ=np.exp(Z)   
    eZ_mean=np.reshape(np.sum(eZ,axis=1),(-1,1))
    Yhat=eZ/eZ_mean 
    # print("Yhat",Yhat.shape)
    logYhat=np.log(Yhat)
    # print("logYhat",logYhat.shape)
    # print("Y. shape",Y.shape)
    aa=-np.sum(Y*logYhat)/X.shape[1]

    # bb=(alpha/2)*(np.sum(np.dot(w.T,w)))

    fCE=aa
    return [fCE,Yhat]   


def stochastic_gradient_descent(epochs,learning_rate,alpha,mini_batch_size,X_train,Y_train,w,b):

    for i in range(epochs):
        print("Epoch no:",i,"out of",epochs)
        batches=int((len(X_train.T)/mini_batch_size))
        # batches=2
        init=0
        end=mini_batch_size
        for j in range(batches):         
          
            mini_batch=X_train[:,init:end]
            # print("Y_train.shape",Y_train.shape)
            y_mini_batch=Y_train[init:end,:]
          
            grad_w,grad_b=gradient_w_b(mini_batch,w,b,y_mini_batch,alpha)

            w_values=w-(np.dot(learning_rate,grad_w))
            b_values=b-(np.dot(learning_rate,grad_b))

            init=end
            end=end+mini_batch_size
            w=w_values
            b=b_values
    
        fCE_each_epoch,_=fCE(X_train,Y_train,w,b,alpha)
        bb=(alpha/2)*(np.sum(np.dot(w.T,w)))
        fCE_each_epoch+=bb
        print("fCE_each_epoch: ",fCE_each_epoch)
      
    return [fCE_each_epoch,w,b]


def softmax_regression():
    # Load data
    X_tr = np.reshape(np.load("fashion_mnist_train_images.npy"), (-1, 28*28))
    ytr = np.load("fashion_mnist_train_labels.npy")
    X_te = np.reshape(np.load("fashion_mnist_test_images.npy"), (-1, 28*28))
    yte = np.load("fashion_mnist_test_labels.npy")
    # print("X_tr",X_tr.shape)
    # print("ytr",ytr.shape)
    # print("X_te",X_te.shape)
    # print("yte",yte.shape)

    # #Division of Dataset 80% Training Dataset and 20% validation dataset 
    X=X_tr.T
    # print("X",X.shape)

    indx_values = np.random.permutation(X.shape[1])
    # print("X shape [1] ",X.shape[1])

    X_train=X[:,indx_values[:int(X.shape[1]*0.8)]]
    X_valid=X[:,indx_values[int(X.shape[1]*0.8):]]
    
    # print("X_train.shape,X_valid.shape",X_train.shape,X_valid.shape)

    Y_train=ytr[indx_values[:int(X.shape[1]*0.8)]]
    Y_valid=ytr[indx_values[int(X.shape[1]*0.8):]]

    #one hot encoding 
    y_train=np.zeros((Y_train.size,Y_train.max()+1))
    y_valid=np.zeros((Y_valid.size,Y_valid.max()+1))
    y_train[np.arange(Y_train.size),Y_train]=1
    y_valid[np.arange(Y_valid.size),Y_valid]=1
    # print("Y_valid.shape",y_train[:10,:10])
    # print("Y_valid.shape",y_valid[:10,:10])
    # print("y_train.shape y_valid.shape",y_train.shape,y_valid.shape)

    #Test data structuring
    X_test=X_te.T
    y_test=np.zeros((yte.size,yte.max()+1))
    y_test[np.arange(yte.size),yte]=1
    # print("X_test  y_test",X_test.shape,y_test.shape)

    # #Random values of 
    w=np.random.randint(0,1,int(X.shape[0]))
    w=np.atleast_2d(w).T
    # # b=np.random.randn(1,1)
    b=np.zeros((10))

    # print("shape of w",w.shape)

    epochs=[1000,800,600,400]
    learning_rate=[0.000003,0.000004,0.000005,0.000006]
    alpha=[2,3,4,5]
    mini_batch_size=[600,400,200,100]

    # epochs=[400,600,800,1000]
    # learning_rate=[0.000001,0.000002,0.000003,0.000004]
    # alpha=[1,2,3,4]
    # mini_batch_size=[400,600,800,1000]

    fCE_min=inf

    for i in epochs:
        print("epochs",i)
        for j in learning_rate:
            for k in alpha:
                for l in mini_batch_size:
                    #Fmse=stochastic_gradient_descent(epochs,learning_rate,alpha,mini_batch_size,X_train,Y_train,w,b)
                    print("Current epochs (i)",i,"Current Learning rate",j,"Current alpha", k,"Current mini_batch_size",l)
                    fCE_,w,b =stochastic_gradient_descent(i,j,k,l,X_train,y_train,w,b)
                    fCE_valid,_ = fCE(X_valid,y_valid,w,b,k)
                
                    print("Fmse_valid",fCE_valid)
            
                    if fCE_valid<fCE_min:
                        print("Lowest Fmse for epochs (i)",i," Learning rate",j,"alpha", k," mini_batch_size",l)
                        Min_fCE=fCE_valid
                        print("Min_FMSE",Min_fCE)
                        hyper_para=[i,j,k,l]
                        fCE_min=fCE_valid
    
    best_epoch = hyper_para[0]
    best_lr = hyper_para[1]
    best_alpha = hyper_para[2]
    best_mini = hyper_para[3]
    #Random values of 
    w=np.random.randint(0,1,int(X.shape[0]))
    w=np.atleast_2d(w).T
    b=np.zeros((10))
  
    fCE_train,weights,bias= stochastic_gradient_descent(best_epoch,best_lr,best_alpha,best_mini,
                                                        X_train,y_train,w,b)
    fCE_test,Yhat = fCE(X_test,y_test,weights,bias,best_alpha)
    

    Yhat=np.argmax(Yhat,1)
    accuracy = 100*np.sum(yte == Yhat)/X_te.shape[0]
    print("Minimun value of fCE on validation dataset",Min_fCE)
    print("fCE on Test dataset is: ",fCE_test)
    print("Best Hyperparameters: epochs (i)",i," Learning rate",j,"alpha", k," mini_batch_size",l)
    print("Accuracy in percentage",accuracy)
    return ...

softmax_regression ()
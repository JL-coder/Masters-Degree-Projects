from audioop import bias
from cmath import inf
from re import A
import numpy as np
from numpy import atleast_2d, random



def linear_regression (X, y_tr):
    w=np.linalg.solve(np.dot(X,X.T),np.dot(X,y_tr))
    return w

def gredient_w(X,w,b,y,alpha):
    #here gredient with respect to w 
    error=(np.dot(X.T,w))+b-y
   
    aa=(np.dot(X,error))/X.shape[1]
    
    penalty=(alpha*w)/X.shape[1]

    gredient_Fmse_w=aa+penalty
    return gredient_Fmse_w

def gredient_b(X,w,b,y):

    gredient_Fmse_b=np.mean((np.dot(X.T,w)+b-y))
    return gredient_Fmse_b

def Fmse(X,w,b,y):

    cc=np.square(np.dot(X.T,w)+b-y)

    Fmse=(np.mean(cc)/(2))
    return Fmse



def Stochastic_gradient_descent(epochs,learning_rate,alpha,mini_batch_size,X_train,Y_train,w,b):

    for i in range(epochs):
        batches=int((len(X_train.T)/mini_batch_size))
        # batches=2
        init=0
        end=mini_batch_size
        for j in range(batches):         
          
            mini_batch=X_train[:,init:end]
            
            y_mini_batch=Y_train[init:end]
          
            grad_w=gredient_w(mini_batch,w,b,y_mini_batch,alpha)
            grad_b=gredient_b(mini_batch,w,b,y_mini_batch)

         

            w_values=w-(np.dot(learning_rate,grad_w))
            b_values=b-(np.dot(learning_rate,grad_b))
          

            init=end
            end=end+mini_batch_size
            w=w_values
            b=b_values
            
        
    
        Fmse_each_epoch=Fmse(X_train,w,b,Y_train)
      
    return [Fmse_each_epoch,w,b]


def train_age_regressor ():
    # Load data
    X_tr = np.reshape(np.load("C:/Users/joshu/Desktop/Deep Learning/Homework 2/age_regression_Xtr.npy"), (-1, 48*48))
    ytr = np.load("C:/Users/joshu/Desktop/Deep Learning/Homework 2/age_regression_ytr.npy")
    X_te = np.reshape(np.load("C:/Users/joshu/Desktop/Deep Learning/Homework 2/age_regression_Xte.npy"), (-1, 48*48))
    yte = np.load("C:/Users/joshu/Desktop/Deep Learning/Homework 2/age_regression_yte.npy")

    # print("X_tr",X_tr.shape)

    X=X_tr.T
    # print("X",X.shape)
    # print("ytr",ytr.shape)

    #Division of Dataset 80% Training Dataset and 20% validation dataset 
    indx_values = np.random.permutation(X.shape[1])
    # print("X shape [1] ",X.shape[1])

    X_train=X[:,indx_values[:int(X.shape[1]*0.8)]]
    X_valid=X[:,indx_values[int(X.shape[1]*0.8):]]
    
    # print("X_train.shape,X_valid.shape",X_train.shape,X_valid.shape)

    Y_train=ytr[indx_values[:int(X.shape[1]*0.8)]]
    Y_train=atleast_2d(Y_train).T
    Y_valid=ytr[indx_values[int(X.shape[1]*0.8):]]
    Y_valid=atleast_2d(Y_valid).T
    print(Y_train.shape)
    print(Y_valid.shape)

    #Random values of 
    w=np.random.randint(-10,10,int(X.shape[0]))
    w=np.atleast_2d(w).T
    # b=np.random.randn(1,1)
    b=0
    
    # print("shape of w and b",w.shape)

    epochs=[50,70,90,110]
    learning_rate=[0.0003,0.0001,0.0007,0.0009]
    alpha=[1,3,5,7]
    mini_batch_size=[400,200,100,50]

    Fmse_min=inf

    
    for m in epochs:
        print("epochs",m)
        for n in learning_rate:
            for o in alpha:
                for p in mini_batch_size:
                    #Fmse=Stochastic_gradient_descent(epochs,learning_rate,alpha,mini_batch_size,X_train,Y_train,w,b)
                    Fmse_,w,b =Stochastic_gradient_descent(m,n,o,p,X_train,Y_train,w,b)
                    Fmse_valid = Fmse(X_valid,w,b,Y_valid)
                    if Fmse_valid<Fmse_min:
                        print("Lowest Fmse for epochs (m)",m," Learning rate",n,"alpha", o," mini_batch_size",p)
                        Min_FMSE=Fmse_valid
                        print("Min_FMSE",Min_FMSE)
                        Hyper_para=[m,n,o,p]
                        Fmse_min=Fmse_valid
    
    best_epoch = Hyper_para[0]
    best_lr = Hyper_para[1]
    best_alpha = Hyper_para[2]
    best_mini = Hyper_para[3]
    #Random values of 
    w=np.random.randint(-10,10,int(X.shape[0]))
    w=np.atleast_2d(w).T
    # b=np.random.randn(1,1)
    b=0
    Fmse_train,weights,bias= Stochastic_gradient_descent(best_epoch,best_lr,best_alpha,best_mini,X_train,Y_train,w,b)
    Fmse_test = Fmse(X_te.T,weights,bias,yte)
    print("fMSE on Testing dataset is: ",Fmse_test)
    return ...

train_age_regressor()

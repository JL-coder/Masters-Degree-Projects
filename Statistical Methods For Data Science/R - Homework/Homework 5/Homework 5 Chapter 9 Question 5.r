#We have seen that we can fit an SVM with a non-linear kernel in order
#to perform classification using a non-linear decision boundary.We will
#now see that we can also obtain a non-linear decision boundary by
#performing logistic regression using non-linear transformations of the
#features.

#a) Generate a data set with n = 500 and p = 2, such that the observations
#belong to two classes with a quadratic decision boundary
#between them. For instance, you can do this as follows:

set.seed(321)
x1 = runif(500) - 0.5
x2 = runif(500) - 0.5
y = 1 * (x1^2 - x2^2 > 0)

#b) Plot the observations, colored according to their class labels.
#Your plot should display X1 on the x-axis, and X2 on the yaxis.

plot(x1[y==0], x2[y==0], col = "green", xlab = "X1", ylab = "X2", pch = "+")
points(x1[y==1], x2[y==1], col = "blue", pch = 4)

#c) Fit a logistic regression model to the data, using X1 and X2 as
#predictors.

linear_model.fit = glm(y ~ x1 + x2, family = binomial)
summary(linear_model.fit)

#d) Apply this model to the training data in order to obtain a predicted
#class label for each training observation. Plot the observations,
#colored according to the predicted class labels. The
#decision boundary should be linear.

data = data.frame(x1 = x1, x2 = x2, y = y)
lin_model.probability = predict(linear_model.fit, data, type="response")
lin_model.prediction = ifelse(lin_model.probability > 0.52, 1, 0)
data.positive = data[lin_model.prediction == 1, ]
data.negative = data[lin_model.prediction == 0, ]
plot(data.positive$x1, data.positive$x2, col = "green", xlab = "X1", ylab="X2", pch = "+")
points(data.negative$x1, data.negative$x2, col = "red", pch = 4)

#e) Now fit a logistic regression model to the data using non-linear
#functions of X1 and X2 as predictors (e.g. X^2 1 , X1×X2, log(X2),
#and so forth).
lin_model.probability = glm(y ~ poly(x1, 2) + poly(x2, 2) + I(x1 * x2), data = data, family = binomial)

#f) Apply this model to the training data in order to obtain a predicted
#class label for each training observation. Plot the observations,
#colored according to the predicted class labels. The
#decision boundary should be obviously non-linear. If it is not,
#then repeat (a)-(e) until you come up with an example in which
#the predicted class labels are obviously non-linear.

lin_model.probability = predict(linear_model.fit, data, type="response")
lin_model.prediction = ifelse(lin_model.probability > 0.5, 1, 0)
data.positive = data[lin_model.prediction == 1, ]
data.negative = data[lin_model.prediction == 0, ]
plot(data.positive$x1, data.positive$x2, col = "green", xlab = "X1", 
ylab = "X2", pch = "+")
points(data.negative$x1, data.negative$x2, col = "red", pch = 4)

#g) Fit a support vector classifier to the data with X1 and X2 as
#predictors. Obtain a class prediction for each training observation.
#Plot the observations, colored according to the predicted
#class labels.

library(e1071)
SVM.fit = svm(as.factor(y) ~ x1 + x2, data, kernel = "linear", cost = 0.1)
SVM.prediction = predict(SVM.fit, data)
data.positive = data[SVM.prediction == 1, ]
data.negative = data[SVM.prediction == 0, ]
plot(data.positive$x1, data.positive$x2, col = "green",
xlab = "X1", ylab = "X2", pch = "+")
points(data.negative$x1, data.negative$x2, col = "red", pch = 4)

#h) Fit a SVM using a non-linear kernel to the data. Obtain a class
#prediction for each training observation. Plot the observations,
#colored according to the predicted class labels.

SVM.fit = svm(as.factor(y)~ x1 + x2, data, gamma = 1)
SVM.prediction = predict(SVM.fit, data)
data.positive = data[SVM.prediction == 1, ]
data.negative = data[SVM.prediction == 0, ]
plot(data.positive$x1, data.positive$x2, col = "green", xlab = "X1",
 ylab = "X2", pch = "+")
points(data.negative$x1, data.negative$x2, col = "red", pch = 4)

#g) Comment on your results.
# In this analysis different SVMs were used to classify a random dataset. 
#From this we have found that when a model is non-linear SVMs are an 
#important tool for getting an accurate model. However, without an 
#interaction term (gamma) SVM with linear/logistic kernals are not as good 
#at finding the non-linear decision boundaries. That being said only gamma
# needs to be found to improve a SVM model and it can be found fairly easily 
#through cross-validation.

#Chapter 9 Question 4
#Generate a simulated two-class data set with 100 observations and
#two features in which there is a visible but non-linear separation between
#the two classes. Show that in this setting, a support vector
#machine with a polynomial kernel (with degree greater than 1) or a
#radial kernel will outperform a support vector classifier on the training
#data. Which technique performs best on the test data? Make
#plots and report training and test error rates in order to back up
#your assertions.

library('caret')

set.seed(1)
something <- 3
Xvar <- matrix(rnorm(100 * 2), ncol = 2)
Xvar[1:30, ] <- Xvar[1:30, ] + something
Xvar[31:60, ] <- Xvar[31:60, ] - something
y <- c(rep(0,60), rep(1,40))
data_frame <- data.frame(x = X, y = as.factor(y))
plot(Xvar, col = y + 1)

#Split to training and testing set
training <- sample(100, 80)
dat.training <- dat[training, ]
dat.testing <- dat[-training, ]

#Start SVM and describe model
library(e1071)
SVM <- svm(y ~ ., data = dat.training, kernel = "linear", scale = FALSE)
plot(SVM, dat.training)
summary(SVM)

table(predict = SVM$fitted, truth = dat.training$y)
SVM.Linear <- confusionMatrix(data = SVM$fitted, reference = dat.training$y)
SVM.Linear
#error rate => 32/48+32 = 0.4 the error rate is 40%. 
#All of the training points were labelled zero so the 
#model is useless on that set.

SVM.poly <- svm(y ~ ., data = dat.training, kernel = "polynomial", scale = FALSE)
plot(SVM.poly, data = dat.training)

table(predict = SVM.poly$fitted, truth = dat.training$y)
SVM.poly <- confusionMatrix(data = SVM.poly$fitted, reference = dat.training$y)
SVM.poly
#The model made 5 correct predictions. It has an error rate of 35%
#Try again with radial kernal

SVM.radial <- svm(y ~ ., data = dat.training, kernel = "radial", scale = FALSE)
plot(SVM.radial, data = dat.training)
table(predict = SVM.radial$fitted, truth = dat.training$y)
SVM.radial <- confusionMatrix(data = SVM.radial$fitted, reference = dat.training$y)
SVM.radial

#The model made 4 correct predictions. With an error rate of 35%.

#Among the linear, polynomial, and radial SVM both polynomial and
#radial performed better than linear SVM with an error rate of 35%.
#Linear had an error rate of 40%. The default degrees of freedom is 3. 
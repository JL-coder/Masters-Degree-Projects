#Part a)
library(readr)
Default <- read_csv("R Related Files/Homework 2/Default.csv")
Default.fit <- glm(as.factor(default) ~ income + balance, data = Default, family = binomial)
summary(Default.fit)
#Part b)
#1. Split sample into training and validation set
trainingSet <- sample(dim(Default)[1], dim(Default)[1] / 2)
#2. Fit to multiple logistic regression model
fit.glm <- glm(as.factor(default) ~ income + balance, data = Default, family = "binomial", subset = trainingSet)
summary(fit.glm)
#3. Obtain a prediction of default status for each individual
probability = predict(fit.glm, newdata = Default[-trainingSet,], type = "response")
prediction.glm <- rep("No", length(probability))
prediction.glm[probability > 0.5] <- "Yes"
#4. Compute validation set error
mean(prediction.glm != Default[-trainingSet,]$default)
#Part c)
#Experiment 1
trainingSet <- sample(dim(Default)[1], dim(Default)[1] / 2)
fit.glm <- glm(as.factor(default) ~ income + balance, data = Default, family = "binomial", subset = trainingSet)
summary(fit.glm)
probability = predict(fit.glm, newdata = Default[-trainingSet,], type = "response")
prediction.glm <- rep("No", length(probability))
prediction.glm[probability > 0.5] <- "Yes"
mean(prediction.glm != Default[-trainingSet,]$default)
#Experiment 2
trainingSet <- sample(dim(Default)[1], dim(Default)[1] / 2)
fit.glm <- glm(as.factor(default) ~ income + balance, data = Default, family = "binomial", subset = trainingSet)
summary(fit.glm)
probability = predict(fit.glm, newdata = Default[-trainingSet,], type = "response")
prediction.glm <- rep("No", length(probability))
prediction.glm[probability > 0.5] <- "Yes"
mean(prediction.glm != Default[-trainingSet,]$default)
#Experiment 3
trainingSet <- sample(dim(Default)[1], dim(Default)[1] / 2)
fit.glm <- glm(as.factor(default) ~ income + balance, data = Default, family = "binomial", subset = trainingSet)
summary(fit.glm)
probability = predict(fit.glm, newdata = Default[-trainingSet,], type = "response")
prediction.glm <- rep("No", length(probability))
prediction.glm[probability > 0.5] <- "Yes"
mean(prediction.glm != Default[-trainingSet,]$default)
#The validation test error rate is variable. It is dependent on which observations are in the training and validation sets.
#Part d)
trainingSet <- sample(dim(Default)[1], dim(Default)[1] / 2)
fit.glm <- glm(as.factor(default) ~ income + balance + student, data = Default, family = "binomial", subset = trainingSet)
probability = predict(fit.glm, newdata = Default[-trainingSet,], type = "response")
prediction.glm <-  rep("No", length(probability))
prediction.glm[probability > 0.5] <- "Yes"
mean(prediction.glm != Default[-trainingSet,]$default)
#Based on the three experiments performed earlier it does not appear that adding a "student" dummy variable leads to a reduction in validation set esimate of the error rate.
#For this run it seems the error rate was about in the middle when compared to the three experimental runs. 


#4.  (15 points) Section 4.7, page171, question 10
#Part a)
library(readr)
weekly <- read_csv("R Related Files/Homework 2/Weekly.csv")
summary(weekly)
install.packages("corrplot")
corrplot(cor(weekly[,-9]))
#According to the correlation plot the only variables that are linearly related are the year and volume.
pairs(weekly[,-9])
plot(weekly$Volume, ylab = "Shares traded (in billions)")
#Its clear that the volume of shares traded since the 1990s have increased exponetially.

#Part b)
weekly.fit = glm(as.factor(Direction) ~ Lag1+Lag2+Lag3+Lag4+Lag5+Volume, data=Weekly,family=binomial)
summary(weekly.fit)
#The only variable that appears statistically significant is Lag2. All other variables fail to reject the null hypothesis.

#Part c)
logweekly.probe = predict(weekly.fit,type = 'response')
logweekly.pred = rep("Down", length(logweekly.probe))
logweekly.pred[logweekly.probe > 0.5] = "Up" 
table(logweekly.pred, Direction)
#There are 54 true down predictions and 557 true up predictions out of a toal of 1089 total predictions therefore the percentage of correct predictions is:
((54 + 557)/(54 + 48 + 430 +557)) * 100
#Based off this information the model only predicted the weekly market trends correctly 56.11% of the time. 
(557/(48 + 557)) * 100
#The model was able to predict the weekly Up trends 92.1% of the time.
(54/(430+54)) * 100
#The model was able to predict the weekly Down trends only 11.2% of the time.
#That means most of the error from the model is coming from its inability to accurately predict the downward trend of the stock.

#Part d)
training = (Year<2009)
weekly.09to10 <- weekly[!training,]
weekly.fit <- glm(as.factor(Direction) ~ Lag2, data = weekly, family = binomial, subset = training)
logweekly.probe = predict(weekly.fit, weekly.09to10, type = "response")
logweekly.pred = rep("Down", length(logweekly.probe))
logweekly.pred[logweekly.probe > 0.5] = "Up"
Direction.09to10 = Direction[!training]
table(logweekly.pred, Direction.09to10)
(mean(logweekly.pred == Direction.09to10)) * 100
#By splitting the Weekly dataset into training and testing datasets we were able to improve the model's prediction capability.
#The model was able to correct predict the weekly trend 62.5% of the time. An about 6% increase from using the whole dataset. 
(56/(5+56)) * 100
#The model's ability to predict upward trends took a slight hit and is able to accurately predict 91.80% of the time.
(9/(9+34)) * 100
#The greatest improvement to the model came with its ability to accurately predict downward trends. The model was able to predict downward trends 20.93% of the time. A nearly 10% increase from using the whole dataset!

#Part e)
library(MASS)
weeklyLDA.fit <- lda(as.factor(Direction) ~ Lag2, data=weekly,family=binomial, subset=training)
weeklyLDA.predict <- predict(weeklyLDA.fit, weekly.09to10)
weeklyLDA.pred <- predict(weeklyLDA.fit, weekly.09to10)
table(weeklyLDA.pred$class, Direction.09to10)
(mean(weeklyLDA.pred$class==Direction.09to10)) * 100
#The LDA model was able to predict the weekly trend 62.5% of the time. Same as the logistic regression model.

#Part d)
weeklyQDA.fit = qda(Direction ~ Lag2, data = weekly, subset = training)
weeklyQDA.pred = predict(weeklyQDA.fit, weekly.09to10)$class
table(weeklyQDA.pred, Direction.09to10)
(mean(weeklyQDA.pred==Direction.09to10)) * 100
#The quadratic linear analysis model was able to predict the weekly trend 58.65% of the time. Lower than both LDA and and Logistic Regression. 

#Part e)
library(class)
week.training = as.matrix(Lag2[training])
week.test = as.matrix(Lag2[!training])
training.Direction = Direction[training]
training.Direction = Direction[training]
set.seed(1)
weeklyKNN.pred = knn(week.training, week.test, training.Direction, k = 1)
table(weeklyKNN.pred, Direction.09to10)
(mean(weeklyKNN.pred == Direction.09to10)) * 100
#The KNN model was able to predict the weekly trend 50% of the time. Lower than every other model that has been tried.

#Part f)
#Both Logistic Regression and Linear Discriminant Analysis tied for first place with an accuracy rate of 62.5%.

#Part g)
#See if more data is useful for prediction. Try using lag columns 2 - 4. 
weekly.fit <- glm(as.factor(Direction) ~ Lag2 + Lag3 + Lag4, data=weekly,family=binomial, subset=training)
logweekly.prob = predict(weekly.fit, weekly.09to10, type = "response")
logweekly.pred = rep("Down", length(logweekly.prob))
logweekly.pred[logweekly.prob > 0.5] = "Up"
Direction.09to10 = Direction[!training]
table(logweekly.pred, Direction.09to10)
(mean(logweekly.pred == Direction.09to10)) * 100
#When including lag columns 3 and 4 the accuracy for logistic regression goes down by about 1% to 61.53%
#Try this with LDA
weeklyLDA.fit <- lda(Direction~ Lag2 + Lag3 + Lag4, data=weekly,family=binomial, subset=training)
weeklyLDA.pred <- predict(weeklyLDA.fit, weekly.09to10)
table(weeklyLDA.pred$class, Direction.09to10)
(mean(weeklyLDA.pred$class == Direction.09to10)) * 100
#Same accuracy as logistic regression
#Now try QDA
weeklyQDA.fit = qda(Direction ~ Lag2 + Lag3 + Lag4, data = weekly, subset = training)
weeklyQDA.pred = predict(weeklyQDA.fit, weekly.09to10)$class
table(weeklyQDA.pred, Direction.09to10)
(mean(weeklyQDA.pred == Direction.09to10)) * 100
#The accuracy of QDA is 54.81% which is about a 4% drop from the original QDA using just Lag2 as the x value.
#KNN will inevitebly drop with more x variables so instead of adding more I am going to increase the value of K
#K = 5
weekly.train = as.matrix(Lag2[training])
weekly.test = as.matrix(Lag2[!training])
training.Direction = Direction[training]
set.seed(1)
weeklyKNN.pred = knn(weekly.train, weekly.test, training.Direction, k=5)
table(weeklyKNN.pred, Direction.09to10)
(mean(weeklyKNN.pred == Direction.09to10)) * 100
#Accuracy for k = 3 was 53.85% an increse from k = 1. 
#K = 100
weekly.train = as.matrix(Lag2[training])
weekly.test = as.matrix(Lag2[!training])
training.Direction = Direction[training]
set.seed(1)
weeklyKNN.pred = knn(weekly.train, weekly.test, training.Direction, k=100)
table(weeklyKNN.pred, Direction.09to10)
(mean(weeklyKNN.pred == Direction.09to10)) * 100
# With a K of 100 the accuracy continued to increse and is now at 57.69%.
#With more x variables there was a slight drop in accuracy for all the algorithms applied. LDA and Logistic Regression still performed the best and did not take a large hit to their accruracy when more variables were added.



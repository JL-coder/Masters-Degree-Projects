#Section 7.9 Questions 6
#Part A: Perform polynomial regression to predict wage using age. 
#Use cross-validation to select the optimal degree d for the polynomial. 
#What degree was chosen, and how does this compare to the results of hypothesis testing using ANOVA? Make a plot of the resulting polynomial fit to the data.
#install.packages('ISLR')
#install.packages('ggplot2')
#install.packages('data.table')
#install.packages('gam')
#install.packages('tree')
#install.packages('randomForest')
library(ISLR)
library(boot)
library(ggplot2)
library(data.table)
library(gam)
library(tree)
library(MASS)
library(randomForest)
Wage <- read.csv("C:/Users/joshu/OneDrive/Documents/R Related Files/Homework 4/Wage.csv")
#View(Wage)
set.seed(15)
degree <- 10
cv.errors <- rep(0, degree)
for (x in 1:degree) {
  glm.fit <- glm(wage ~ poly(age, x), data = Wage)
  cv.errors[x] <- cv.glm(Wage, glm.fit, K = 10)$delta[1]
}
cv.errors
plot(cv.errors, type = "b", xlab = "Polynomial Degree", ylab = "Test MSE")
points(which.min(cv.errors), cv.errors[which.min(cv.errors)], col = "green", cex = 2, pch =  19)
fit.1 = lm(wage ~ age ,data=Wage)
fit.2 = lm(wage ~ poly(age, 2), data = Wage)
fit.3 = lm(wage ~ poly(age, 3), data = Wage)
fit.4 = lm(wage ~ poly(age, 4), data = Wage)
fit.5 = lm(wage ~ poly(age, 5), data = Wage)
anova(fit.1, fit.2, fit.3, fit.4, fit.5)
#According to the anova test degree 4 should be acceptable.
#Used 3 polynomials instead of 4 because confidence interval was slightly smaller
ggplot(Wage, aes(age, wage)) + geom_point(color = "red") + 
  stat_smooth(method = "lm", formula = y ~ poly(x, 3), size = 1)
#Part B: Fit a step function to predict wage using age, and perform crossvalidation
#to choose the optimal number of cuts. Make a plot of
#the fit obtained.
variable <- rep(0, 10)
for (x in 2:10) {
  Wage$cut.point = cut(Wage$age, x)
  lm.fit = glm(wage ~ cut.point, data = Wage)
  variable[x] = cv.glm(Wage, lm.fit, K = 10)$delta[2]
}
variable.data <- data.table(c(2,3,4,5,6,7,8,9,10), variable[-1])
ggplot(variable.data, aes(V1, V2)) + geom_line()
#Minimum cut point of 8
fit <- glm(wage~cut(age, 8), data=Wage)
prediction <- predict(fit, data.frame(age = seq(from = 18, to = 80)))
pred <- data.table(seq(from = 18, to = 80), prediction, keep.rownames = TRUE)
ggplot(Wage, aes(age, wage)) + geom_point(color = "blue") + geom_line(data = pred, aes(V1, prediction), size = 1)
#Shows step function plot with a minimum of 8 cut points. 

#Section 7.9 Question 7: The Wage data set contains a number of other features not explored
#in this chapter, such as marital status (maritl), job class (jobclass),
#and others. Explore the relationships between some of these other
#predictors and wage, and use non-linear fitting techniques in order to
#fit flexible models to the data. Create plots of the results obtained,
#and write a summary of your findings.

View(Wage)
#Lets look into marital status and see if I can find anything interesting
table(Wage$maritl)
#Fairly low numbers for widowed and separated individuals
ggplot(Wage, aes(x = maritl, y = wage, fill = maritl)) + geom_boxplot() + theme(legend.position = "none")
#Married workers tend to make higher wages compared to the rest.
#Look at wages vs education
table(Wage$education)
ggplot(Wage, aes(x = education, y = wage, fill = education)) + geom_boxplot() + theme(legend.position = "none")
#As expected indivduals with more advanced degrees tend to make more in wages. 
table(Wage$region)
#The data set is focused on middle alantic and doesnt have any information from elsewhere
table(Wage$race)
ggplot(Wage, aes(x = race, y = wage, fill = race)) + geom_boxplot() + theme(legend.position = "none")
#Asian's tend to earn higher wages than the other races and have a larger spread compared to the others.
table(Wage$jobclass)
ggplot(Wage, aes(x = jobclass, y = wage, fill = jobclass)) + geom_boxplot() + theme(legend.position = "none")
#Workers working in information tend to make more than industrial workers
table(Wage$health)
#Based on the table those whose health falls into the "Very Good" category tend to make more.
ggplot(Wage, aes(x = health, y = wage, fill = health)) + geom_boxplot() + theme(legend.position = "none")
table(Wage$health_ins)
ggplot(Wage, aes(x = health_ins, y = wage, fill = health_ins)) + geom_boxplot() + theme(legend.position = "none")
#Workers with higher wages tend to have health insurance. Disturbingly almost half of the workers don't have health insurance.
#From all of this I now understand how wages interact with most of the dependent variables. 
#I decided to fit wages with multiple predictors using GAM
fit1 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education, data = Wage)
fit2 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + jobclass, data = Wage)
fit3 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + maritl, data = Wage)
fit4 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + jobclass + maritl, data = Wage)
fit5 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + race, data = Wage)
fit6 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + jobclass + race, data = Wage)
fit7 <- gam(wage ~ lo(year, span = 0.7) + s(age, 5) + education + jobclass + race + maritl, data = Wage)
anova(fit1, fit2, fit3, fit4, fit5, fit6, fit7)
#All of the different fits appear to have high significance
#Fit5 had the lowest score and appeard to fit the best so lets start with that
par(mfrow = c(2, 3))
plot(fit5, se = T, col = "blue")
#And check fit7 and fit4 just for fun
par(mfrow = c(2, 3))
plot(fit7, se = T, col = "red")
plot(fit4, se = T, col = "green")
#These all look the same to the first one regardless of changes I make so I guess they aren't needed... that said:
#It appears according to the graphs that even with the the multiple predictors as time (in years) increases so do wages
#Similarly as age increases wages do as well at least till indivduals get to retirement age (50s and more prominetitly 60s) then wages start to 
#decrease drastically and the confidence interval grows to reflect this difference. 


#Section 8.4, Page 333-334, question 8
#Part A: Split into training and testing set.
Carseats <- read.csv("C:/Users/joshu/OneDrive/Documents/R Related Files/Homework 4/Carseats.csv")
set.seed(1)
Carseats.training <- sample(nrow(Carseats), nrow(Carseats) / 2)
Carseats.testing <- Carseats[-training, "Sales"]

#Part B: Fit a regression tree to the training set, plot, and interpret (i.e. what test error rate?)
tree.carseats <- tree(Sales~.,data=Carseats,subset=Carseats.training)
summary(tree.carseats)
plot(tree.carseats)
text(tree.carseats, pretty = 0)

carseat.prediction <- predict(tree.carseats, newdata = Carseats[-training,])
mean((carseat.prediction - Carseats.testing)^2)
#MSE of 3.330945 

#Part C: Use cross-validation in order to determine the optimal level of
#tree complexity. Does pruning the tree improve the test error
#rate?

set.seed(1)
crossval.carseats <- cv.tree(tree.carseats)
crossval.carseats
plot(crossval.carseats$size, crossval.carseats$dev, type = "b")
tree.minpt <- which.min(crossval.carseats$dev)
#Min point by cross validation seems to change alot. The point I create does not seem to help but the lowest is about 13 or 14
points(tree.minpt, crossval.carseats$dev[tree.minpt], col = "green", pch = 20, cex = 2)
prune.carseats <- prune.tree(tree.carseats, best = 14)
plot(prune.carseats)
text(prune.carseats, pretty = 0)
pruned.prediction <- predict(prune.carseats, Carseats[-training,])
mean((pruned.prediction - Carseats.testing)^2)
#MSE of 3.420517. Pruning made the MSE worse. 

#Part D: Use the bagging approach in order to analyze this data. What
#test error rate do you obtain? Use the importance() function to
#determine which variables are most important.

#set.seed(1)
bagging.carseats = randomForest(Sales~., data = Carseats, mtry = 10, subset = training, importance = T)
#bagging.carseats
prediction.bagging = predict(bagging.carseats, newdata = Carseats[-training,])
mean((prediction.bagging - Carseats.testing)^2)
importance(bagging.carseats)
#From importance we find that Price and ShelveLoc were the two most important variables
#MSE of 2.556495. Bagging approuch reduced the MSE.

#Part E: Use random forests to analyze this data. What test error rate do
#you obtain? Use the importance() function to determine which
#variables are most important. Describe the effect of m, the number
#of variables considered at each split, on the error rate
#obtained.

randforest5try.carseats = randomForest(Sales~., data = Carseats, mtry = 5, subset = training, importance = T)
randforest3try.carseats = randomForest(Sales~., data = Carseats, mtry = 3, subset = training, importance = T)
#randforest5try.carseats
#randforest3try.carseats
#Random forest with 3mtry has lower % of var explained and higher mean of squared residuals
prediction5try.carseats = predict(randforest5try.carseats, newdata = Carseats[-training,])
prediction3try.carseats = predict(randforest3try.carseats, newdata = Carseats[-training,])
mean((prediction5try.carseats - Carseats.testing)^2)
#MSE for 5mtry is 2.838924. A little higher than the bagging MSE.
mean((prediction3try.carseats - Carseats.testing)^2)
#MSE for 3mtry is 3.238048. The MSE was better than the pruning MSE but worse than using a higher number for mtry
importance(randforest5try.carseats)
#From importance we find that price and shelveloc are still the two most important variables but their %IncMSE are lower than when bagging.

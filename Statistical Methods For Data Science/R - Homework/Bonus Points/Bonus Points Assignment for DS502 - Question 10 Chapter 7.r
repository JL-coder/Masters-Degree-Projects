#Bonus Points Assignment for DS502
#Question 10 Chapter 7.9
library(ISLR)
library(leaps)
library(gam)
library(gbm)
library(glmnet)
library(randomForest)
library(cutpointr)
#install.packages('leaps')
#install.packages('cutpointr')
#install.packages('regsubsets')

#Part A) Split the data into a training set and a test set. Using out-of-state
#tuition as the response and the other variables as the predictors,
#perform forward stepwise selection on the training set in order
#to identify a satisfactory model that uses just a subset of the
#predictors.

#College <- read.csv("C:/Users/joshu/OneDrive/Documents/R Related Files/Bonus Points/College.csv")
attach(College)

set.seed(2020)

train = sample(length(Outstate), length(Outstate) / 2)
test = -train
College.train = College[train, ]
College.test = College[test, ]

#Note the regsubsets function was acting up on my machine for some reason and wouldnt run the first time 
#despite the libraries for it being installed. Might need to check libraries to get this to work on your machine.
forward_fit = regsubsets(Outstate ~ ., data = College.train, nvmax = 17, method = "forward")

fit.summary = summary(forward_fit)

par(mfrow = c(1, 3))

#For CP
plot(fit.summary$cp, xlab = "Number of Variables", ylab = "Cp", type = "1")
minimum.cp = min(forward_fit.summary$cp)
std.cp = sd(fit.summary$cp)
abline(h = min.cp + 0.2 * std.cp, col = "#010168", lty = 2)
abline(h = min.cp - 0.2 * std.cp, col = "#010168", lty = 2)

#For BIC
plot(fit.summary$bic, xlab = "Number of variables", ylab = "BIC", type='l')
minimum.bic = min(fit.summary$bic)
std.bic = sd(fit.summary$bic)
abline(h = min.bic + 0.2 * std.bic, col = "#010168", lty = 2)
abline(h = min.bic - 0.2 * std.bic, col = "#010168", lty = 2)

#For adjusted R2
plot(fit.summary$adjr2, xlab = "Number of variables", ylab = "Adjusted R2", type = "l", ylim = c(0.4, 0.84))
max.adjr2 = max(fit.summary$adjr2)
std.adjr2 = sd(fit.summary$adjr2)
abline(h = max.adjr2 + 0.2 * std.adjr2, col = "#010168", lty = 2)
abline(h = max.adjr2 - 0.2 * std.adjr2, col = "#010168", lty = 2)

#The different subset predictors give different results. Across the three models the 6 seems to be the best value.
#However, looking at training MSE you could argue 7 would be better. For the time being 6 will be used.

fit = regsubsets(Outstate ~ ., data = College, method = "forward")

coefficient = coef(forward_fit, id = 6)

#Taking a peek at the predictors being used
names(coefficient)

#Part B) Fit a GAM on the training data, using out-of-state tuition as
#the response and the features selected in the previous step as
#the predictors. Plot the results, and explain your findings.

gam_fit = gam(Outstate ~ Private + s(Room.Board, df = 2) + s(PhD, df = 2) +
s(perc.alumni, df = 2) + s(Expend, df = 5) + s(Grad.Rate, df = 2),
data=College.train)

par(mfrow = c(2,3))
plot(gam_fit, se = T, col = "green")

#Graduation Rate and Room & Board are fairly linear. PhD is somewhat linear (if not looking a little crooked).
#Other variables are not linear

# Part C) Evaluate the model obtained on the test set, and explain the
#results obtained.
pred_y = predict(gam_fit, College.test)
MSEerror = mean((College.test$Outstate - pred_y)^2)
#Show the MSE
print(MSEerror)
#Calculate Total Sum of Squares and then show Residual Sum of Squares
TSS = mean((College.test$Outstate - mean(College.test$Outstate))^2)
#Residual Sum of Squares
RSS = 1 - MSEerror/TSS
RSS

#Using GAM and 6 predictors got a test R2 of about 0.795. As a result 79.5% of the variance
# is explained by the model

# Part D) For which variables, if any, is there evidence of a non-linear
# relationship with the response?

summary(gam_fit)

#ANOVA show evidence of a non-linear relationship between the features "Outstate and Expend."
#Additionally if youn consider the p-value as 0.05 then there is a some what strong non-linear relationship between
#"Outstate" and the "Percent of alumni (perc.alumni)." This agrees with earlier observations with 
# percent of alumni in part B is non-linear. 

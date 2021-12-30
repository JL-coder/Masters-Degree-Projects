#Part 1: Split the data set into a training and testing set
#install.packages('ISLR')

view(College)
set.seed(11)
training = sample(1:dim(College)[1], dim(College)[1] / 2)
testing <- -training
College.training <- College[training, ]
College.testing <- College[testing, ]

#Part 2: Fit a linear model using least squares on the training set, and
#report the test error obtained.
fit.lm <- lm(Apps ~ . , data = College.training)
pred.lm <- predict(fit.lm, College.testing)
mse = mean((pred.lm - College.testing$Apps)^2)
#Test error 
print("Test error: ")
print(mse / 10000000)

#Part 3: Fit a ridge regression model on the training set, with λ chosen
#by cross-validation. Report the test error obtained.
#install.packages('glmnet')
library(glmnet)
training.something <- model.matrix(Apps ~ . -1 , data = College.training)
testing.something <- model.matrix(Apps ~ . -1, data = College.testing)
grid <- 10 ^ seq(4, -2, length = 100)
modl.ridge <- cv.glmnet(training.something, College.training[,"Apps"], alpha = 0, lambda = grid, thresh = 1e-12)
lambda.best <- modl.ridge$lambda.min
print("lambda value:")
print(lambda.best)
ridge.pred <- predict(modl.ridge, newx = testing.something, s = lambda.best)
#install.packages("pls")
library(pls)
ridge_mse = mean((College.testing[, "Apps"] - ridge.pred)^2)
print("Test error: ")
print(ridge_mse / 10000000)

#Part 4: Fit a lasso model on the training set, with λ chosen by crossvalidation.
#Report the test error obtained, along with the number
#of non-zero coefficient estimates.
modl.lasso <- cv.glmnet(training.something, College.training[,"Apps"], alpha = 1, lambda = grid, thresh = 1e-12)
lambda.best <- modl.lasso$lambda.min
lasso.pred <- predict(modl.lasso, newx = testing.something, s = lambda.best)
lasso_mse = mean((College.testing[,"Apps"] - lasso.pred)^2)
print("Test error: ")
print(lasso_mse / 10000000)
modl.lasso <- glmnet(model.matrix(Apps ~ . -1, data = College), College[,"Apps"], alpha = 1)
predict(modl.lasso, s = lambda.best, type = "coefficients")
#Number of nonzero coefficients = 18 (IF intercept counts as a coefficent here).

#Part 5: Fit a PCR model on the training set, with M chosen by crossvalidation.
#Report the test error obtained, along with the value
#of M selected by cross-validation.

pcr_fit <- pcr(Apps ~ ., data = College.training, scale = TRUE, validation = "CV")
validationplot(pcr_fit, val.type = "MSEP")
pcr_prediction <- predict(pcr_fit, College.testing, ncomp = 7)
#Fit a PCR Model
validationplot(pcr_fit, val.type = "MSEP")
#Test MSE
pcr_prediction <- predict(pcr_fit, College.testing, ncomp = 7)
pcr_mse <-  mean((College.testing[, "Apps"] - pcr_prediction)^2)
print("Test MSE for PCR: ")
print(pcr_mse / 10000000)

#Part 6: Fit a PLS model on the training set, with M chosen by crossvalidation.
#Report the test error obtained, along with the value
#of M selected by cross-validation.
pls_fit <- plsr(Apps ~ ., data = College.training, scale = TRUE, validation = "CV")
#Fit PLS Model
validationplot(pls_fit, val.type = "MSEP")
pls_pred <- predict(pls_fit, College.testing, ncomp = 7)
pls_mse <- mean((College.testing[,"Apps"] - pls_pred)^2)
print("Test MSE for PLS: ")
print(pls_mse / 1000000)

#Part 7: Comment on the results obtained. How accurately can we predict
#the number of college applications received? Is there much
#difference among the test errors resulting from these five approaches?

average_test <- mean(College.testing[, "Apps"])
linear_r2 = 1 - mean((College.testing[, "Apps"] - pred.lm)^2)/mean((College.testing[, "Apps"] - average_test)^2)
ridge_r2 = 1 - mean((College.testing[, "Apps"] - ridge.pred)^2) /mean((College.testing[, "Apps"] - average_test)^2)
lasso_r2 = 1 - mean((College.testing[, "Apps"] - lasso.pred)^2) /mean((College.testing[, "Apps"] - average_test)^2)
pcr_r2 = 1 - mean((College.testing[, "Apps"] - pcr_prediction)^2) /mean((College.testing[, "Apps"] -average_test)^2)
pls_r2 = 1 - mean((College.testing[, "Apps"] - pls_pred)^2) /mean((College.testing[, "Apps"] -average_test)^2)
par(mfrow = c(1,2))

#Create a bar plot to visualize differences
barplot(c(linear_r2, ridge_r2, lasso_r2, pcr_r2, pls_r2), col="green", names.arg=c("OLS","Ridge", "Lasso", "PCR", "PLS"), main = "Test R-Squared", ylab = "Test R-Squared", ylim = c(0,1))
barplot(c(mse, ridge_mse, lasso_mse, pcr_mse, pls_mse), col="red", names.arg=c("OLS","Ridge", "Lasso", "PCR", "PLS"), main = "Test MSE", ylab = "Test MSE")
#The results for the test R^2 and test MSE are comparable. The only difference is that PCR had a lower test R^2 than the other methods. The lower R^2 translates into a higher MSE which is reflected in the bar graph with PCR having the highest MSE among the different methods.
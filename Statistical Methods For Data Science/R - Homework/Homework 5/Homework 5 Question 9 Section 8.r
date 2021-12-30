#Section 8.4 Question 9
#a) Create a training set containing a random sample of 800 observations,
# and a test set containing the remaining observations.
library('ISLR')
library('caret')
library('tidyverse')
library('rpart')
library('rpart.plot')
library('knitr')
library('kableExtra')
library('tree')
#install.packages('caret')
#install.packages('tidyverse')
#install.packages('ggthems')
#install.packages('rpart.plot')
#install.packages('kableExtra')
attach(OJ)
set.seed(1)

train <- createDataPartition(OJ$Purchase, p = 800/1070, list = FALSE)
training <- OJ[train,]
testing <- OJ[-train,]
purchase.testing = OJ$Purchase[-train]
#b) Fit a tree to the training data, with Purchase as the response
#and the other variables except for Buy as predictors. Use the
#summary() function to produce summary statistics about the
#tree, and describe the results obtained. What is the training
#error rate? How many terminal nodes does the tree have?

model <- rpart(Purchase ~ ., data = training, method = "class",
control = rpart.control(cp = 0))
summary(model, cp=1)
#Based on the summary the most important variable is LoyalCH for determining
#which orange juice the customer will buy. The next most important is Price Difference
#but its not nearly as important. The baseline accuracy for the model is 61.8%

postResample(predict(model, training, type = "class"),
training$Purchase) %>% kable

#The tree model beats the baseline with an accuracy of 86.89%

tree <- tree(Purchase ~ ., data = training)
summary(tree)
#The variables used in the tree construction are LoyalCH, PriceDiff,
# ListPriceDiff, and PctDiscMM. The tree has 7 terminal nodes. The 
#training error on the tree is 15.48%. 

#c) Type in the name of the tree object in order to get a detailed
#text output. Pick one of the terminal nodes, and interpret the
#information displayed.

tree(formula = Purchase ~ ., data = training)

#Interpreting teriminal node 13 - ListPriceDiff > 0.235
#There are 143 observations in the branch.
#It has a deviance of 119.300 with an overall prediction of "CH"
#Finally the fraction of observations in the branch that take on values
#of "CH" and "MM " are 0.8531 and 0.1469 respectivly

#d) Create a plot of the tree, and interpret the results.
plot(tree)
text(tree, pretty=0)

#The most important predictor for purchasing juice is "LoyalCH" with a
#value less than 0.482935 leading to most classifications being "MM."
# Unless the pricediff is greater than 0.31 than its classification
#is "CH". If the value of LoyalCh is greater than 0.76 than the
#classification is "CH" otherwise if the ListpriceDiff < 0.235
#than the classification is either "CH" or "MM" depending on
#which side of the PctdiscMM classification it falls on.
#Otherwise if its greater than the listpricediff than its classified as "CH"

#e)Predict the response on the test data, and produce a confusion
#matrix comparing the test labels to the predicted test labels.
#What is the test error rate?
seed(1000)
prediction = predict(tree, testing, type = "class")
caret::confusionMatrix(prediction, testing$Purchase)
error = round(mean(prediction != purchase.testing)*100, 2)
error
#Accuracy of 81.04%, Sensitivity of 87.8%, Specificity of 70.48%.
#The test error is %18.96 

#f)Apply the cv.tree() function to the training set in order to
#determine the optimal tree size.

cv_model <- train(training[,-1], training[,1], method = 'rpart',
trControl = trainControl(method = 'cv', number = 10),
tuneGrid = expand.grid(cp = seq(0, 0.5, length.out = 10)))
cv_model


#g) Produce a plot with tree size on the x-axis and cross-validated
#classification error rate on the y-axis.
cv.OJ = cv.tree(tree, FUN = prune.misclass)
cv.OJ
#plot(cv.oj$size, cv.oj$dev, type = "b")


#h) Which tree size corresponds to the lowest cross-validated classification
#error rate?

#According to the graph a tree size of 7 would lead to the lowest error rate
#however a tree size of 2 has a similar error rate. I would go with 2 since 
#this will simplify the tree and increase interpretability.

#i) Produce a pruned tree corresponding to the optimal tree size
#obtained using cross-validation. If cross-validation does not lead
#to selection of a pruned tree, then create a pruned tree with five
#terminal nodes.

pruned.OJ = prune.misclass(tree, best=2)
summary(pruned.OJ)
plot(pruned.OJ)
text(pruned.OJ, pretty = 0)
#Misclassification error is 18.48% and residual mean deviance is 95.05%

#j) Compare the training error rates between the pruned and unpruned
#trees. Which is higher? 
summary(tree)
summary(pruned.OJ)
#The unpruned tree has an error of 15.48% while the pruned tree has an 
#error of 18.48%. The unpruned tree performed better than the pruned tree.

#k)Compare the test error rates between the pruned and unpruned
#trees. Which is higher?
test_outcome <- testing$Purchase
test_error_unpruned <- mean(prediction != test_outcome)
test_error_unpruned

pruned_tree_prediction <- predict(pruned.OJ, testing, type = "class")
table(test_outcome, pruned_tree_prediction)
pruned_tree_error <- mean(pruned_tree_prediction != test_outcome)
pruned_tree_error

#The test error of the unpruned tree is 0.1895911 and the test
#error of the pruned tree is 0.2081784. The unpruned tree
#performed better on the test set. 



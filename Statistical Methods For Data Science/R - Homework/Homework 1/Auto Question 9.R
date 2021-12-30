#Homework 1 Question 9
#Question 1
library(readr)
auto <- read_csv("R Related Files/Homework 1/Auto.csv")
auto <- na.omit(auto)
str(auto)
#"horsepower" and "name" are qualitative the rest are quantitative
#Question 2
summary(auto[,-c(4,9)])
#Question 3
sapply(auto[,-c(4,9)], mean)
sapply(auto[,-c(4,9)], sd)
#Question 4
data_subset <- auto[-c(10:85), -c(4,9)]
sapply(data_subset, range)
sapply(data_subset, mean)
sapply(data_subset, sd)
#Question 5
#Use pairs function to get overview of the different relationships
pairs(auto[,-c(4,9)])
plot(auto$weight, auto$displacement, xlab = "Weight", ylab = "Displacement")
#Displacement is a measure of cylinder volue swept by all the pistons of an engine so it would make since that there is 
#a positive correlation between this and weight as bigger engines would have more volume. Lets see if the trend continues
#when comparing weight and horsepower.
plot(auto$weight, auto$horsepower, xlab = "Weight", ylab = "Horsepower")
#Bigger engines tend to have more horsepower. As expected there is a slight positive correlation between weight and
#horsepower. As weight increases there is a increase in horsepower. But does the increase in size and horsepower 
#effect the mpg?
plot(auto$weight, auto$mpg, xlab = "Weight", ylab = "MPG")
#There is a slight negative correlation between the weight and mpg. That means that as weight increases the mpg 
#decreases. This means that as cars increase in size (and possibly get bigger engines to be able to move that increased
#load) we see a decrease in that cars fuel economy.
#Question 6
plot(auto$mpg, auto$year, xlab = "Year", ylab = "MPG")
#Over time cars are getting more efficient. But, I would say there is only a minor correlation compared to other variables that have been investigated previously.
plot(auto$mpg, auto$displacement, xlab = "MPG", ylab = "Displacement")
#There appears to be a negative exponential correlation between MPG and displacement. So displacement greatly effects 
#how efficient a car is. This would be a useful metric for predicting MPG along with weight and mpg.
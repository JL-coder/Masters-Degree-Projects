#Part a
library(readr)
college <- read_csv("R Related Files/College.csv")
#Part b
rownames <- college[,1]
college <- college[,-1]
#Part c.1
summary(college)
#c.2
#Private is a charachter need to change to a factor
college$Private <- as.factor(college$Private)
pairs(college[,1:10])
#c.3
plot(college$Private, college$Outstate, xlab = "Private University", ylab = "Tuition in USD", main = "Out of State Vs Private Tuition")
#c.4
Elite <- rep("No", nrow(college))
Elite[college$Top10perc > 50] <- "yes"
Elite <- as.factor(Elite)
college$Elite <- Elite
summary(college$Elite)
plot(college$Elite, college$Outstate, xlab = "Elite University", ylab = "Out of State tuition in USD", main = "Outstate Tuition vs Elite University")
#c.5
par(mfrow=c(2,2))
hist(college$Grad.Rate, xlab = "Graduation Rate", ylab = "Count", main = " ")
hist(college$Apps, xlab = "Applications Received", ylab = "Count", main = " ")
hist(college$Expend, xlab = "Instructional Expenditure Per Student", main = " ")
hist(college$S.F.Ratio, xlab = "Student tot Faculty Ratio", main = " ")
#c.6
#Its hard to do analysis without knowing the name of the colleges your're supposed to be analyzing unfortunately,
#R makes it almost impossible to reinsert a column at a specific index once removed. So its quicker/easier to reload the
#original file again and work with that for this part of the problem.
college_w_names <- read_csv("R Related Files/College.csv")
row.names(college_w_names)[which.min(college_w_names$Room.Board)]
college_w_names[412,1]
row.names(college_w_names)[which.max(college_w_names$Room.Board)]
college_w_names[38,1]
dev.off()
enrollment_rate <- college_w_names$Enroll / college_w_names$Accept
row.names(college_w_names)[which.min(enrollment_rate)]
college_w_names[211,1]
row.names(college_w_names)[which.max(enrollment_rate)]
college_w_names[78,1]
plot(enrollment_rate, college_w_names$Outstate)
#There appears to be a negative correlation between out of state tution and enrollment rate. Interestingly, the school
# with the highest enrollment rate "California Lutheran University" appears to enroll all the students that apply to the school.
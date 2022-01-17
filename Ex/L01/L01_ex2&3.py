##################################################
### Lecture 01 Exercise 2,3
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Exercise 2
## Assign variables and print my birthday
##################################################
# Assign my birthday to 3 variables (year, month, day) separately
year = 1999
month = 5
day = 17

# create a list to store the date
myBirthday = [year, month, day]

# print myBirthday in a the order of year-month-day
print(myBirthday)

# Update the year variable to the current year (2022)
year = 2022

# Update the list
myBirthday = [year, month, day]

# print again
print(myBirthday)

##################################################
## Exercise 3
## Find RH
##################################################
# Assign useful variables
air_T = 30
dew_pt_T = 25.3
e = 2.71828

# actual vapour pressure
actual_vP = 6.1094 * e ** ((17.625 * dew_pt_T) / (dew_pt_T + 243.04))

# saturated vapour pressure
saturated_vP = 6.1094 * e ** ((17.625 * air_T) / (air_T + 243.04))

# RH
RH = actual_vP / saturated_vP

# print the RH
print(RH * 100, '%')

##################################################
## END
##################################################
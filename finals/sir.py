import numpy as np  # Numpy is the library we needed for this project. In python, we insert libraries using "import" keyword.
import pandas	# 	pandas is also the necessary library.
import datetime 	# datetime is the module (same as library) we needed for calculating the age and number of days between opening date and 30-Apr-2014.

data = pandas.read_csv('/Users/kapil/Desktop/data.csv', delimiter=',')  # We are reading a csv file ( same as excel file ) using read_csv function
																		# which is defined in the pandas library. The whole read file is stored in "data" 
																		# variable. So, data is our dataframe. Now we can have operations on this "data" 
																		# variable.
dob = data.DOB  # DOB is name of coulmn in our csv file of data. Using data.DOB , we are assigning DOB column of data variable to a new variable dob.
od = data.OD 	# OD is name of column in our csv file of data. Using data.OD , we  are assigning OD column of data variable to a new variable od.

age = [] 	# We are defining an empty array called as age. 
ref = datetime.datetime.strptime("30-Apr-14", "%d-%b-%y") # strptime is a name of function in datetime module of datetime library.
for d in dob:			# for loop for accessing each element of date of birth
    if type(d) == float:	
        age.append(d)	# append is a function which adds element to the end of an array.
    else:
        dt = datetime.datetime.strptime(d, "%d-%b-%y")
        if dt.year > 2014:
            dt = dt - datetime.timedelta(weeks=52*100)
            age_in_days = (ref - dt).days / 365
            age.append(age_in_days)    


days = []		# days is an emoty array defined which will be used to store number of days between opening date and 30-APR-2014 for each customers.
for d in od:	# for loop for accessing each element of opening date for each account id
    if type(d) == float:
        days.append(d) # adding value of number of days to the days array
    else:
        try:
            dt = datetime.datetime.strptime(d, "%d/%m/%y")
            if dt.year > 2014:
                dt = dt - datetime.timedelta(weeks=52*100)
                days_in_days = (ref - dt).days
                days.append(days_in_days)
            else:
                days_in_days = (ref - dt).days
                days.append(days_in_days)
        except:
            days.append(None)

data['AGE'] = pandas.Series(age)      # this command is used to insert "AGE" column into our dataset which here is called as "data"
data['DAYS'] = pandas.Series(days)    # this command is used to insert "DAYS" column into our dataset which here is called as "data"

# Above 2 lines of code were used to add 2 more columns like AGE, DAYS into our dataframe object which here is "data"
data = data.drop('AGE', 1)		# Since date of brth column were having many missing values, so do we have for AGE and 
								# hence we are deleting this column from our data.
data = data.drop('DOB', 1)		# Since date of birth column were having many missing values, we are deleting this column from our data.

new_data = data.dropna()		# this line deltes those rows which have any missing value in it form the data. dropna() is a method used for this.

train_X = new_data[["BAL", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "SECU_AMT", "DAYS"]].values 
# the above line of code is defining our input variables. Which variables we want to consider, we need to mention it over here.


train_Y = new_data["FIELD VALUE"].values
# the above line of code is defining our output variables. WHich variables is the final output, we need to mention it over here. Like here
# field value was the output variable which takes only 0 or 1 as values. 0 means customer deserves loan and 1 means customer does not deserves the loan.

import sklearn
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()  # here clf is the object of DecisionTreeClassifier class.
clf = clf.fit(train_X, train_Y) # we are fitting train_X, train_Y data into the clf object.
from sklearn.externals.six import StringIO
import pydot
from sklearn import tree
dot_data = StringIO()

clf = DecisionTreeClassifier(max_depth=4)  # Specifying the depth of the decision tree you want to plot.
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "SECU_AMT", "DAYS"], filled=True, rounded=True, class_names=["Issue Loan", "Don't issue Loan"])
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree4.pdf")





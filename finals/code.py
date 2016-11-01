import numpy as np
import pandas
data = pandas.read_csv('/Users/kapil/Desktop/data.csv', delimiter=',')
data
data.ACCT_NO
data.DOB
data.['DOB']
data['DOB']
dob = data.DOB
dob
type(dob)
for d in dob: print d
for d in dob: print type(d)
for d in dob: print d.dtype
for d in dob: print d
type(1.0) == float
s = '24-Jul-08'
import datetime
datetime.strftime?
datetime.daettime.strftime?
from datetime import strftime
datetime.datetime.strftime?
datetime.datetime.strptime(s, "%d-%b-%y")
datetime.datetime.strptime("24-2-99", "%d-%b-%y")
datetime.datetime.strptime("24-12-99", "%d-%b-%y")
datetime.datetime.strptime("24-Dec-99", "%d-%b-%y")
datetime.datetime.strptime("29-Feb-99", "%d-%b-%y")
ls
a = datetime.datetime.strptime("24-Dec-99", "%d-%b-%y")
a = datetime.datetime.strptime("24-Dec-12", "%d-%b-%y")
a = datetime.datetime.strptime("24-Dec-99", "%d-%b-%y")
b = datetime.datetime.strptime("24-Dec-12", "%d-%b-%y")
(a - b).total_days()
(a - b).total_seconds()
(a - b).days
age = []
ref = datetime.datetime.strptime("30-Apr-14", "%d-%b-%y")
for d in dob:
        if type(d) == float:
            age.append(d)
        else: # d is string
            dt = datetime.datetime.strptime(d, "%d-%b-%y")
            age_in_days = (ref - dt).days
            age.append(age_in_days)
age = []
ref = datetime.datetime.strptime("30-Apr-14", "%d-%b-%y")
for d in dob:
        if type(d) == float:
                age.append(d)
            else:
                    dt = datetime.datetime.strptime(d, "%d-%b-%y")
                    age_in_days = (ref - dt).days
                    age.append(age_in_days)

data['AGE'] = pandas.Series(age)
data.AGE
ref = datetime.datetime.strptime("30-Apr-14", "%d-%b-%y")
ref
dt = datetime.datetime.strptime("01-Jan-66", "%d-%b-%y")
(ref - dt).days
dt
dt.year
dt.year = dt.year - 100
dt.year = dt.year - datetime.timedelta(years=100)
dt.year = dt.year - datetime.timedelta(year=100)
dt.year = dt.year - datetime.timedelta(weeks=52*100)
dt
dt = dt - datetime.timedelta(weeks=52*100)
dt
(ref - dt).years
days = []


for d in od:
        if type(d) == float:
            days.append(d)
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
(ref - dt).year
age = []
ref = datetime.datetime.strptime("30-Apr-14", "%d/%m/%y")
%paste
age
data['AGE'] = pandas.Series(age)
data.AGE
%paste
%paste
%paste
data.OD
data.OD == None
data.OD.fillna(data.OD.mean())
sum([True for idx,row in data.iterrows() if any(row.isnull())])
sum(data.AGE.isnull().values.ravel())
data.size
data.length
len(data)
len(data.dropna())
len(data)
new_data = data.dropna()
len(data)
len(new_data)
new_data.FIELD_VALUE
new_data.FIELDVALUE
new_data.["FIELD VALUE"]
new_data["FIELD VALUE"]
new_data["FIELD VALUE"].values
new_data["FIELD VALUE", "AGE"].values
new_data[["FIELD VALUE", "AGE"]].values
new_data[["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
train_X = new_data[["BAL", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "SECU_AMT", "DAYS"]].values
train_Y = new_date["FIELD VALUE"].values
train_Y = new_data["FIELD VALUE"].values
train_X
train_Y
for t in new_data["LTV (LOAN TO VALUE RATIO)"]:
    print t
new_data["LTV (LOAN TO VALUE RATIO)"][1]
new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] == '#DIV/0!']
new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!']
new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!', ["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!', ["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]]
new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!', ["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
train_X = new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!', ["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALUE RATIO)", "SECU_AMT", "AGE"]].values
train_X.shape
train_Y = new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!',["FIELD VALUE"]].values
train_Y.shape
train_Y
train_Y = new_data.loc[new_data["LTV (LOAN TO VALUE RATIO)"] != '#DIV/0!',"FIELD VALUE"].values
train_Y
import sklearn
train_X
train_Y
import sklearn
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf = clf.fit(train_X, train_Y)
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
from sklearn import tree
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("dtree.pdf")
graph
graph[0].write_pdf("dtree.pdf")
from IPython.display import Image
Image(graph.create_png())
Image(graph[0].create_png())
Image(graph[0].create_png())
graph[0].write_pdf("dtree.pdf")
clf = DecisionTreeClassifier(min_samples_leaf=20)
clf = clf.fit(train_X, train_Y)
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree2.pdf")
clf = DecisionTreeClassifier(max_leaf_nodes=20)
clf = clf.fit(train_X, train_Y)
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
new_data.loc[new_data["FIELD VALUE"] == 1]
clf.feature_importances_
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train_X, train_Y)
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
graph[0].write_pdf("dtree4.pdf")
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree5.pdf")
train_X
train_X[1]
clf = DecisionTreeClassifier(max_depth=4)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree5.pdf")
clf = DecisionTreeClassifier(max_depth=4)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"])
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree5.pdf")
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
clf = DecisionTreeClassifier(max_depth=4)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
clf = DecisionTreeClassifier(max_depth=4)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree4.pdf")
clf = DecisionTreeClassifier(max_depth=5)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree5.pdf")
clf = DecisionTreeClassifier(max_depth=6)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree6.pdf")
clf = DecisionTreeClassifier(max_depth=3, class_weight={0: 1, 1:5})
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree31.pdf")
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train_X, train_Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=["BAL", "OD", "ROI", "LIMSAN_AMT", "DRAW_LIM_AMT", "LOAN_TERM", "OVERDUE", "OLD_SMA", "LTV (LOAN TO VALRATIO)", "SECU_AMT", "AGE"], filled=True, rounded=True, class_names=["Issue Loan", "Don't issue Loan"])
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("dtree3.pdf")
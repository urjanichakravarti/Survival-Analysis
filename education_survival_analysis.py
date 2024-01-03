import numpy as np
import pandas as pd
import plotnine
import seaborn as sns
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter, CoxPHFitter
from sklearn.model_selection import train_test_split
from sklearn import tree
from dtreeviz.trees import *

plotnine.options.figure_size = (5.2, 3.2)
sns.set()
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

# --------------------------  About the Education Datasets --------------------------
"""
This project utilized the Open University Learning Analytics Dataset (OULAD). 
It contains data about courses, students and their interactions with Virtual Learning Environment (VLE) 
for seven selected courses (called modules). Presentations of courses start in February and October - 
they are marked by “B” and “J” respectively. The dataset consists of tables connected using unique identifiers. 
For a detailed column wise explanation, please refer to the README.md file.
"""

# Loading the data
assessments = pd.read_csv("./Data Files/assessments.csv")
courses = pd.read_csv("./Data Files/courses.csv")
studAssess = pd.read_csv("./Data Files/studentAssessment.csv")
studInfo = pd.read_csv("./Data Files/studentInfo.csv")
studReg = pd.read_csv("./Data Files/studentRegistration.csv")


# -------------------------- Preparing the Dataset --------------------------

# Left Joining Required Fields in studInfo and studReg
data = pd.merge(studInfo[["code_module", "code_presentation", "id_student", "num_of_prev_attempts", "final_result"]],
                studReg,
                how="left",
                on=["id_student", "code_module", "code_presentation"])
# Replacing Null Values with 0
data = data.fillna(0)
# Left Joining data and courses to get module_presentation_length for duration calculation
data = pd.merge(data, courses, how="left", on=["code_module", "code_presentation"])
# print(data)

# Calculating Duration
# duration = module_presentation_length if person DID NOT withdraw
# duration = date_unregistration if person DID withdraw
data['duration'] = np.where(data['date_unregistration'] == 0,
                            data['module_presentation_length'],
                            data['date_unregistration'])
print(data)

# Calculating Survival Probability
# if person withdraws, didWithdraw = 1; else didWithdraw = 0
data.loc[data.final_result != "Withdrawn", 'didWithdraw'] = 0
data.loc[data.final_result == "Withdrawn", 'didWithdraw'] = 1

# Visualisation
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x="didWithdraw")
print(data)

# -------------------------- Kaplan Meier --------------------------

plt.figure()
T = data["duration"]
C = data["didWithdraw"]
fitter = KaplanMeierFitter()
fitter.fit(T, event_observed=C, label="KaplanMeier")
fitter.plot_survival_function()

# -------------------------- Cox PH Modelling --------------------------

# Preparing the Cox Modelling Dataset by including qualitative variables and creating dummy variables
data = pd.merge(data,
                studInfo,
                how="left",
                on=["id_student", "code_module", "code_presentation", "num_of_prev_attempts", "final_result"])
data = data[["code_module", "code_presentation", "id_student", "num_of_prev_attempts", "gender", "region",
            "highest_education", "age_band", "studied_credits", "disability", "duration", "didWithdraw"]]

# Including Bins for Number of Credits
bins = [0, 50, 100, 150, 200, 250]
data['binnedCredits'] = pd.cut(data['studied_credits'], bins)
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='binnedCredits', hue='didWithdraw')

# Final Data Cleaning
data.drop('studied_credits', inplace=True, axis=1)
data.drop('id_student', inplace=True, axis=1)
data = pd.get_dummies(data)
print(data)

# Cox Modelling
cph = CoxPHFitter(penalizer=0.1)
cph.fit(data, "duration", event_col="didWithdraw")
cph.print_summary()
plt.figure()
cph.plot()

# -------------------------- Decision Tree --------------------------
data.drop('duration', inplace=True, axis=1)
X = data.drop('didWithdraw', axis=1)
y = data.didWithdraw

# Splitting the dataset into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)
plt.figure()
tree.plot_tree(clf)

# Feature importance
clf.feature_importances_
plt.figure()
feat_importances = pd.Series(clf.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')

# Checking
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='code_module_CCC', hue='didWithdraw')
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='code_module_GGG', hue='didWithdraw')
plt.show()

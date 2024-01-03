import numpy as np
import pandas as pd
import plotnine
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from dtreeviz.trees import *
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter

plotnine.options.figure_size = (5.2, 3.2)
sns.set()
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

# --------------------------  About the Colon Dataset --------------------------
# These public healthcare survival datasets are provided by the survival package in R
# id: id
# study: 1 for all patients
# rx: Treatment - Obs(ervation), Lev(amisole), Lev(amisole)+5-FU
# sex: 1=male
# age: in years
# obstruct: obstruction of colon by tumour
# perfor: perforation of colon
# adhere: adherence to nearby organs
# nodes: number of lymph nodes with detectable cancer
# time: days until event or censoring
# status: censoring status
# differ: differentiation of tumour (1=well, 2=moderate, 3=poor)
# extent: Extent of local spread (1=submucosa, 2=muscle, 3=serosa, 4=contiguous structures)
# surg: time from surgery to registration (0=short, 1=long)
# node4: more than 4 positive lymph nodes
# etype: event type: 1=recurrence,2=death

# Loading the data
colon = pd.read_csv("./Data Files/colon.csv")
print(colon.head())

# Dropping columns with low variance to avoid Convergence Error
columns_to_drop = ['study', 'etype']
colon = colon.drop(columns=columns_to_drop)

# -------------------------- Kaplan Meier --------------------------
T = colon["time"]
C = colon["status"]
fitter = KaplanMeierFitter()
fitter.fit(T, event_observed=C, label="KaplanMeier for colon")
fitter.plot_survival_function()
plt.figure(1)

# -------------------------- Cox PH Modelling --------------------------
cph = CoxPHFitter(penalizer=0.1)
cph.fit(colon, "time", event_col="status")
cph.print_summary()
plt.figure(2)
cph.plot()

# -------------------------- Decision Tree --------------------------
columns_to_include = ['rx', 'sex', 'age', 'obstruct', 'perfor', 'adhere',
                      'nodes', 'differ', 'extent', 'surg', 'node4']
X = colon[columns_to_include]
y = colon.status

# Splitting the dataset into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)
plt.figure(3)
tree.plot_tree(clf)

# Feature Importance
clf.feature_importances_
plt.figure(4)
feat_importances = pd.Series(clf.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')
plt.show()

import numpy as np
import pandas as pd
import plotnine
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from dtreeviz.trees import *
from lifelines import CoxPHFitter

plotnine.options.figure_size = (5.2, 3.2)
sns.set()
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

# --------------------------  About the Ovarian Dataset --------------------------
# These public healthcare survival datasets are provided by the survival package in R
# futime: survival or censoring time
# fustat: censoring status
# age: in years
# resid.ds: residual disease present (1=no,2=yes)
# rx: treatment group
# ecog.ps: ECOG performance status (1 is better, see reference)

# Loading the data
ovarian = pd.read_csv("./Data Files/ovarian.csv")
ovarian = pd.get_dummies(ovarian)
print(ovarian.head())

# -------------------------- Cox PH Modelling --------------------------
cph = CoxPHFitter(penalizer=0.1)
cph.fit(ovarian, "futime", event_col="fustat")
cph.print_summary()
plt.figure()
cph.plot()

# -------------------------- Decision Tree --------------------------
columns_to_include = ['age', 'resid.ds', 'rx', 'ecog.ps', 'resid.ds.name_no', 'resid.ds.name_yes',
                      'ecog.ps.status_bad', 'ecog.ps.status_good', 'rx.group_group 1', 'rx.group_group 2']
X = ovarian[columns_to_include]
y = ovarian.fustat

# Splitting the dataset into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)
plt.figure(2)
tree.plot_tree(clf)

# Feature Importance
clf.feature_importances_
plt.figure(3)
feat_importances = pd.Series(clf.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')
plt.show()

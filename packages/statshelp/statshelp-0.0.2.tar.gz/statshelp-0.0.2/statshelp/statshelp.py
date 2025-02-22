""" 
Methods availables:
    info_lib() -> Informations of importants libs to Data Analysis 
    concepts_analysis()  -> Function to check how type of Hypotesis test based on variables. 
"""

import pandas as pd
from IPython.display import display, Markdown


def info_lib():

    libraries_info = [
    ("import pandas as pd", "Used for data manipulation and analysis, providing data structures like DataFrames.", "df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})"),
    ("import numpy as np", "Supports large, multi-dimensional arrays and matrices, along with mathematical functions.", "arr = np.array([1, 2, 3, 4])"),
    ("import pylab as pl", "Combines features of numpy, scipy, and matplotlib for easy scientific computations.", "pl.plot([1, 2, 3], [4, 5, 6])"),
    
    # Plotting libraries
    ("import matplotlib.pyplot as plt", "A popular library for creating static, animated, and interactive visualizations.", "plt.plot([1, 2, 3], [4, 5, 6]); plt.show()"),
    ("import seaborn as sns", "Built on matplotlib, it provides a high-level interface for statistical graphics.", "sns.scatterplot(x=[1,2,3], y=[4,5,6])"),
    
    # Stats and machine learning libraries
    ("import statsmodels.api as sm", "Provides statistical models and tests for data analysis.", "model = sm.OLS(y, X).fit()"),
    ("import scipy.stats as stats", "Contains statistical functions for probability distributions and hypothesis testing.", "t_stat, p_val = stats.ttest_ind(data1, data2)"),
    ("from scipy import stats", "Provides access to statistical tests and probability functions.", "p_value = stats.ttest_rel(data1, data2)"),
    ("from scipy.stats import mannwhitneyu", "Performs the Mann-Whitney U test for independent samples.", "stat, p = mannwhitneyu(data1, data2)"),
    ("from scipy.stats import chi2_contingency", "Performs a Chi-square test for independence on a contingency table.", "chi2, p, dof, expected = chi2_contingency(table)"),
    
    ("from sklearn.model_selection import train_test_split", "Splits dataset into training and testing sets.", "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)"),
    ("from sklearn.model_selection import KFold", "Splits dataset into K consecutive folds for cross-validation.", "kf = KFold(n_splits=5, shuffle=True, random_state=42)"),
    ("from sklearn.model_selection import cross_val_score", "Performs cross-validation and returns model scores.", "scores = cross_val_score(model, X, y, cv=5)"),
    
    ("from sklearn.preprocessing import StandardScaler", "Standardizes features by removing mean and scaling to unit variance.", "scaler = StandardScaler().fit(X_train)"),
    ("from sklearn.preprocessing import LabelEncoder", "Encodes categorical labels as integers.", "le = LabelEncoder(); y_encoded = le.fit_transform(y)"),
    ("from sklearn.preprocessing import label_binarize", "Binarizes labels for multi-class classification.", "y_bin = label_binarize(y, classes=[0, 1, 2])"),
    
    ("from sklearn.linear_model import LinearRegression", "Performs linear regression modeling.", "model = LinearRegression().fit(X, y)"),
    ("from sklearn.linear_model import LogisticRegression", "Performs logistic regression for classification tasks.", "model = LogisticRegression().fit(X_train, y_train)"),
    
    ("from sklearn.tree import DecisionTreeClassifier", "Implements decision tree classification.", "clf = DecisionTreeClassifier().fit(X_train, y_train)"),
    ("from sklearn.tree import DecisionTreeRegressor", "Implements decision tree regression.", "reg = DecisionTreeRegressor().fit(X_train, y_train)"),

    # Metrics and statistical analysis
    ("from sklearn.metrics import confusion_matrix", "Computes the confusion matrix to evaluate classification performance.", "cm = confusion_matrix(y_true, y_pred)"),
    ("from sklearn.metrics import accuracy_score", "Calculates the accuracy of a classification model.", "accuracy = accuracy_score(y_true, y_pred)"),
    ("from sklearn.metrics import precision_score", "Calculates the precision (positive predictive value) of a model.", "precision = precision_score(y_true, y_pred)"),
    ("from sklearn.metrics import recall_score", "Calculates the recall (sensitivity) of a model.", "recall = recall_score(y_true, y_pred)"),
    ("from sklearn.metrics import roc_auc_score", "Computes the Area Under the Receiver Operating Characteristic Curve (ROC AUC).", "auc = roc_auc_score(y_true, y_prob)"),
    ("from sklearn.metrics import roc_curve", "Computes Receiver Operating Characteristic (ROC) curve points.", "fpr, tpr, thresholds = roc_curve(y_true, y_prob)"),
    ("from sklearn.metrics import classification_report", "Generates a summary report of precision, recall, and f1-score.", "report = classification_report(y_true, y_pred)"),
    ("from sklearn.metrics import f1_score", "Computes the harmonic mean of precision and recall.", "f1 = f1_score(y_true, y_pred)"),
    ("from sklearn.metrics import mean_absolute_error", "Computes the Mean Absolute Error (MAE) between actual and predicted values.", "mae = mean_absolute_error([3, -0.5, 2], [2.5, 0.0, 2])"),
    ("from sklearn.metrics import r2_score", "Computes the R-squared value, a measure of model performance.", "r2 = r2_score([3, -0.5, 2], [2.5, 0.0, 2])"),
    ("from sklearn.metrics import mean_squared_error", "Computes the Mean Squared Error (MSE) for regression models.", "mse = mean_squared_error([3, -0.5, 2], [2.5, 0.0, 2])"),
    ("from sklearn.feature_selection import RFE","Performs Recursive Feature Elimination (RFE) to select the most relevant features for a model.", "rfe = RFE(model, n_features_to_select=20) rfe.fit(X_train, y_train)  # Fit the RFE model col = X_train.columns[rfe.support_]  # Identify selected columns model.fit(X_train[col], y_train)  # Train a new model with selected features"),
   
     # Warnings handling
    ("import warnings", "Suppresses warnings to keep output clean.", 'warnings.filterwarnings("ignore")')
    ]
    libraries_stats = pd.DataFrame(libraries_info, columns=['Library','Description','Code exemplo'])
    
    return display(Markdown(libraries_stats.to_markdown()))


def concepts_analysis():

    concept_list = [
        ('Univariate Analysis','Categorical','Frequency, Mode, Level','Bar Char or Pie Chart','N/A'),
        ('Univariate Analysis','Numerical','Central Tendency(mean,median,mode) and measure of position (min, Q1, median, Q3, max), measure of depression: std, var, skewness, cof','Histogram, density graph, Box, plot','N/A'),
        ('Bivariate Analysis','Continous Vs. Continous','N/A','Pearson correlation or Spearman and regression', 'Scatter plot, Line graph(time)'),
        ('Bivariate Analysis','Categorical Vs. Categorical','Contigency table (two-way)','Stacked bar chart, Grouped bar chart', 'Chi-square test'),
        ('Bivariate Analysis','Continous Vs. Categorical', 'Grooup by categorical column and aggregate for numerical column', 'Grouped nox plot','T-test: If categorical variable has only 2 levels. ANOVA: If categorical variable has more than two levels. **For both tests just apply if all assumptions are satisfied')
    ]    
    concept_list =  pd.DataFrame(concept_list, columns=['Type of test','Type of data','Summarization','Visualization','Test of Independece'])
   
    return display(Markdown(concept_list.to_markdown(index=False)))
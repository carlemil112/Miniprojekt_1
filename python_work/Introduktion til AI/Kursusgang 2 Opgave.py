#!/usr/bin/env python
# coding: utf-8

# # Load data

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = pd.read_csv(r"C:\Users\carle\Desktop\python_work\Introduktion til AI\iris.csv")

# Check for missing values
iris.info()


# # Preprocessing

# In[3]:


# Handle rows with missing values
iris.dropna(inplace=True)

# Define data
X = iris.iloc[:, :2].values  # we only take the first two features for visualization purposes
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)


# # Model training

# In[4]:


# Train kNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_std, y_train)

# Train Naive Bayes classifier
nb = GaussianNB()
nb.fit(X_train_std, y_train);


# # Testing the model

# In[5]:


# Calculate accuracy for training and testing sets
knn_train_accuracy = accuracy_score(y_train, knn.predict(X_train_std))
knn_test_accuracy = accuracy_score(y_test, knn.predict(X_test_std))

nb_train_accuracy = accuracy_score(y_train, nb.predict(X_train_std))
nb_test_accuracy = accuracy_score(y_test, nb.predict(X_test_std))

print("kNN Training Accuracy:", round(knn_train_accuracy, 2))
print("kNN Testing Accuracy:", round(knn_test_accuracy, 2))

print("Naive Bayes Training Accuracy:", round(nb_train_accuracy, 2))
print("Naive Bayes Testing Accuracy:", round(nb_test_accuracy, 2))


# # Visualize decision boundary

# In[7]:


# Define a colormap for plotting decision regions
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Function to plot the decision boundaries
def plot_decision_boundary(classifier, X, y, title):
    h = 0.02  # step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel('Sepal Length (standardized)')
    plt.ylabel('Sepal Width (standardized)')
    plt.title(title)

# Plot decision boundaries with training data
plot_decision_boundary(knn, X_train_std, y_train, 'kNN Decision Boundary (Training Data)')
plt.show()

plot_decision_boundary(nb, X_train_std, y_train, 'Naive Bayes Decision Boundary (Training Data)')
plt.show()

# Plot decision boundaries with test data
plot_decision_boundary(knn, X_test_std, y_test, 'kNN Decision Boundary (Test Data)')
plt.show()

plot_decision_boundary(nb, X_test_std, y_test, 'Naive Bayes Decision Boundary (Test Data)')
plt.show()


# In[ ]:

# Fjern rækker med manglende værdier
iris.dropna(inplace=True)

# Tjek om der stadig er manglende værdier
print(iris.isnull().sum())

import seaborn as sns

# Visualiser data med et parplot
sns.pairplot(iris, hue='target')
plt.show()


from sklearn.model_selection import train_test_split

# Definer dine features (X) og labels/targets (y)
X = iris.drop('target', axis=1).values  # Alle features
y = iris['target'].values  # Labels

# Split data i trænings- og testdata (70% træning, 30% test)
# Brug random_state for at gøre opdelingen reproducerbar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tjek størrelsen af de opdelte datasæt
print(f'Træningsdata: {X_train.shape}, Testdata: {X_test.shape}')


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Vælg to features, f.eks. petal_length og petal_width
X = iris[['petal_length', 'petal_width']].values  # De valgte to features
y = iris['target'].values  # Labels/target

# Del datasættet op i trænings- og testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardisér de to valgte features (vigtigt for kNN)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Træn kNN-modellen
knn = KNeighborsClassifier(n_neighbors=5)  # Brug f.eks. 5 naboer
knn.fit(X_train_std, y_train)

# Test modellen
y_pred_train = knn.predict(X_train_std)
y_pred_test = knn.predict(X_test_std)

# Evaluer modelpræstationen
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f'kNN Træningsnøjagtighed: {train_accuracy:.2f}')
print(f'kNN Testnøjagtighed: {test_accuracy:.2f}')

import numpy as np #lineær algebra
import pandas as pd #Bruges til at læse filen (pd.read_csv)
import matplotlib.pyplot as plt #visualiser dataen
import seaborn as sns #statistisk data visualisering
from sklearn.model_selection import train_test_split #opdeling af data til træning og data til test
from sklearn.ensemble import RandomForestClassifier #Selve algoritmen til random forest
from sklearn.metrics import accuracy_score #Udregner præcisionen af denne random forest (Hvor mange den klassificerer rigtigt som døde og ikke døde ud fra features)


# Læs dataen med pandas:
df = pd.read_csv('titanic.csv')

# Fjern ubrugelige kolonner:
df.drop(['PassengerId','Name', 'Ticket', 'Embarked'], axis=1, inplace=True)

# Bemærk: 'Sex' er kategorisk og skal omdannes til numeriske værdier, da maskinlæringsmodeller ikke kan håndtere tekst direkte
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Håndter manglende værdier i 'Age' ved at erstatte dem med medianen
df['Age'].fillna(df['Age'].median(), inplace=True)

# Se dimensioner af datasættet:
print(df.shape) #Der er altså 891 data, og 12 features
print(df.head()) #viser de første 5 rækker

# Afklar feature vector og mål variablen:
# Bemærk: Når du vælger flere kolonner, skal du bruge dobbelte brackets [[]]
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].values
y = df['Survived'].values

# Del datasættet op i trænings- og testdata:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definer Random Forest-algoritmen
rfc = RandomForestClassifier(n_estimators= 1000, random_state=42) #Kalder Random forest rfc, og sætter random state til 42 her også

# Træn modellen:
rfc.fit(X_train, y_train) #Vælger at træningssættet skal være X_train og y_train defineret tidligere

# Lav forudsigelser baseret på testdata:
y_pred = rfc.predict(X_test) #Prædikterer antallet af døde vha. X_test sættet

# Tjek nøjagtighed:
print('Model accuracy score med 1000 decision-trees: {0:0.4f}'.format(accuracy_score(y_test, y_pred)))


feature_scores = pd.Series(rfc.feature_importances_, index=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']).sort_values(ascending=False)

feature_scores

# Creating a seaborn bar plot

sns.barplot(x=feature_scores, y=feature_scores.index)



# Add labels to the graph

plt.xlabel('Feature Importance Score')

plt.ylabel('Features')



# Add title to the graph

plt.title("Visualizing Important Features")



# Visualize the graph

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Beregn confusion matrix:
cm = confusion_matrix(y_test, y_pred)

# Print confusion matrix:
print('Confusion matrix\n\n', cm)

# Visualisér confusion matrix med seaborn heatmap:
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix for Titanic Survival Prediction')
plt.show()

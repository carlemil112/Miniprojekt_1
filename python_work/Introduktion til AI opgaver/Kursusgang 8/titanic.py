import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Læs data
data = pd.read_csv('titanic.csv')

# Præprocessering
data.drop(['PassengerId', 'Name', 'Cabin', 'Ticket', 'Embarked'], axis=1, inplace=True)
data.dropna(inplace=True)
data['Sex'].replace(['male', 'female'], [1, 0], inplace=True)

# Definer features og mål
X = data[['Age', 'Sex', 'Pclass', 'SibSp', 'Parch', 'Fare']].values
y = data['Survived'].values

# Split datasættet i træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definér parameter-rummet
param_grid = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': [None, 10, 20, 30, 40, 50],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4, 10],
    'bootstrap': [True, False]
}

# Initialiser Random Forest Classifier
rf = RandomForestClassifier(random_state=42)

# Initialiser GridSearchCV
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    n_jobs=-1,  # Brug alle tilgængelige CPU-kerner
    verbose=2,
    scoring='accuracy'
)

# Fit GridSearchCV til træningsdata
grid_search.fit(X_train, y_train)

# De bedste parametre
best_params = grid_search.best_params_
print("Bedste hyperparametre fundet af GridSearchCV:")
print(best_params)

# Bedste score
best_score = grid_search.best_score_
print(f"Bedste krydsvalideringsnøjagtighed: {best_score * 100:.2f}%")

# Brug den bedste model til at lave forudsigelser
best_rf = grid_search.best_estimator_

# Forudsig på trænings- og testdatasættet
y_pred_train = best_rf.predict(X_train)
y_pred_test = best_rf.predict(X_test)

# Beregn nøjagtighed
accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred_test)

print('\nRandom Forest efter hyperparameteroptimering')
print(f' - Training Accuracy: {accuracy_train * 100:.2f}%')
print(f' - Test Accuracy: {accuracy_test * 100:.2f}%')

import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve, auc, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve, auc, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

'### 1. LOAD CSV FILEN OG FJERN INDEKSERINGSKOLONNER ###'
path_to_csv_file = r'C:/Users/carle/Desktop/python_work/Introduktion til AI opgaver/Kursusgang 6/Lektion6-Classification/breast-cancer.csv' # <-- sæt stien ind til csv filen her
df = pd.read_csv(path_to_csv_file)

# Fjern kun 'Unnamed: 0', hvis den findes
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print(df.info())

'### 2. SCATTERPLOT UD FRA UDVALGTE FEATURES ###'
# Konverter 'diagnosis' til numerisk, hvis det er kategorisk
le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])  # 0 for benign, 1 for malign

# Lav scatterplot med farvekodning på diagnosis
df.plot(kind="scatter", x='radius_mean', y='texture_mean', c='diagnosis', cmap='jet', colorbar=True)
plt.show()

'### 3. VÆLG EN BINÆR KLASSIFIER UD FRA BOGEN ###'
model = LogisticRegression()

'### 4. KLARGØR DATA ###'
input = df.drop('diagnosis', axis=1)
output = df['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.20, random_state=42)

'## TRÆNING AF MODEL ##'
model.fit(X_train, y_train)

'### 5. LAV EN CONFUSION MATIRX ###'
pred = model.predict(X_test)
cm = confusion_matrix(y_test, pred)

# Plot Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Predicted B', 'Predicted M'],
            yticklabels=['Actual B', 'Actual M'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

'### 6. LAV EN PLOT AF EN ROC-KURVE ###'
pred_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

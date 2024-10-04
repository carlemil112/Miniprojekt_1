from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import gzip

columns = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income', 'median_house_value']

'## open file and read contents ##'
with gzip.open('housing.tgz', 'rb') as file:
    housing = pd.read_csv(file)
    housing.rename(columns={'housing/': 'longitude'}, inplace=True)

'## are there any missing values? ##'
print(housing.info())

'## remove the text attribute ##'



'### HANDLE THE DATAFRAME THREE DIFFERENT WAYS (CLEAN THE DATA) ###'
housing = housing.drop('ocean_proximity', axis=1)
'## OPTION 1 ## --> drop rows with nan values'
df_dropna = housing.dropna(subset=["total_bedrooms"])
'## OPTION 2 ## --> drop columns with nan values'
df_drop = housing.drop("total_bedrooms", axis=1)
'## OPTION 3 ## --> impute the misssing values'
imputer = SimpleImputer(strategy="median") # strategy can be; mean, most_frequent, (constant, fill_value --> works with text) other methods than SimpleImputer, that are more powerful are KNNImputer and IterativeImputer
'## Train imputer on dataset ##'
imputer.fit(housing)
'## Perform imputation ##'
imputed_np_arr = imputer.transform(housing)
imputed_df = pd.DataFrame(imputed_np_arr, columns=columns)



'### SPLIT DATAFRAME INTO TRANING AND TEST ###'
"CITE Hands-On_With-Machine_Learning: As with all estimators, it is important to fit the scalers to the training data only: never use fit() or fit_transform() " \
"for anything else than the training set. Once you have a trained scaler, you can then use it to transform() any other set, " \
"including the validation set, the test set, and new data. Note that while the training set values will always be scaled to the specified range, " \
"if new data contains outliers, these may end up scaled outside the range. If you want to avoid this, just set the clip hyperparameter to True."

input = imputed_df.drop('median_house_value', axis=1)
output = imputed_df['median_house_value']

#X_train_opt1, X_test_opt1, y_train_opt1, y_test_opt1 = train_test_split()
#X_train_opt2, X_test_opt2, y_train_opt2, y_test_opt2 = train_test_split()
X_train_opt3, X_test_opt3, y_train_opt3, y_test_opt3 = train_test_split(input, output, test_size=0.20, random_state=42)


'### PERFROM STANDARDSCALER SCALING ###'
'## Now we can scale data by training a scaling method on the traning data since this is the distribution we want the ' \
'model to learn and therefore the scaling method to learn ##'
std_scaler = StandardScaler()
housing_num_scaled = std_scaler.fit_transform(X_train_opt3)
'# scale the test set with the trained scaler #'
housing_num_scaled_test = std_scaler.transform(X_test_opt3)

'### TRAINING A REGRESSION MODEL ###'
lin_reg = LinearRegression()
lin_reg.fit(housing_num_scaled, y_train_opt3)


rand_forr_reg = RandomForestRegressor(n_estimators=500, verbose=2)
rand_forr_reg.fit(housing_num_scaled, y_train_opt3)

'### PREDICTIONS ###'
pred = rand_forr_reg.predict(housing_num_scaled_test)
pred_lin_reg = lin_reg.predict(housing_num_scaled_test)

'### CALCULATE ERROR ###'
rmse_rand_forr_reg = mean_squared_error(y_test_opt3, pred, squared=False)
rmse_lin_reg = mean_squared_error(y_test_opt3, pred_lin_reg, squared=False)
print(f"MSE RandomForrestRegressor: {rmse_rand_forr_reg:.2f}$" + '\n' +
      f"MSE LinearRegression: {rmse_lin_reg:.2f}$")
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm as cm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from scipy import stats
import joblib

#reading and inital processing
df = pd.read_csv('Battery_RUL.csv')
df.drop(columns='Cycle_Index', inplace=True)
new_column_names = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'RUL']
df.columns = new_column_names

#removing outliers
old_rows = df.shape[0]
ACCEPTABLE_Z_SCORE = 3
print("num rows before removing outliers: ", old_rows)

for i in range(len(new_column_names)):
  df = df[(np.abs(stats.zscore(df[new_column_names[i]])) < ACCEPTABLE_Z_SCORE)]
new_rows = df.shape[0]

print("num rows after removing outliers: ", new_rows)
print("percentage of rows removed: ", (1 - new_rows/old_rows) * 100)

#creating dataset for model
data = df.drop(['RUL'], axis=1).values
target = df['RUL'].values

#scaling
scaler = StandardScaler()
scaler.fit(data)
scaler.transform(data)

#train-test split
x_train, x_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    random_state=4,
                                                    test_size=0.3,
                                                    shuffle=True)

#model
regr = LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

#results
print("Coefficients: \n", regr.coef_)
print("Mean squared error: %f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %f" % r2_score(y_test, y_pred))

#saving model for persistence
joblib.dump(regr, open('model.sav', 'wb'))
joblib.dump(scaler, open('scaler.pkl', 'wb'))
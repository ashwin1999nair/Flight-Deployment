import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

df=pd.read_csv('deploy_airline_df.csv')

df.drop('Unnamed: 0',axis=1,inplace=True)

X=df.drop('Price',axis=1)
print(X.head())
print(X.shape)
print(X.columns)

y=df['Price']

#splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)



from sklearn.ensemble import RandomForestRegressor
RF_Model=RandomForestRegressor(n_estimators=1500,min_samples_split=2,min_samples_leaf=2,max_features='sqrt'
                               ,max_depth=38)
RF_Model.fit(X_train,y_train)
y_pred_RF=RF_Model.predict(X_test)

#Use pickle to save our model so that we can use it later

import pickle
# Saving model
pickle.dump(RF_Model, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
print(y_pred_RF)
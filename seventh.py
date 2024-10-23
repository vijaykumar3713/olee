# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:19:29 2024

@author: KJC Staff
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
# load dataset
data= pd.read_csv('C:/Users/KJC Staff/Desktop/dataset.csv')

#display
print("Original Data:")
print(data.head())
#missing values
#numeric columns
numeric_columns= data.select_dtypes(include=['float64','int64']).columns
imputer= SimpleImputer(strategy='mean')
data[numeric_columns]= imputer.fit_transform(data[numeric_columns])

#categorical
categorical_columns= data.select_dtypes(include=['object']).columns
imputer= SimpleImputer(strategy='most_frequent')
data[categorical_columns]= imputer.fit_transform(data[categorical_columns])

# encode categorical variables
label_encoders={}
for column in categorical_columns:
    le= LabelEncoder()
    data[column]=le.fit_transform(data[column])
    label_encoders[column]=le
    
#feature scaling
scaler= StandardScaler()
data[numeric_columns]= scaler.fit_transform(data[numeric_columns])    

#training and testing
x= data.drop('target',axis=1)
y=data['target']
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=42)
print("In pre-processed Data: ")
print(x_train.head())
print(y_train.head())
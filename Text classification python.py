# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from  sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score
data ={
       'Day': ['Sunny', 'Windy','Sunny', 'Windy', 'Windy','Sunny', 'Windy','Sunny' ],
       'Temprature' :['Cool','Cool','hot','hot','Cool','hot','hot','hot'],
       'class' :['play','not play','play','play','not play','play','not play','play'],
       }
df= pd.DataFrame(data)
X_raw = df[['Day','Temprature']]
Y_raw = df['class']
onehot_encoder = OneHotEncoder()
X_encoded = onehot_encoder.fit_transform(X_raw).toarray()
label_encoder = LabelEncoder()
Y_encoded = label_encoder.fit_transform(Y_raw)
X_train, X_test,  Y_train, Y_test =train_test_split(X_encoded,Y_encoded,test_size=0.3, random_state=42)
model = GaussianNB()
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)
print("Test Accuracy:" , accuracy_score(Y_test, y_pred))

new_instance = pd.DataFrame([['Windy', 'Cool']], columns=['Day' , 'Temprature'])
new_instance_encoded = onehot_encoder.transform(new_instance).toarray()
predicted_class = model.predict(new_instance_encoded)
predicted_label = label_encoder.inverse_transform(predicted_class)[0]

print("prediction for Day=Windy , Temp=Cool:", predicted_label)


#load processed data  from processed folder
#create model and train the model
#save the model into artifacts folder
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

X_train=pd.read_csv("../data/processed/X_train.csv")
y_train=pd.read_csv("../data/processed/y_train.csv")
X_test=pd.read_csv("../data/processed/X_test.csv")
y_test=pd.read_csv("../data/processed/y_test.csv")
print(X_train)


model=LinearRegression()
model.fit(X_train,y_train)

with open("../artifacts/model.pkl","wb") as f:
    pickle.dump(model,f)
print("Model training completed and model saved to artifacts folder")
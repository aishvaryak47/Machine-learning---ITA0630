import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("regression.csv")

# Separate features and target
X = data[["X"]]
y = data["Y"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict value
prediction = model.predict([[7]])

print("Predicted value for X = 7:", prediction[0])

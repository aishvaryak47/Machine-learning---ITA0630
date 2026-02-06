import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("polynomial.csv")

# Separate features and target
X = data[["X"]]
y = data["Y"]

# Convert to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Create model
model = LinearRegression()

# Train model
model.fit(X_poly, y)

# Predict value
prediction = model.predict(poly.transform([[7]]))

print("Predicted value for X = 7:", prediction[0])

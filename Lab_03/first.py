import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Data
x = np.linspace(0, 20, 100)
y = 2.6 * x + 1.25

# Train/Test Split
x_train = x[:80]
y_train = y[:80]

x_test = x[80:]
y_test = y[80:]

#  Linear Regression from Scratch 
x_mean = np.mean(x_train)
y_mean = np.mean(y_train)

numerator = np.sum((x_train - x_mean) * (y_train - y_mean))
denominator = np.sum((x_train - x_mean) ** 2)

m = numerator / denominator

b = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (b):", b)

# Predictions
y_pred = m * x_test + b

# Plotting 
plt.scatter(x_train, y_train, marker="*", label="Train Data")
plt.scatter(x_test, y_test, marker="*", label="Test Data")
plt.plot(x_test, y_pred, label="Regression Line")
plt.title("Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
x_train,x_test, y_train, y_test = train_test_split(x,y,random_state=42,test_size=0.2)


model = LinearRegression()

x_train =x_train.reshape(-1,1)

model.fit(x_train,y_train)


print(f"Number of dimensions of x_train is: {x_train.ndim}")

print(model.predict([[30]]))


df = pd.read_csv("./archive/Salary_Data.csv")

df.head()

plt.savefig("plot.png")
print("Plot saved successfully as plot.png")

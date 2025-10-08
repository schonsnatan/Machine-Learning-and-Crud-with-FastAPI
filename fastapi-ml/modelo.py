import joblib
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# fake data (size in m^2, rooms, parking spaces) y=price
X = np.array([
    [100, 3, 2],
    [150, 4, 3],
    [120, 2, 1],
    [300, 5, 4],
    [200, 3, 2],
    [250, 4, 3],
    [180, 3, 2],
    [140, 2, 1],
    [320, 5, 4],
    [210, 3, 0],
    [80, 2, 1],
    [400, 6, 4],
    [220, 4, 2],
    [160, 3, 1],
    [350, 5, 3]
])
y = np.array([
    200000, 300000, 180000, 500000, 400000,
    450000, 360000, 220000, 520000, 410000,
    150000, 650000, 420000, 280000, 600000
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())  #will be replaced by GridSearch
])

param_grid = [
    {
        "regressor": [LinearRegression()],
    },
    {
        "regressor": [Ridge()],
        "regressor__alpha": [0.01, 0.1, 1.0, 10.0]
    },
    {
        "regressor": [Lasso()],
        "regressor__alpha": [0.001, 0.01, 0.1, 1.0]
    },
    {
        "regressor": [RandomForestRegressor(random_state=42)],
        "regressor__n_estimators": [50, 100, 200],
        "regressor__max_depth": [None, 5, 10]
    }
]

grid_search = GridSearchCV(
    pipe,
    param_grid,
    cv=5,               
    scoring="neg_mean_squared_error", 
    n_jobs=-1,
    verbose=1,
    refit=True
)

grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Better score (negative MSE):", grid_search.best_score_)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
mse_test = mean_squared_error(y_test, y_pred)
r2_test = r2_score(y_test, y_pred)

print(f"MSE in test: {mse_test:.2f}")
print(f"R² in test: {r2_test:.2f}")

joblib.dump(best_model, "best_regression_model.pkl")
print("✅ Best model pipeline saved to best_regression_model.pkl")

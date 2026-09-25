# Internet Order Delivery Time Prediction

## Project Overview

This project aims to **predict the delivery time of internet orders** using information related to the order, delivery distance, traffic conditions, and the number of active courier orders.

A **Regression model** from the `scikit-learn` library is used to predict the delivery time.

## Dataset

The dataset is stored in `data.xlsx`.

The dataset contains **1001 records** and includes the following input features:

| Column | Description |
|---|---|
| `Distance_km` | Distance of the order destination in kilometers |
| `Item_Count` | Number of items in the order |
| `Traffic_Level` | Traffic level |
| `Active_Courier_Orders` | Number of active orders assigned to couriers |

**20% of the data was used for testing**, while 80% was used for training.

## Problem Type and Model

This is a **Regression problem** because the goal is to predict a numerical value: the **delivery time of an order**.

The model was implemented using the `scikit-learn` library in Python.

### Workflow

1. Load the dataset from `data.xlsx`
2. Select the input features
3. Split the data into training and testing sets
4. Train the regression model
5. Predict the delivery time
6. Evaluate the model using MAE, MSE, and RMSE

## Model Evaluation Metrics

### 1. MAE — Mean Absolute Error

MAE measures the average absolute difference between the actual and predicted values.

**Formula:**

```text
MAE = (1 / n) × Σ |yᵢ − ŷᵢ|
```

**Result: 3.57**

### 2. MSE — Mean Squared Error

MSE measures the average of the squared differences between the actual and predicted values.

**Formula:**

```text
MSE = (1 / n) × Σ (yᵢ − ŷᵢ)²
```

**Result: 19.84**

### 3. RMSE — Root Mean Squared Error

RMSE is the square root of MSE and is expressed in the same unit as the target variable.

**Formula:**

```text
RMSE = √[(1 / n) × Σ (yᵢ − ŷᵢ)²]
```

or:

```text
RMSE = √MSE
```

**Result: 4.45**

## Evaluation Results

| Metric | Formula | Result |
|---|---|---:|
| **MAE** | `(1 / n) × Σ \|yᵢ − ŷᵢ\|` | **3.57** |
| **MSE** | `(1 / n) × Σ (yᵢ − ŷᵢ)²` | **19.84** |
| **RMSE** | `√[(1 / n) × Σ (yᵢ − ŷᵢ)²]` | **4.45** |

### Formula Symbols

| Symbol | Meaning |
|---|---|
| `yᵢ` | Actual delivery time |
| `ŷᵢ` | Predicted delivery time |
| `n` | Number of test samples |
| `Σ` | Sum over all test samples |

## Results Interpretation

- **MAE = 3.57** — The average absolute difference between actual and predicted delivery time is 3.57 time units.
- **MSE = 19.84** — The average squared prediction error is 19.84.
- **RMSE = 4.45** — The root mean squared prediction error is 4.45 time units.

> The exact time unit depends on the target variable used in the dataset.

## Software Output

The following image shows the software output and model results:

![Model Output](a.png)

> Make sure that `output.png` is placed in the same directory as `README.md` so that the image is displayed correctly.

## Project Structure

```text
project/
│
├── data.xlsx
├── output.png
├── README.md
└── ...
```

## Libraries Used

- Python
- Pandas
- Scikit-learn

### Installation

```bash
pip install pandas scikit-learn openpyxl
```

## Conclusion

This project uses a **Regression model** to predict internet order delivery time based on four input features:

- `Distance_km`
- `Item_Count`
- `Traffic_Level`
- `Active_Courier_Orders`

The dataset contains **1001 records**, with **80% used for training and 20% used for testing**.

The final evaluation results are:

| Metric | Result |
|---|---:|
| MAE | **3.57** |
| MSE | **19.84** |
| RMSE | **4.45** |

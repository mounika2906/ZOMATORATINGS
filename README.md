
# Zomato Bangalore Restaurant Rating Prediction

This project aims to predict restaurant ratings in Bangalore using machine learning techniques. We explore and model the Zomato dataset to uncover factors that drive customer ratings and help platforms like Zomato make better recommendations.

---

## Industry Context  
Online food delivery and restaurant discovery platforms like Zomato rely heavily on customer ratings for ranking and recommendations. Accurate predictions improve personalized suggestions, better visibility for new restaurants, and strategic business insights.

## Problem Definition  
Build a machine learning model to estimate restaurant ratings using features like online ordering, table booking, cost, cuisine, votes, and location—helping Zomato improve recommendations and analytics.

## About the Data  
The dataset contains ~51,000 restaurant records from Bangalore with features like `online_order`, `book_table`, `votes`, `rate`, `location`, `rest_type`, `cuisines`, `dish_liked`, `approx_cost(for two people)`, `listed_in(type)`, and `listed_in(city)`.

## Data Preprocessing  
- Dropped irrelevant columns (name, url, phone, etc.).
- Cleaned non-numeric ratings like 'NEW' and '-'.
- Converted 'rate' to float (e.g., "4.1/5" → 4.1).
- Cleaned and converted 'cost' to integer.
- Handled missing values via mode or removal.
- Encoded categorical variables (label encoding).
- Split data: 70% training, 30% testing.

---

## Actionable Insights from EDA
-  Online ordering correlates with higher ratings.
-  Table booking restaurants tend to have better ratings.
-  Extremely high-cost restaurants don’t always receive high ratings.
-  Higher number of votes leads to more stable, reliable ratings.
-   Cuisines like North Indian and Chinese are associated with better ratings.

---

##  Data Preparation  
- Converted all relevant features to numeric.
- Separated features (X) and target (y = `rate`).
- Train-test split: 70/30.

## Model Selection  
- **Linear Regression** – as a baseline.  
- **Random Forest Regressor** – to capture non-linearity.  
- **Extra Trees Regressor** – better generalization and variance control.

## Model Training  
- Trained all models on training data.
- Tuned ensemble parameters:
  - `Random Forest`: n_estimators
  - `Extra Trees`: n_estimators

## Model Evaluation  

| Model                  | R² Score |
|------------------------|----------|
| Linear Regression      | 0.308    |
| Random Forest Regressor| 0.846    |
| Extra Trees Regressor | **0.919** |

**Extra Trees Regressor Metrics**  
- MAE: 0.2457  
- MSE: 0.1062  
- RMSE: 0.3260  

**Best Model: Extra Trees Regressor**

---

## Feature Importance  
Top features influencing ratings:
- `votes`
- `cuisines`
- `dish_liked`
- `location`
- `online_order`

---

## Key Results  
- Best R² Score: **0.919**  
- Online presence (order/table) and cuisine significantly affect ratings.

---

##  Tools & Technologies  
- Python, Pandas, NumPy, Matplotlib, Seaborn  
- Scikit-learn, LabelEncoder  
- Extra Trees Regressor, Random Forest  
- Jupyter Notebook, Joblib  
- Streamlit (for web app UI)  
- AWS EC2 (deployment)

---

##  Conclusion  
This project successfully built a robust ML model to predict restaurant ratings with high accuracy. Insights drawn can aid platforms like Zomato in improving recommendations, ranking strategies, and user satisfaction.



## Software and Tools Requirements
1. [GithubAccount](https://github.com/)
2. [VsCodeIde](https://code.visualstudio.com/)
3. [HerokuAccount](https://www.heroku.com/)
4. [GitCLI](https://git-scm.com/)


create a new environment

...

conda create -p venv python==3.9 -y

...


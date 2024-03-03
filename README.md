# PM2.5 Concentration Prediction

## Introduction
This project aims to predict PM2.5 (particulate matter with a diameter of 2.5 micrometers or less) concentration using machine learning techniques. PM2.5 concentration prediction is crucial for environmental monitoring and public health management, as high levels of PM2.5 can have adverse effects on human health.

## Folder Structure
- **CSV_Data**: Contains CSV files for training and test data.
- **PM25_data**: Contains NetCDF files for PM2.5 data.
- **models**: Contains saved trained models.
- **README.md**: Readme file describing the project.
- **main.py**: Main Python script for data preprocessing, modeling, and evaluation.
- **requirements.txt**: List of dependencies.

## Dependencies
The project requires the following dependencies:
- Python 3.x
- pandas
- numpy
- scikit-learn
- xarray
- matplotlib
- seaborn
- netCDF4
- scipy

You can install the required dependencies using pip:
```bash
pip install -r requirements.txt

Data Preprocessing
Attributes Used for Training:

Various environmental and meteorological variables such as temperature, cloud cover, ozone concentration, etc.
These attributes are connected to PM2.5 concentration as they influence air quality and pollutant levels in the atmosphere.
Code Explanation:

The provided Python script preprocesses the data by reading CSV files containing training and test data.
It performs data cleaning, handling missing values, outlier detection, and transformation of numerical columns.
The data is then split into features (independent variables) and the target variable (PM2.5 concentration).
Model Used: RandomForestRegressor and GradientBoostingRegressor
RandomForestRegressor:

Ensemble learning method that constructs multiple decision trees during training.
Trained with hyperparameters: n_estimators=100, random_state=42.
Known for high accuracy and robustness to overfitting.
GradientBoostingRegressor:

Ensemble learning method that builds decision trees sequentially.
Trained with hyperparameters: n_estimators=100, max_depth=7, min_samples_split=7, min_samples_leaf=3, learning_rate=0.1.
Focuses on improving model performance by correcting errors of the previous model.
Model Training and Evaluation
The RandomForestRegressor and GradientBoostingRegressor models are trained and evaluated using Mean Squared Error (MSE) and R-squared score (R2).
The models' performance is visualized using line graphs to compare actual vs. predicted PM2.5 concentration.
Results
The project generates machine learning models to predict PM2.5 concentration based on environmental variables.
Model evaluation metrics such as MSE and R2 are used to assess model performance.
Conclusion
This project demonstrates the application of machine learning techniques to predict PM2.5 concentration, which is essential for environmental monitoring and public health management.
The RandomForestRegressor and GradientBoostingRegressor models show promising performance in predicting PM2.5 concentration based on environmental variables.

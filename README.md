# PM2.5 Concentration Prediction

## Introduction
This project aims to predict PM2.5 (particulate matter with a diameter of 2.5 micrometers or less) concentration using machine learning techniques. PM2.5 concentration prediction is crucial for environmental monitoring and public health management, as high levels of PM2.5 can have adverse effects on human health.

## Folder Structure
```
- CSV_Data: Contains CSV files for training and test data.
- PM25_data: Contains NetCDF files for PM2.5 data.
- models: Contains saved trained models.
- README.md: Readme file describing the project.
- main.py: Main Python script for data preprocessing, modeling, and evaluation.
- requirements.txt: List of dependencies.
```

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
```


 ## Factors Taken into Account When Training the Model

### Environmental and Meteorological Variables
- Temperature (t2m): Temperature is a crucial factor influencing air quality and PM2.5 concentration. Higher temperatures can accelerate chemical reactions leading to the formation of PM2.5.
- Cloud Cover (cp): Cloud cover affects solar radiation reaching the Earth's surface, which can influence atmospheric stability and pollutant dispersion.
- Low Cloud Cover (lcc): Low cloud cover affects visibility and can trap pollutants near the surface, potentially increasing PM2.5 concentration.
- Ozone Concentration (tco3): Ozone is a key component of photochemical smog and can react with other pollutants to form PM2.5.
- Total Precipitation (tp): Precipitation can scavenge particles from the atmosphere, reducing PM2.5 concentration.
- Other Variables: The model may also consider additional environmental variables such as wind speed, humidity, and atmospheric pressure, which can indirectly affect PM2.5 concentration.

### Geographical Factors
- Latitude and Longitude: Geographical location can influence local sources of pollution, atmospheric dynamics, and weather patterns, all of which contribute to variations in PM2.5 concentration.
- Proximity to Urban Areas: Urban areas typically have higher levels of PM2.5 due to vehicular emissions, industrial activities, and other anthropogenic sources.

### Seasonality and Time Trends
- Month: The model accounts for seasonal variations in PM2.5 concentration, as air quality can vary throughout the year due to factors such as temperature, humidity, and vegetation cycles.
- Time Trends: The model may also consider long-term time trends in PM2.5 concentration, such as changes in emission regulations, industrial activities, and urbanization.

### Land Use and Land Cover
- Vegetation Cover: Vegetation can act as a natural filter for air pollutants, affecting PM2.5 concentration levels.
- Urbanization: The degree of urbanization and land use patterns in an area can influence local emissions and air quality, impacting PM2.5 concentration.

### Socioeconomic Factors
- Population Density: Areas with higher population density may experience higher PM2.5 concentration due to increased vehicular traffic, industrial activities, and energy consumption.
- Socioeconomic Status: Socioeconomically disadvantaged communities may be disproportionately affected by PM2.5 pollution due to factors such as proximity to industrial sites and lack of access to healthcare resources.

### Data Sources and Quality
- Data Sources: The model relies on data from various sources, including ground-based monitoring stations, satellite observations, and numerical weather prediction models.
- Data Quality: Ensuring data quality is essential for accurate model predictions. Quality control procedures may include data validation, outlier detection, and interpolation techniques to address missing or erroneous data points.

By considering these factors, the model aims to capture the complex interactions between environmental, geographical, temporal, and socioeconomic variables that influence PM2.5 concentration levels.


- **Code Explanation**:
  - The provided Python script preprocesses the data by reading CSV files containing training and test data.
  - It performs data cleaning, handling missing values, outlier detection, and transformation of numerical columns.
  - The data is then split into features (independent variables) and the target variable (PM2.5 concentration).

## Model Used: RandomForestRegressor and GradientBoostingRegressor
- **RandomForestRegressor**:
  - Ensemble learning method that constructs multiple decision trees during training.
  - Trained with hyperparameters: n_estimators=100, random_state=42.
  - Known for high accuracy and robustness to overfitting.

- **GradientBoostingRegressor**:
  - Ensemble learning method that builds decision trees sequentially.
  - Trained with hyperparameters: n_estimators=100, max_depth=7, min_samples_split=7, min_samples_leaf=3, learning_rate=0.1.
  - Focuses on improving model performance by correcting errors of the previous model.

## Model Training and Evaluation
- The RandomForestRegressor and GradientBoostingRegressor models are trained and evaluated using Mean Squared Error (MSE) and R-squared score (R2).
- The models' performance is visualized using line graphs to compare actual vs. predicted PM2.5 concentration.

## Results
- The project generates machine learning models to predict PM2.5 concentration based on environmental variables.
- Model evaluation metrics such as MSE and R2 are used to assess model performance.

## Conclusion
- This project demonstrates the application of machine learning techniques to predict PM2.5 concentration, which is essential for environmental monitoring and public health management.
- The RandomForestRegressor and GradientBoostingRegressor models show promising performance in predicting PM2.5 concentration based on environmental variables.

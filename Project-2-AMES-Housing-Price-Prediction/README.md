# DSI Project 2: Sales Price Prediction using Ames Housing Data
---

### Problem Statement
---

The focus of this project is to create a **regression model based on the Ames Housing dataset** to **predict the price of a house at sale, given a set of characteristics of the house**.

Such a model will be useful for people who would like to 'flip' their house (i.e. buy a house at low price, renovate to improve certain features of the house, then sell the house for a gain).

In this project, various models will be developed using regression techniques such as Linear Regression, Lasso Regression, and Ridge Regression.

The models will be cross validated, and evaluated using metrics such as R squared and Mean Squared Error before the final model is selected.


### Executive Summary
---

Based on the final model built with 30 features, it is noted that some features have bigger impact on the SalePrice prediction.

The top 10 features are:

1. Total Area            : Total Area of the house 
2. Overall Qual          : Overall material and finish of the house (evaluated on an ordinal scale) 
3. MS SubClass 020       : MS SubClass - 1-STORY 1946 & NEWER ALL STYLES
4. Mas Vnr Area          : Masonry veneer area in square feet
5. House Style_1Story^   : House Style - One storey
6. Total Bath            : Total number of bathrooms (above grade and in basement)
7. Kitchen Qual          : Kitchen quality (ordinal scale)
8. Exter Qual            : Quality of the material on the exterior (evaluated on an ordinal scale) 
9. Neighborhood_NridgeHt : Neighborhood - Northridge Heights
10. Neighborhood_StoneBr : Neighborhood - Stone Brook

^: negative correlation with SalePrice

The **total area** of the house is the biggest predictor of Sale Price. In this model, **every unit increase in total built area square feet will increase Sale Price by USD 30,860**. 

It is also not surprising that better **overall quality** and **newer houses** (as indicated by MS Subclass 020). **Improving the overall quality score by 1 point will increase the Sale Price by USD 14,884**. 

The **exterior** is also important both in terms of **masonry veneer area** and **quality of the exterior**.

Interestingly, **kitchen quality** and **total number of bathroom** are also strong predictors, which matches what is shown on TV shows such as 'Property Brothers' and 'House Hunter', in which the ladies care a lot about kitchen, and Americans do not seem to like sharing bathrooms.

**One storey** housing has an **inversed relationship with pricing**.

Lastly, **neighborhood** is also key. As the old saying goes, when it comes to housing, it's all 'location, location, 'location'. Neighborhoods such as Northridge Heights and Stone Brook positively impact Sale Price.

House flippers can consider increasing total area by building another storey, if the corresponding increase in Sale Price can offset the cost. 

Other actionable areas include renovation to improve overall quality, kitchen quality and increase the number of bathroom. Unfortunately, it is impossible to change the neighborhood, so the flippers should first ensure that the house they purchase to flip is in a good location like Northridge Heights and Stone Brook.


### Project Approach
---

#### 1. Data

The Ames Housing Dataset is used in this project. It is an exceptionally detailed and robust dataset with many different features related to houses.

The datasets from [DSI-US-6 Regression Challenge](https://www.kaggle.com/c/dsi-us-6-project-2-regression-challenge) were presented in 2  files:
1. train.csv (containing all of the training data for modelling)
2. test.csv (containing the test data for predictions)

The [data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) was also provided.

Additional features created include

| feature       | Description   |     
| :------------ |:--------------|
| Total Area    | Total indoor and outdoor area (Gr Liv Area + Total Bsmt SF + Wood Deck SF + Open Porch SF + Enclosed Porch SF + 3-Ssn Porch + Screen Porch + Pool Area + Garage Area) (in square feet)| 
| Age           | Year Sold minus Year Built (in years)|
| New House     | House with age no more than 25 years |
| Total Bath    | Total number of bathrooms above grade and in basement (Half bath is considered as 0.5 bathroom)|


#### 2. Data Cleaning & EDA

Based on initial data exploration, it is noted that the datasets contain housing transaction record from **year 2006 to 2010**. There are 2051 records in the train dataset, and 879 records in the test dataset.

As part of **Data Cleaning**, the following were performed:
1. Reviewing data types and converting to correct data types (e.g. MS SubClass and Mo Sold).
2. Checking for missing values and imputing missing values. Continuous variables were mostly imputed with median, and discrete variables with mode. Some variables were imputed with appropriate values such as 'NA' or 0 if the missing values correspond to the absent of features (e.g. Garage, Basement).
3. Ordinal variables to mapped to corresponding numeric scale.

As for **Exploratory Data Analysis**, the following were performed:
**Part A: Target Variable (SalePrice)**
* Summary statistics of target variable SalePrice 
* Visualising distribution of target variable SalePrice, in which it is noted that SalePrice is positively skewed.

**Part B: Numeric Continuous Variables**
* Summary statisticss of numeric continuous variables to check for extreme values
* Correlation matrix of numeric continuous variables
* Visusalisation using distplots and scatterplots of variables vs. SalePrice
* Focusing of numeric continuous variables with strong correlation with SalePrice, checking for multicollinearity by looking at the correlation coefficients for exclusion from modelling.

**Part C: Numeric Categorical Variables**
* Correlation matrix of numeric categorical variables
* Visusalisation using boxplots of variables vs. SalePrice
* Focusing of numeric categorical variables with strong correlation with SalePrice, checking for multicollinearity by looking at the correlation coefficients for exclusion from modelling.

**Part D: Nominal Variables**
* Visualisation using countplots, and identify variables with low variance to exclude from modelling.


#### 3. Feature Engineering

Based on the EDA, 2 new features were created:
1. Total Area = Gr Liv Area + Total Bsmt SF + Wood Deck SF + Open Porch SF + Enclosed Porch SF + 3-Ssn Porch + Screen Porch + Pool Area + Garage Area
2. Age = Yr Sold - Year Built
3. New House: 1 corresponds to houses with Age less than or equal 25 years, and 0 for those with Age over 25 years.
4. Total Bath = Full Bath + (Half Bath * 0.5) + Bsmt Full Bath + (Bsmt Half Bath * 0.5)

A set of 24 features were selected based on EDA and the inclusion of new features created.

Among these, One Hot Encoding was applied to nominal variables. The resulting train dataset has 129 features, and a column for SalePrice as target variable.


#### 4. Model Preparation

1. Feature set X and target variable y was set up
2. Train/ test split was applied.
3. Standard Scaler was applied to scale the variables.


#### 5. Modelling

With these initial set of 129 features, the following models were created:
1. Linear Regression
2. Lasso Regression
3. Ridge Regression

Given the large number of features, Lasso Regression was helpful in feature selection.  


#### 6. Model Iteration

Based on the initial Lasso Regression done, 30 features with the highest coefficients (in absolute value) were picked to go into the final model.

Lasso Regression and Ridge Regression were used and compared. Lasso performed marginally better. 

#### 7. Generate Predictions on Test Set

The Lasso Regression with 30 features was then fitted to the whole training dataset to generate the predictions on the test dataset. Given that Power Transform was applied for scaling, predictions were inversed transformed to obtain the final predictions for submission.

The public score on Kaggle is 31661.69157.


### Conclusion & Recommendations
---

Based on the final model built with 30 features, it is noted that some features have bigger impact on the SalePrice prediction.

The top 10 features are:

1. Total Area            : Total Area of the house 
2. Overall Qual          : Overall material and finish of the house (evaluated on an ordinal scale) 
3. MS SubClass 020       : MS SubClass - 1-STORY 1946 & NEWER ALL STYLES
4. Mas Vnr Area          : Masonry veneer area in square feet
5. House Style_1Story^   : House Style - One storey
6. Total Bath            : Total number of bathrooms (above grade and in basement)
7. Kitchen Qual          : Kitchen quality (ordinal scale)
8. Exter Qual            : Quality of the material on the exterior (evaluated on an ordinal scale) 
9. Neighborhood_NridgeHt : Neighborhood - Northridge Heights
10. Neighborhood_StoneBr : Neighborhood - Stone Brook

^: negative correlation with SalePrice


The **total area** of the house is the biggest predictor of Sale Price. In this model, **every unit increase in total built area square feet will increase Sale Price by USD 30,860**. 

It is also not surprising that better **overall quality** and **newer houses** (as indicated by MS Subclass 020). **Improving the overall quality score by 1 point will increase the Sale Price by USD 14,884**. 

The **exterior** is also important both in terms of **masonry veneer area** and **quality of the exterior**.

Interestingly, **kitchen quality** and **total number of bathroom** are also strong predictors, which matches what is shown on TV shows such as 'Property Brothers' and 'House Hunter', in which the ladies care a lot about kitchen, and Americans do not seem to like sharing bathrooms.

**One storey** housing has an **inversed relationship with pricing**.

Lastly, **neighborhood** is also key. As the old saying goes, when it comes to housing, it's all 'location, location, 'location'. Neighborhoods such as Northridge Heights and Stone Brook positively impact Sale Price.

House flippers can consider increasing total area by building another storey, if the corresponding increase in Sale Price can offset the cost. 

Other actionable areas include renovation to improve overall quality, kitchen quality and increase the number of bathroom. Unfortunately, it is impossible to change the neighborhood, so the flippers should first ensure that the house they purchase to flip is in a good location like Northridge Heights and Stone Brook.
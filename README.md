# Final_Project

<<<<<<< HEAD
## Potential Questions

	1. Are their correlations between lack of preventative care and patient outcomes? 
	We can group this based on State.
 
	2. Are their health risks related to sleeping less than seven hours?

## Resources

Data Source: PLACES: Census Tract Data (GIS Friendly Format), 2021 release: https://chronicdata.cdc.gov/500-Cities-Places/PLACES-Census-Tract-Data-GIS-Friendly-Format-2021-/yjkw-uj5s

- Tools: Python 3.7.6, Visual Studio

- Libraries: SKLearn/Scikit-learn, Pandas, Plotly, Maptplotlib, hvPlot

- Model: Supervised Machine Learning

- Database: PostgreSQL

Communication: Slack
=======
Topic: US Health

## Reason topic was selected:
Dataset is large and encompases possible variables that may be related to one another.  It also includes mapping components.  Health is a topic that affects everyone.  We wanted to better understand how health metrics might differ by location.

## Data source
We are using data from the 2021 Places Census data.  This data provides statistical estimates of measures related to health outcomes, prevention, and health risk behaviors for counties in the United State.  These are determined by combining various surveys for the same populations. 
The data is sourced through the The United States Census bureau by counties

https://chronicdata.cdc.gov/500-Cities-Places/PLACES-Census-Tract-Data-GIS-Friendly-Format-2021-/yjkw-uj5s

## Questions we hope to answer with the data
Main Question
- Can we predict a propensity of cancer based on rural or urban classification?

Possible alternative/supplemental questions
- Are there behaviors that can be used to predict a population's medical outcomes such as cancer.
- Is there a difference in medical outcomes for populations based on if they sleep less than 7 hrs a day.
- Are there locations that have differences in their medical outcomes to help identify areas where there may be interventions.
- Does living in metropolitan area lead to higher health risks?
- A specific health factor e.g Is there a correlation between hours of sleep per a night and obesity?


## Communication protocols
The team is using slack to communicate between classes.  We also have a file to help us determine best times to meet outside of class if needed.  We are going to use slack for notifications on updates to the main branch.

## Tools to be used:
- Python
- Jupyter Notebook
- Tableau for mapping
- Postgres for our database

## Steps for pre-processing
Identify which rows we want to keep
Deleting null rows
Create a table that we can use to label the rows as urban, micro-urban, or rural.


## Machine Learning Model

PCA and K-means clustinging will be used to identify unique clusting in the data. Input will be all health related variables and the **RuralUrban** column encoded. The features will be scaled and PCA will be applied to reduce dimensionallity to three components. This will allow the data to be plotted using 3D graphs. Drilling down, each category of data will have clustering applied. This includes preventative service, risk factors, and health outcomes.

A balanced random forest classifier will be used to predict **urban** or **rural** based on feature variables containing percentage of population with health issues, rural population, and urban population. Feature importance will be used to find what features are contributing the most to the models classification. 

A regression model will be used to predict percentage of population with cancer based on input features. Feature variables will be percentage of population with other health issues, rural and urban population, and rural or urban classification.

A regression model will be used to predict percentage of population with cancer based on rural and urban population, along with rural or urban classification. This will convey if there is correlation between the two populations and classification to the cancer rate.

Scaling will be applied to inputs of the regression models but not the balanced random forest.

Other models will be applied if the need arises. 

## Databases

- We are using PostgreSQL hosted by AWS. We are creating two tables. One table contains our county variable (Health related data) and the other has a population density data.In addition, we are using PySpark to transform, load and extract before hosting on a remote server.
- The machine learning model will be connected to the database (PostgreSQL).

![PostgreSQL Schema](images/Schema.png)

>>>>>>> 9594063a194c74ae65e35bb3b8faedf2b26e0e88


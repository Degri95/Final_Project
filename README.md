# Final_Project

Topic: US Health

## Reason topic was selected:
Dataset is large and encompases possible variables that may be related to one another.  It also includes mapping components.  Health is a topic that affects everyone.  We wanted to better understand how health metrics might differ by location.

## Data source
We are using data from the 2021 Places Census data.  This data provides statistical estimates of measures related to health outcomes, prevention, and health risk behaviors for census tracts in the United State.  These are determined by combining various surveys for the same populations.  Each census tract is a small location division that averages about 4,000 inhabitants.  We also reviewed Census data for better health.
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

Preliminary: Random Forest to find weights. (We might do additional models.)

Outputs we are hoping to see a weight for each input to predict the cancer outcome.



## Databases


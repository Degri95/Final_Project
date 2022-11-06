--creating table for places_county
DROP TABLE IF EXISTS county_info CASCADE;
CREATE TABLE county_info (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL,
    CountyName VARCHAR,
    StateDesc VARCHAR
);


DROP TABLE IF EXISTS health_outcomes CASCADE;
CREATE TABLE health_outcomes (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL,
    ARTHRITIS DECIMAL,
    CASTHMA DECIMAL,
    BPHIGH DECIMAL,
    CANCER DECIMAL,
    HIGHCHOL DECIMAL,
    KIDNEY DECIMAL,
    COPD DECIMAL,
    CHD DECIMAL,
    DEPRESSION DECIMAL,
    DIABETES DECIMAL,
    OBESITY DECIMAL,
    TEETHLOST DECIMAL,
    STROKE DECIMAL
);


DROP TABLE IF EXISTS prevention CASCADE;
CREATE TABLE prevention (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL,
    ACCESS DECIMAL,
    CHECKUP DECIMAL,
    DENTAL DECIMAL,
    BPMED DECIMAL,
    CHOLSCREEN DECIMAL,
    MAMMOUSE DECIMAL,
    CERVICAL DECIMAL,
    COLON_SCREEN DECIMAL,
    COREM DECIMAL,
    COREW DECIMAL
);


DROP TABLE IF EXISTS health_risk_behaviors CASCADE;
CREATE TABLE health_risk_behaviors (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL,
    BINGE DECIMAL,
    CSMOKING DECIMAL,
    LPA DECIMAL,
    SLEEP DECIMAL
);


DROP TABLE IF EXISTS health_status CASCADE;
CREATE TABLE health_status (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL,
    MHLTH DECIMAL,
    PHLTH DECIMAL,
    GHLTH DECIMAL
);


DROP TABLE IF EXISTS population CASCADE;
CREATE TABLE county_population (
    CountyFIPS VARCHAR PRIMARY KEY NOT NULL, 
    Density DECIMAL
);

--Merge county info with county_population table
SELECT county_info.CountyFIPS, county_info.CountyName, county_info.StateDesc, county_population.Density
FROM county_info
INNER JOIN county_population
ON county_info.CountyFIPS = county_population.CountyFIPS;


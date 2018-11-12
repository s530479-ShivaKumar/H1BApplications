# H1BApplications
Big Data - 44517
- Roshan Thalal, Santhosh Bonala
- Shiva Kumar Mutukula, Aditya Jyothi Swaroop

## Links
- Repository: [https://github.com/s530479-ShivaKumar/H1BApplications](https://github.com/s530479-ShivaKumar/H1BApplications)  
- Issue Tracker: [https://github.com/s530479-ShivaKumar/H1BApplications/issues](https://github.com/s530479-ShivaKumar/H1BApplications/issues)
## Introduction
We are going to work on H1B Application records from 2016 to 2017. We are going to analyze and find out things like Number of Applications for an Employer.   

## Data Source
We are taking H1B Applications dataset which has employer name, Cities,Zip Codes and so on. This DataSet had records from 2016 to 2017. Dataset is of size 610MB and records from 2016 and 2017. Dataset is a combination of text and numerics, the file extension is .csv and structured
### DataSource: https://www.kaggle.com/evangelize/h1b-visa-applications#H1B.csv
## The Challenge (Big Data Qualifications)
### veracity:  Dataset is trustworthy
### volume: Dataset contains nearly 1.5 Million Records
### variety: Dataset is Structured
### velocity: Dataset is updated frequently
### value: It is valuable because we can track the records of H1B Applicants

## Big Data Questions
- Shiva - For each employer, find the number of applications filed.
- Roshan
- Santhosh - For Each SOC-Code, Total Number of Applications Received ?
- Aditya

## Big Data Solutions
- Shiva - Count of applications filed by an employer.
- Roshan
- Santhosh Bonala
    1. Mapper Input 

    | case_submitted | employer_name         | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status         | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
    |----------------|-----------------------|---------------|----------------|----------------------|---------------|---------------|----------|---------------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
    | 2/23/2016      | DISCOVER PRODUCTS INC | RIVERWOODS    | IL             | 60015                | 1             | 9/30/2016     | 15-1121  | CERTIFIED-WITHDRAWN | 65811                 | Y                  | Year             | 59197           | Year           | 2017 |
    2. Mapper Output/ Reducer Input : `15-1121,1`
    3. Reducer Output: `15-1121,10`
    4. Language: Python
    5. Bar Chart
- Aditya
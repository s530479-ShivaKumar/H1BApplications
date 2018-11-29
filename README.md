# H1BApplications
Big Data - 44517
- Roshan Thalal, Santhosh Bonala
- Shiva Kumar Mutukula, Aditya Jytohiswaroop Malireddy

## Links
- Repository: [https://github.com/s530479-ShivaKumar/H1BApplications](https://github.com/s530479-ShivaKumar/H1BApplications)  
- Issue Tracker: [https://github.com/s530479-ShivaKumar/H1BApplications/issues](https://github.com/s530479-ShivaKumar/H1BApplications/issues)
## Introduction
We are going to work on H1B Application records from 2016 to 2017. We are going to analyze and find out things like Number of Applications for an Employer.   

## Data Source
We are taking H1B Applications dataset which has employer name, Cities,Zip Codes and so on. This DataSet had records from 2016 to 2017. Dataset is of size 610MB and records from 2016 and 2017. Dataset is a combination of text and numerics, the file extension is .csv and structured
### DataSource: https://www.kaggle.com/evangelize/h1b-visa-applications#H1B.csv
## The Challenge (Big Data Qualifications)
1. veracity:  Dataset is trustworthy
1. volume: Dataset contains nearly 1.5 Million Records
1. variety: Dataset is Structured
1. velocity: Dataset is updated frequently
1. value: It is valuable because we can track the records of H1B Applicants

## Big Data Questions
- Shiva - For each employer, find the number of applications filed.
- Roshan - For each states, find the total number of H1B Application.
- Santhosh - For Each SOC-Code, Total Number of Applications Received ?
- Aditya - For each date, find the number of applications filed?

## Big Data Solutions
### Shiva - Count of applications filed by an employer.
- Mapper Input

| case_submitted | employer_name     | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
|----------------|-------------------|---------------|----------------|----------------------|---------------|---------------|----------|-------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
| 9/27/2016      | INFO SERVICES LLC | LIVONIA       | MI             | 48152                | 1             | 9/30/2016     | 15-1199  | WITHDRAWN   | 102000                | Y                  | Year             | 90376           | Year           | 2017 |

- Mapper Output/ Reducer Input : `INFO SERVICES LLC - 1`
- Reducer Output: `INFO SERVICES LLC - 100`     
- Language: Python
- Bar Chart


### Roshan

- Mapper Input 


| case_submitted | employer_name     | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
|----------------|-------------------|---------------|----------------|----------------------|---------------|---------------|----------|-------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
| 9/27/2016      | INFO SERVICES LLC | LIVONIA       | MI             | 48152                | 1             | 9/30/2016     | 15-1199  | WITHDRAWN   | 102000                | Y                  | Year             | 90376           | Year           | 2017 |
- Mapper Output/ Reducer Input : 'MI,1'
- Reducer Output : 'MI 1500'
- Language: Python
-Bar Chart


### Santhosh
- Mapper Input 

    | case_submitted | employer_name         | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status         | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
    |----------------|-----------------------|---------------|----------------|----------------------|---------------|---------------|----------|---------------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
    | 2/23/2016      | DISCOVER PRODUCTS INC | RIVERWOODS    | IL             | 60015                | 1             | 9/30/2016     | 15-1121  | CERTIFIED-WITHDRAWN | 65811                 | Y                  | Year             | 59197           | Year           | 2017 |
    2. Mapper Output/ Reducer Input : `15-1121,1`
    3. Reducer Output: `15-1121,10`
    4. Language: Python
    5. Bar Chart
    
## Aditya

- Mapper Input 

| case_submitted | employer_name     | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
|----------------|-------------------|---------------|----------------|----------------------|---------------|---------------|----------|-------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
| 11/3/2015      | SUNTRUST BANKS INC | ATLANTA       | GA             | 30308                | 1             | 10/1/2016     | 13-2099  | 	CERTIFIED-WITHDRAWN   | 71750.0                | Y                  | Year             | 59405.0           | Year           | 2017 |

- Mapper Output/ Reducer Input : `11/3/2015 - 1`
- Reducer Output: `11/3/2015 - 200`     
- Language: Python
- Bar Chart

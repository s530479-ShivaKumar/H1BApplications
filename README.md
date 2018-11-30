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
We are taking H1B Applications dataset which has employer name, Cities,Zip Codes and so on. This DataSet had records from 2016 to 2017. Dataset is of size 610MB and records from 2016 and 2017. Dataset also contains about 15 fields. Dataset is a combination of text and numerics, the file extension is .csv and structured
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

- Mapper Output/ Reducer Input : `INFO SERVICES LLC , 1`
- Reducer Output: `INFO SERVICES LLC , 100`     
- Language: Python
- Bar Chart
![shimg](https://user-images.githubusercontent.com/31738370/49255125-ad4ceb00-f3f0-11e8-9b2d-9de336900fdd.PNG)
### Top 5 employers who filed max number of applications	 
![top5](https://user-images.githubusercontent.com/31738370/49255203-e71df180-f3f0-11e8-8a44-f61e8b3a5a54.PNG)

### summary
The highest number of applications filed by employers is as follows
1. INFOSYS LIMITED - 37874 Applications
2. TATA CONSULTANCY SERVICES LIMITED - 25840 Applications
3. CAPGEMINI AMERICA INC - 25088 Applications
4. IBM INDIA PRIVATE LIMITED - 17488 Applications
5. WIPRO LIMITED - 15168 Applications



### Roshan

- Mapper Input 


| case_submitted | employer_name     | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
|----------------|-------------------|---------------|----------------|----------------------|---------------|---------------|----------|-------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
| 9/27/2016      | INFO SERVICES LLC | LIVONIA       | MI             | 48152                | 1             | 9/30/2016     | 15-1199  | WITHDRAWN   | 102000                | Y                  | Year             | 90376           | Year           | 2017 |
- Mapper Output/ Reducer Input : 'MI,1'
- Reducer Output : 'MI 1500'
- Language: Python
-Result 

![graph](https://user-images.githubusercontent.com/42624428/49266674-b18efd80-f41c-11e8-9f1e-3e464f2c2256.PNG)

###Top 14 states that filled most H1B Applicaion in 2016 and 2017



![graph2](https://user-images.githubusercontent.com/42624428/49267000-fb2c1800-f41d-11e8-9c9f-6143ecd9b420.PNG)





### Santhosh
- Mapper Input 

    | case_submitted | employer_name         | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status         | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
    |----------------|-----------------------|---------------|----------------|----------------------|---------------|---------------|----------|---------------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
    | 2/23/2016      | DISCOVER PRODUCTS INC | RIVERWOODS    | IL             | 60015                | 1             | 9/30/2016     | 15-1121  | CERTIFIED-WITHDRAWN | 65811                 | Y                  | Year             | 59197           | Year           | 2017 |
- Mapper Output/ Reducer Input : `15-1121,1`
- Reducer Output: `15-1121,10`
- Language: Python
- Results
![soc_code count](https://raw.githubusercontent.com/s530479-ShivaKumar/H1BApplications/master/SanthoshBonala/images/output.PNG)
    - The highest number of applications where filed in categories mentioned below
        1. 15-1121 (Computer Systems Analysts) - 596950 Applications
        2. 15-1132 (Software Developers) - 538554 Applications
        3. 15-1131 (Computer Programmers) - 433401 Applications
        4. 15-1199 (Computer Occupations) - 214834 Applications
- Summary:
    I have calculated the number of H1B applications received under particular SOC_CODE(Category). The top four categories under which huge amount of applications were received.
    
## Aditya

- Mapper Input 

| case_submitted | employer_name     | employer_city | employer_state | employer_postal_code | total_workers | decision_date | soc_code | case_status | wage_rate_of_pay_from | full_time_position | wage_unit_of_pay | prevailing_wage | pw_unit_of_pay | year |
|----------------|-------------------|---------------|----------------|----------------------|---------------|---------------|----------|-------------|-----------------------|--------------------|------------------|-----------------|----------------|------|
| 11/3/2015      | SUNTRUST BANKS INC | ATLANTA       | GA             | 30308                | 1             | 10/1/2016     | 13-2099  | 	CERTIFIED-WITHDRAWN   | 71750.0                | Y                  | Year             | 59405.0           | Year           | 2017 |

- Mapper Output/ Reducer Input : `11/3/2015, 1`
- Reducer Output: `11/3/2015, 200`     
- Language: Python
- Bar Chart
![capture](https://user-images.githubusercontent.com/31738366/49253307-f484ad00-f3eb-11e8-8e8e-cd6602770412.PNG)
### Top 6 dates on which applications filed:
![capture1](https://user-images.githubusercontent.com/31738366/49256693-7e854380-f3f5-11e8-8125-82a814b0a360.PNG)

### Summary:
- I have calculated the number of H1B Applications filed for each date from 2009 to 2017 period, and the most applications are filed in the month of March 2017. 
- For each year from 2012 to 2017, the number of applications filed during the month of March are more.
- For each year from 2012 -2017, the number of applicatons filed during the months od december and january are less when compared to other months.





# SAT and ACT Analysis


### Problem Statement

In this project, the main focus is to analyse a dataset comprising of participation rates and mean test scores by states for the year 2017 and 2018, with the aim to **identify ways to improve SAT participation rate for the College Board**.


### Executive Summary

From the data analysis and additinal secondary research, **state contracts and state funded test are key drivers to SAT participation**. 

Among states that showed strong increase in SAT participate in 2018, such as Illinois, Colorado, and Rhode Island, the uptake in SAT participation rate is linked to College Board winning state contracts, in which high school students are offered state-funded SAT test.

It is recommended that the College Board focuses on developing partnership with states that do not have any prevailing contract awarded to either the College Board or ACT, and currently have low SAT participation in 2018. Examples of such states include Iowa, Kansas, and South Dakota.


### Project Approach

#### 1. Data

Four datasets were provided for the purpose of this project: 
1. **SAT 2017**, which contains the participation rate and test scores by state for SAT in 2017
2. **ACT 2017**, which contains the participation rate and test scores by state for ACT in 2017
3. **SAT 2018**, which contains the participation rate and test scores by state for SAT in 2018
4. **ACT 2018**, which contains the participation rate and test scores by state for ACT in 2018


#### 2. Data Cleaning

The following data cleaning was done before Exploratory Data Analysis:
1. The 2017 datasets were imported and checked for errors against data sources available online:
For SAT: https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/
For ACT: https://www.act.org/content/dam/act/unsecured/documents/cccr2017/ACT_2017-Average_Scores_by_State.pdf
2. Data errors identified were fixed accordingly.
3. SAT 2017 and ACT 2017 were merged into a Combined 2017 dataset.
4. The 2018 datasets were imported and and aligned to similar format as the 2017 data. 
5. SAT 2018 and ACT 2018 were merged into a Combined 2018 dataset.
6. The Combined dataset for each year is then merged into a Final dataset for further Exploratory Data Analysis.

**Data Dictionary**

|Feature|Type|Dataset|Description|
|:---|:---|:---|:---|
|state|object|ACT/SAT|Name of state from which data is collected| 
|participation_sat_2017|int|SAT|Percentage of graduating high school students participated in SAT in 2017|
|reading_sat_2017|int|SAT| Average score of Evidence-based reading and writing section for SAT in 2017|
|math_sat_2017|int|SAT|Average score of Math section for SAT in 2017|
|total_sat_2017|int|SAT|Average total SAT score for SAT in 2017|
|participation_act_2017|int|ACT|Percentage of graduating high school students participated in ACT in 2017|
|english_act_2017|float|ACT|Average score of English section for ACT in 2017|
|math_act_2017|float|ACT|Average score of Math section for ACT in 2017|
|reading_act_2017|float|ACT|Average score of Reading section for ACT in 2017|
|science_act_2017|float|ACT|Average score of Science section for ACT in 2017|
|composite_act_2017|float|ACT|Average Composite score for ACT in 2017|
|participation_sat_2018|int|SAT|Percentage of graduating high school students participated in SAT in 2018|
|reading_sat_2018|int|SAT| Average score of Evidence-based reading and writing section for SAT in 2018|
|math_sat_2018|int|SAT|Average score of Math section for SAT in 2018|
|total_sat_2018|int|SAT|Average total SAT score for SAT in 2018|
|participation_act_2018|int|ACT|Percentage of graduating high school students participated in ACT in 2018|
|english_act_2018|float|ACT|Average score of English section for ACT in 2018|
|math_act_2018|float|ACT|Average score of Math section for ACT in 2018|
|reading_act_2018|float|ACT|Average score of Reading section for ACT in 2018|
|science_act_2018|float|ACT|Average score of Science section for ACT in 2018|
|composite_act_2018|float|ACT|Average Composite score for ACT in 2018|


#### 3. Exploratory Data Analysis

The following exploratory data analysis were conducted:
1. Identify the states with highest/ lowest participation rate for each test in each year.
2. Identify the states with highest/ lowest mean total/ composite score for each test in each year.
3. Idenfity the states with 100% participation on a given test have a rate change year-to-year.
4. Identify the states show have >50% participation on both tests either year.


#### 4. Data Visualisation

1. Histograms were plotted using matplotlib to explore the distribution of participation rate and mean test score for each test in each year.
2. Scatterplots were plotted using seaborn to explore relationship between various combination of data features.
3. Boxplots were plotted using seaborn to examine the descriptive statistics of various data features.


#### 5. Descriptive and Inferential Statistics

The application of Central Limit Theorem was discussed based on the exploratory data analysis and data visualisation.


#### 6. Outside Research 

Further secondary research were conducted to explore any reason driving SAT participation rate year-on-year change in 2018.

Source: 
https://www.edweek.org/ew/articles/2018/10/31/sat-scores-rise-as-number-of-test-takers.html
https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html
https://co.chalkbeat.org/2015/12/23/21092477/goodbye-act-hello-sat-a-significant-change-for-colorado-high-schoolers


### Conclusion & Recommendations

Based on the analysis conducted, sharp increase in SAT participation rate is seen year-on-year in 2018 for **Colorado** and **Illinois**, along with decline in ACT participation, indicates conversion from ACT to SAT. 

**Rhode Island** also saw a notable increase in SAT participation year-on-year.

Understanding the driver behind this uptake in SAT participation may present opportunity to map the same strategy to other states to boost SAT participation rate. 

Further secondary research shows that **state contracts and state funded test** are key driver of SAT participation rate in Colorado, Illinois and Rhode Island in 2018.

According to report from *Education Week*, in 2017-2018, 10 states (**Colorado**, Connecticut, Delaware, Idaho, **Illinois**, Maine, Michigan, New Hampshire, **Rhode Island**, and West Virginia) and the District of Columbia **covered the cost of the SAT for all their public school students**. Three years prior to that, only three states and the District of Columbia did so.

**State contracts and state funded test are key drivers to SAT participation**. It is recommended that the College Board **focuses on developing partnership with states that do not have any prevailing contract awarded to either the College Board or ACT, and currently have low SAT participation in 2018.**

Examples of such states include Iowa, Kansas, and South Dakota.

Source: https://www.edweek.org/ew/section/multimedia/states-require-students-take-sat-or-act.html



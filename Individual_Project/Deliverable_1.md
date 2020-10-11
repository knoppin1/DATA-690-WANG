# DATA 609 - Individual Project
## Ken Noppinger

## Instructions

- Find an issue that you are passionate about or are interested in as the topic for this exploratory data analysis project.
- Make sure there are publicly available data about this issue to perform exploratory analysis.
- The analysis should include descriptive statistics, data visualization, and optionally statistical inference.

## Deliverable #1 - Project Proposal in Markdown format

- Write and submit a research proposal in the **Markdown** format that answers the following questions:

---

### 1. What is your issue of interest (provide sufficient background information)?

The prevalence of COVID-19 in the most densely populated places in the US will be explored. 

Since March 2020, the COVID-19 virus has been raging through the US and around the world. To date, there are 37.5 million cases worlwide and there are almost 8 million 
cases within the US.  During the spring, it was learned that the virus can be spread airborne through droplets and since that discovery there has been a significant 
emphasis placed on social distancing and wearing masks by health organizations and both state and federal governments. This analysis will shed light on the impact of 
population density relative to the virus spread.  

The goal is to determine which densely populated places in the US have done a better job of containing the spread of the virus.  

---

### 2. Why is this issue important to you and/or to others?

This topic is important because the metrics reported by Johns Hopkins (https://coronavirus.jhu.edu/map.html), 
Microsoft (https://bing.com/covid), and Worldometers (https://www.worldometers.info/coronavirus) all fall short in considering population density.

These sites primarily show statistics for active, recovered, and fatal cases. There is some reporting of tests, cases, and deaths per million people,
but the actual density of those areas has not been a factor in the reporting.  This reporting fails to show data based on "closeness", which is important 
given that the virus is known to spread person-to-person in close distances.  It stands to reason that comparison of densely populated areas will better 
identify the places that have statistically been more or less affected.  

Knowing this information will provide insight into those places whose local policies may be working better than others in containing the virus in lieu of a vaccine.

---

### 3. What questions do you have in mind and would like to answer?

- What counties in the US are the most populated?
- What counties in the US are the most densely populated?
- What counties in the US have the most confirmed cases of COVID-19?
- Are the most densely populated counties represented in the counties with the highest case counts?  If not, which ones?
- How do case counts in densely populated counties compare to counts in counties with the highest rates of cases per million people?  Is there a correlation?

---

### 4. Where do you get the data to help answer your questions? 

The following COVID-19 data files will be referenced from the Johns Hopkins Resource Center (note - these files are updated daily):
- Daily Reports - https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/10-07-2020.csv
- Time Series Data - https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv 

The following file provides population estimates for all counties in the US (note - 2019 estimates will be used):
- https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/PopulationEstimates.xls

The following census data file will be used to extract the county land area information needed for the study:
- https://www.census.gov/library/publications/2011/compendia/usa-counties-2011.html

All of these files contain a FIPS code (Federal Information Processing Standard state code) column that uniquely identifies the counties.  Data will be loaded into
dataframes and merged on this column as appropriate to consolidate the data of interest for the study.

---

### 5. What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units do you expect to analyze?

The main unit for analyis is a "county" in the US.  

There are 3275 counties in the data set to be used for the study.

---

### 6. What variables/measures do you plan to use in your analysis?

Key variables or metrics to the study are:
- County Population
- County Land Area (Sq. Miles)
- County Population Per Square Mile
- Confirmed Cases (both aggregate and over time)
- Confirmed Cases Per Million Population
- Confirmed Cases Per Square Mile

---

### 7. What kinds of techniques do you you plan to use (for example, summary statistics, scatter plot, bar chart, chi-squared test)? 

Summary statistics such as Count, Mean, Range, Standard Deviation will be identified for each variable.

Scatter plots and histograms will be displayed to characterize the different variables under study.

Line or bar charts will compare COVID-19 aggregate data in counties identified as most densely populated.

Time series line or bar charts will compare COVID-19 spread in counties identified as most densely populated. 

---
## COMPLETE

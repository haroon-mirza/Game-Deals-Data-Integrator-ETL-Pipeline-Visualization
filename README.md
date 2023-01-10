# cheapsharkETL

An ETL pipeline that calls the Cheapshark API, transforms data into CSV, and uploads into a Postgres database. Database is then connected to Power BI for further visualizations.

# Architecture
![Cheapshark ETL](https://user-images.githubusercontent.com/110737193/211638208-a243de53-7a44-4a0e-9a0f-ee094048a742.PNG)

Containerized through Docker, ochestrated by Prefect, dashboard created through Power BI

1. Call and extract data from Cheapshark API. Transforms and converts data into CSV.
2. Load transformed data into Postgres Database, which is then connected to Power BI for further visualizations.

# Dashboard
![dashboard](https://user-images.githubusercontent.com/110737193/211638552-4746ec72-da9c-4878-9d7e-a698093d0009.PNG)
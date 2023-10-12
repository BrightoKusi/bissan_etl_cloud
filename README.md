# bissan_etl_cloud


Bissan Exports is an international company focused on exporting locally manufactured products to destination countries.

They have a well-structured database of all of their sales and employees.
Bissan company provides some stipend for employees who choose to go on vacations.
As the Data Engineer, you have been given access to their Employees Database and drive URL to build a Data Mart based on the questions posed by the Business Executives.

You are also to house their data on an off-prem storage like AWS cloud platform. Build a warehouse for their business analysis.


-- Tools and Dependencies
- Python
- AWS
- Boto3
- Psycopg2
- Pandas
- s3fs
- Redshift-connector
- sqlalchemy


-- Actions
- Create an s3 bucket(data lake).
- Create tables to match the source database housing the data.
- Fetch data from source to data lake.
- Create a warehouse using redshift serverless.
- Create a dev schema as initial destination storage and fetch data from data lake into it.
- Create a staging schema which is transformed in granularity and aggregation to meet the business needs of the data analysts, scientists and other users of the data.



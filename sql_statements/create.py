#================================================ For DEV(raw_data)  schema
schema_name = 'raw_data'

departments = '''CREATE TABLE IF NOT EXISTS raw_data.departments(
   _id VARCHAR PRIMARY KEY NOT NULL,
    department VARCHAR,
    salary NUMERIC,
    entitled_bonus INTEGER); '''  

banks = '''CREATE TABLE IF NOT EXISTS raw_data.banks
(
    _id VARCHAR PRIMARY KEY NOT NULL ,
    code INTEGER,
    name VARCHAR
);'''



employees = '''CREATE TABLE IF NOT EXISTS raw_data.employees(
            id INTEGER PRIMARY KEY NOT NULL 
            , department_id VARCHAR (8)
            , highest_education_level VARCHAR
            , years_of_experience INTEGER
            , name VARCHAR (50)
);'''



appraisals = '''CREATE TABLE IF NOT EXISTS raw_data.appraisals(
            id INTEGER PRIMARY KEY NOT NULL
            , employee_id INTEGER
            , last_appraisal_score INTEGER
            , appraised_by VARCHAR
);'''



#============================================== For STAR SCHEMA
dim_departments = ''' CREATE TABLE IF NOT EXISTS staging.dim_departments(
            id BIGINT IDENTITY (1, 1)
            , department VARCHAR (15)
            , salary NUMERIC (7,2)
            , entitled_bonus INTEGER
); '''  

dim_employees = '''CREATE TABLE IF NOT EXISTS staging.dim_employees(
            id BIGINT IDENTITY (1, 1)
            , department_id VARCHAR (8)
            , highest_education_level VARCHAR
            , experience_level VARCHAR
            , name VARCHAR (50)
);'''

dim_appraisals = '''CREATE TABLE IF NOT EXISTS staging.dim_appraisals(
            id BIGINT IDENTITY (1, 1)
            , employee_id INTEGER
            , appraised_by VARCHAR
            , worker_value
);'''

ft_employees_details = '''CREATE TABLE IF NOT EXISTS staging.ft_employees_details(
            id BIGINT IDENTITY (1, 1)
            , employee_id INTEGER
            , department_id VARCHAR
            , appraisal_id INTEGER
            , salary NUMERIC(7,2)
            , entitled_bonus NUMERIC
            , total_income  NUMERIC
            , years_of_experience INTEGER
            , last_appraisal_score INTEGER
            , worker_value VARCHAR
);'''

raw_data_tables = ['departments', 'employees', 'appraisals']

transformed_tables = ['dim_departments', 'dim_employees', 'dim_appraisals', 'ft_employees_details']

dim_departments = '''INSERT INTO staging.dim_departments(
            _id 
            , department 
            , salary 
            , entitled_bonus 
)
SELECT _id, department, salary, entitled_bonus FROM departments
; '''  


dim_employees = '''INSERT INTO staging.dim_employees(
            id 
            , department_id 
            , highest_education_level
            , experience_level
            , name 
)
SELECT _id, department_id, highest_education_level
, CASE WHEN (years_of_experience > 7) then 'high experience' ELSE 'low experience' END AS experience_level
, name 
FROM employees
;'''


dim_appraisals = '''INSERT INTO staging.dim_appraisals(
            id 
            , employee_id 
            , appraised_by
            , worker_value
)
SELECT id, employee_id, appraised_by 
,CASE WHEN (last_appraisal_score > 8) then 'indispensible' ELSE 'replaceable' END AS worker_value
FROM appraisals;'''


ft_employees_details = '''CREATE TABLE IF NOT EXISTS staging.ft_employees_details(
            employee_id 
            , department_id 
            , appraisal_id 
            , salary 
            , entitled_bonus
            , total_income
            , years_of_experience  
            , last_appraisal_score
)
SELECT e._id, d._id, a.id, d.salary, d.entitled_bonus, (d.salary + d.entitled_bonus) as total_income 
,e.years_of_experience, a.last_appraisal_score
FROM employees e 
LEFT JOIN departments d
    ON e.department_id = d._id
LEFT JOIN appraisals a
    ON e._id = a.employee_id
;'''


transformed_queries = ['dim_departments','dim_employees', 'dim_appraisals', 'ft_employees_details']
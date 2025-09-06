# Stage 1: Easy-Level Queries

## Q1. How do vaccination rates correlate with a decrease in disease incidence?
SELECT c.iso_3_code, c.country_name, c.year,
       AVG(c.coverage) AS avg_coverage,
       AVG(i.incidence_rate) AS avg_incidence
FROM coverage_data c
JOIN incidence_rate i 
     ON c.iso_3_code = i.iso_3_code AND c.year = i.year
GROUP BY c.iso_3_code, c.country_name, c.year
ORDER BY year;


# Q2. What is the drop-off rate between 1st dose and subsequent doses?

SELECT iso_3_code, country_name, year, antigen,
       (target_number - doses)::FLOAT / NULLIF(target_number,0) AS drop_off_rate
FROM coverage_data;

# Q3. Has the rate of booster dose uptake increased over time?

SELECT year, antigen,
       AVG(coverage) AS avg_booster_coverage
FROM coverage_data
WHERE coverage_category_description ILIKE '%booster%'
GROUP BY year, antigen
ORDER BY year;

# Q4. Which regions have high disease incidence despite high vaccination rates?

SELECT c.iso_3_code, c.country_name, c.year, c.coverage, i.incidence_rate
FROM coverage_data c
JOIN incidence_rate i 
     ON c.iso_3_code = i.iso_3_code AND c.year = i.year
WHERE c.coverage > 80 AND i.incidence_rate > 50
ORDER BY i.incidence_rate DESC;


## Stage 2: Medium-Level Queries

# Q1. Correlation between vaccine introduction and decrease in disease cases
SELECT r.country_name, r.disease, r.year,
       SUM(r.cases) AS total_cases,
       v.intro
FROM reported_cases r
JOIN vaccine_intro v
     ON r.iso_3_code = v.iso_3_code AND r.year = v.year
GROUP BY r.country_name, r.disease, r.year, v.intro
ORDER BY r.country_name, r.disease, r.year;

# Q2. Which diseases show the most reduction in cases due to vaccination?

SELECT disease, 
       (MAX(cases) - MIN(cases)) AS reduction_in_cases
FROM reported_cases
GROUP BY disease
ORDER BY reduction_in_cases DESC;

# Q3. Are there disparities in vaccine introduction timelines across WHO regions?
SELECT who_region, description AS vaccine,
       MIN(year) AS first_intro_year,
       MAX(year) AS last_intro_year
FROM vaccine_intro
WHERE intro = 'Yes'
GROUP BY who_region, vaccine
ORDER BY vaccine, who_region;

# Q4. Gaps in coverage for high-priority diseases (e.g., TB, Hepatitis B)

SELECT country_name, year, antigen, coverage
FROM coverage_data
WHERE antigen IN ('TB', 'HEPB')
ORDER BY country_name, year;

# Stage 3: Scenario-Based Queries

# Scenario 1: Identify regions with low vaccination coverage

SELECT who_region, country_name, year, AVG(coverage) AS avg_coverage
FROM coverage_data c
JOIN vaccine_intro v ON c.iso_3_code = v.iso_3_code
GROUP BY who_region, country_name, year
HAVING AVG(coverage) < 50
ORDER BY avg_coverage ASC;

# Scenario 2: Evaluate measles campaign effectiveness (last 5 years)

SELECT r.country_name, r.year, r.disease, SUM(r.cases) AS measles_cases
FROM reported_cases r
WHERE r.disease = 'MEASLES' AND r.year >= EXTRACT(YEAR FROM CURRENT_DATE) - 5
GROUP BY r.country_name, r.year, r.disease
ORDER BY r.year;

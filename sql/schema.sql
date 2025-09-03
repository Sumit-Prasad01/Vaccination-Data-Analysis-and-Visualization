CREATE TABLE coverage_data (
    id SERIAL PRIMARY KEY,
    iso_3_code VARCHAR(3),
    country_name VARCHAR(100),
    year INT,
    antigen VARCHAR(50),
    antigen_description TEXT,
    coverage_category VARCHAR(50),
    coverage_category_description TEXT,
    target_number INT,
    doses INT,
    coverage FLOAT
);

CREATE TABLE incidence_rate (
    id SERIAL PRIMARY KEY,
    iso_3_code VARCHAR(3),
    country_name VARCHAR(100),
    year INT,
    disease VARCHAR(50),
    disease_description TEXT,
    denominator TEXT,
    incidence_rate FLOAT
);

CREATE TABLE reported_cases (
    id SERIAL PRIMARY KEY,
    iso_3_code VARCHAR(3),
    country_name VARCHAR(100),
    year INT,
    disease VARCHAR(50),
    disease_description TEXT,
    cases INT
);

CREATE TABLE vaccine_intro (
    id SERIAL PRIMARY KEY,
    iso_3_code VARCHAR(3),
    country_name VARCHAR(100),
    who_region VARCHAR(20),
    year INT,
    description TEXT,
    intro VARCHAR(10)
);

CREATE TABLE vaccine_schedule (
    id SERIAL PRIMARY KEY,
    iso_3_code VARCHAR(3),
    country_name VARCHAR(100),
    who_region VARCHAR(20),
    year INT,
    vaccinecode VARCHAR(50),
    vaccine_description TEXT,
    schedule_rounds VARCHAR(20),
    targetpop VARCHAR(50),
    targetpop_description TEXT,
    geoarea VARCHAR(50),
    ageadministered VARCHAR(50),
    sourcecomment TEXT
);
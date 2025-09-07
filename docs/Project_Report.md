# Vaccination Data Analysis Project

## 📌 Project Overview
This project focuses on analyzing vaccination data across countries to understand vaccine coverage, disease incidence, vaccine introductions, and vaccine schedules.  
The pipeline integrates **data cleaning, database management (PostgreSQL), and visualization (Power BI)** to answer all project questions.

---

## 🔄 Project Pipeline

### 1. Data Collection & Cleaning
- Collected 4 datasets:  
  - Coverage Data  
  - Incidence Rate Data  
  - Reported Cases Data  
  - Vaccine Introduction Data  
  - Vaccine Schedule Data  
- Cleaned and preprocessed datasets using Python (pandas).  
- Ensured consistent column naming, removed nulls, and standardized datatypes.  

### 2. Database Integration (PostgreSQL)
- Designed normalized relational schema.  
- Created tables for all datasets (`coverage_data`, `incidence_rate`, `reported_cases`, `vaccine_intro`, `vaccine_schedule`).  
- Loaded cleaned CSV files into PostgreSQL using SQLAlchemy.  

### 3. Visualization (Power BI)
- Connected PostgreSQL database to Power BI.  
- Built **4 dashboard pages** to answer analysis questions.  

---

## 📊 Power BI Dashboard Pages

### 🔹 Page 1 – Coverage Overview
- **Map Visualization**: Vaccine coverage across countries.  
- **Bar/Line Charts**: Coverage by antigen, category, and year.  
- **Filters**: Country, Antigen, Year.  

✔️ Answers: Coverage distribution, trends, and country-level analysis.

---

### 🔹 Page 2 – Disease Trends
- **Line Chart**: Incidence rate trends over years (per disease).  
- **Bar Chart**: Reported cases by disease.  
- **Filters**: Country, Year.  

✔️ Answers: Which diseases are most common, how incidence rates evolve over time.

---

### 🔹 Page 3 – Vaccine Introduction
- **Timeline Chart**: Vaccines introduced by year.  
- **Table**: Country-wise vaccine introductions.  
- **Filters**: Country, Vaccine.  

✔️ Answers: When vaccines were introduced and variations across countries.

---

### 🔹 Page 4 – Vaccine Schedule
- **Matrix Table**: Vaccine schedules (age vs. vaccine).  
- **Detailed Table**: Country, vaccine, schedule.  
- **Filters**: Country, Vaccine.  

✔️ Answers: At what age vaccines are scheduled and differences in schedules.

---

## ✅ Outcomes
- A complete **data-to-dashboard pipeline**.  
- PostgreSQL ensures structured storage.  
- Power BI dashboards (4 pages) **answer all questions in the project report**.  
- Easy-to-use filters make the analysis interactive and user-friendly.  

---


## 👨‍💻 Tech Stack
- **Python**: Data cleaning & preprocessing  
- **PostgreSQL**: Database design & storage  
- **SQLAlchemy**: Database connection & data loading  
- **Power BI**: Dashboard visualization  

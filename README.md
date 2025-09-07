
# 🧪 Vaccination Data Analysis Project

## 📌 Overview
This project analyzes global vaccination data to answer key questions about vaccine coverage, disease incidence, vaccine introductions, and vaccination schedules.  
The solution integrates **Python, PostgreSQL, and Power BI** to build an end-to-end data pipeline and interactive dashboards.

---

## 🚀 Features
- Data cleaning & preprocessing of raw vaccination datasets.  
- PostgreSQL database with normalized schema for structured storage.  
- Data validation pipeline to ensure quality.  
- Power BI dashboards with **4 interactive pages**:  
  1. **Coverage Overview** → Vaccine coverage trends & map.  
  2. **Disease Trends** → Incidence rate & reported cases.  
  3. **Vaccine Introduction** → Introduction timelines & country details.  
  4. **Vaccine Schedule** → Age-wise vaccine schedules across countries.  

---

## 🛠️ Tech Stack
- **Python** → Data cleaning, preprocessing, and EDA.  
- **PostgreSQL** → Database schema & storage.  
- **SQLAlchemy** → Database integration & data loading.  
- **Power BI** → Interactive dashboards & analysis.  

---

## 📂 Project Structure
```
Vaccination Project/
│── data/                 # Raw & cleaned datasets (CSV/Excel)
│── database/             # SQL schema, database creation & data push scripts
│── notebooks/            # EDA Code & Visuals
│── eda/                  # Exploratory Data Analysis notebooks/scripts
│── scripts/              # Data cleaning & preprocessing scripts
│── powerbi/              # PBIX Power BI dashboard files
│── README.md             # Project documentation
│── Vaccination_Project_Documentation.md  # Detailed pipeline write-up
```

---

## ⚙️ Setup Instructions
1. Clone the repository.  
2. Create a virtual environment and install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Create PostgreSQL database and schema:  
   ```bash
   python database/create_db.py
   ```  
4. Push cleaned data into PostgreSQL:  
   ```bash
   python database/data_pusher.py
   ```  
5. Open **Power BI** and connect to the PostgreSQL database.  

---

## 📊 Dashboard Preview
- **Page 1:** Coverage Overview (map + bar/line charts)  
- **Page 2:** Disease Trends (line & bar charts)  
- **Page 3:** Vaccine Introduction (timeline + tables)  
- **Page 4:** Vaccine Schedule (matrix + detailed table)  

---

## ✅ Outcomes
- A fully working **data-to-dashboard pipeline**.  
- Answers all project report questions.  
- Easy-to-use filters & visuals for insights.  

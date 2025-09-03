# Vaccination-Data-Analysis-and-Visualization


## Project Structure 

```
vaccination_project/
│── data/
│   ├── raw/                  # Original datasets (CSV, Excel, etc.)
│   ├── cleaned/              # Cleaned datasets after preprocessing
│
│── scripts/
│   ├── data_cleaning.py      # Handle missing values, formatting
│   ├── eda.py                # Exploratory data analysis scripts
│   ├── sql_queries.sql       # SQL table creation & insertion
│
│── database/
│   ├── schema_design.sql     # Normalized schema
│   ├── dump/                 # Exported SQL dumps (for backup/sharing)
│
│── powerbi/
│   ├── dashboards.pbix       # Power BI project file
│   ├── visuals/              # Exported dashboard screenshots
│
│── docs/
│   ├── project_report.md     # Detailed documentation
│   ├── requirements.txt      # Python dependencies
│   ├── README.md             # High-level project overview
│
│── outputs/
│   ├── charts/               # PNG/JPEG plots from EDA
│   ├── reports/              # Generated reports or PDFs
│
└── .gitignore                # If using Git
```
# Automated Data Warehouse – Weather & City Integration
This project is an end-to-end ETL (Extract, Transform, Load) pipeline designed to automatically collect weather data, combine it with local city information, and load everything into a PostgreSQL data warehouse.
It serves as a practical demonstration of modern data engineering concepts, including API extraction, CSV processing, data cleaning, warehouse modeling, and automated loading.
📌 Project Overview
The goal of this project is to automate the creation of a small data warehouse containing:
A dimension table of cities
A fact table of daily weather data
The pipeline performs the following steps automatically:
Extract
Weather data from a public JSON file (replacing OpenWeather API)
Local city details from a CSV file
Transform
Clean column names
Merge datasets on city names
Prepare rows for fact/dimension tables
Load
Automatically initialize the PostgreSQL schema
Insert cleaned and merged data into the warehouse
The system is modular, easy to adapt, and designed for real-world educational use.

1. Clone the project
git clone <your_repository_url>
cd project/
2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Copy the example file:
cp .env.example .env
Edit .env and update your PostgreSQL configuration:
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=weather_warehouse
5. Run the ETL pipeline
python -m src.main
6. Expected Output
Database schema is created automatically
CSV and JSON data are extracted
Data is cleaned and merged
City dimension and weather fact table are populated
A clean log of operations is displayed in the terminal


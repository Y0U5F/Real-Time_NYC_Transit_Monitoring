# 📁 Project Structure Documentation

This document describes the organized structure of the Real-Time NYC Transit Monitoring project.

## Directory Structure

```
Real-Time_NYC_Transit_Monitoring/
│
├── README.md                    # Main project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── Dockerfile                   # Docker container configuration
├── entrypoint.sh                # Container entrypoint script
│
├── src/                         # Source code
│   ├── pipeline/                # Main pipeline code
│   │   ├── __init__.py
│   │   ├── orchestrator.py      # Prefect orchestration (main entry point)
│   │   │
│   │   ├── ingestion/           # Data ingestion layer
│   │   │   ├── __init__.py
│   │   │   └── gtfs_scrapper.py # Downloads GTFS data from MTA API
│   │   │
│   │   ├── bronze/              # Bronze layer (raw data)
│   │   │   ├── __init__.py
│   │   │   └── load_to_duckdb.py # Loads raw data to DuckDB
│   │   │
│   │   ├── silver/              # Silver layer (cleaned/standardized data)
│   │   │   ├── __init__.py
│   │   │   └── dbt_nyc_transit/ # DBT project for transformations
│   │   │       ├── dbt_project.yml
│   │   │       ├── profiles.yml
│   │   │       └── models/
│   │   │           └── staging/
│   │   │               ├── schema.yml
│   │   │               ├── sources/
│   │   │               └── *.sql (staging models)
│   │   │
│   │   └── gold/                # Gold layer (analytical/star schema)
│   │       ├── __init__.py
│   │       ├── load_to_snowflake.py # Loads data to Snowflake
│   │       └── transformation.py    # Creates star schema
│   │
│   └── utils/                   # Utility functions
│       └── __init__.py
│
├── docs/                        # Documentation
│   ├── images/                  # Images and diagrams
│   │   ├── _workflow_chart.png
│   │   ├── _batching_dash.png
│   │   ├── _streaming_dash.png
│   │   └── mta_star_schema.jpeg
│   └── presentations/           # PDF presentations
│       ├── NYC_transit_overview.pdf
│       └── nyc_transit_presentation.pdf
│
├── config/                      # Configuration files
│
└── data/                        # Data files (gitignored)
    └── batch_files/             # Downloaded GTFS files
```

## Pipeline Flow

1. **Ingestion** (`src/pipeline/ingestion/`)
   - Downloads GTFS data from MTA API
   - Extracts ZIP files to `data/batch_files/`

2. **Bronze Layer** (`src/pipeline/bronze/`)
   - Loads raw CSV files into DuckDB
   - Creates `data/nyc_transit_bronze.duckdb`

3. **Silver Layer** (`src/pipeline/silver/`)
   - DBT transformations for data cleaning
   - Standardizes schemas and data types
   - Creates staging tables in Snowflake

4. **Gold Layer** (`src/pipeline/gold/`)
   - Loads data from DuckDB to Snowflake
   - Creates star schema (dimensions and facts)
   - Final analytical tables

5. **Orchestration** (`src/pipeline/orchestrator.py`)
   - Coordinates all pipeline steps using Prefect
   - Manages scheduling and error handling

## Running the Pipeline

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python -m src.pipeline.orchestrator
```

### Docker
```bash
# Build and run
docker build -t nyc-transit-pipeline .
docker run -p 4200:4200 nyc-transit-pipeline
```

## Key Files

- **orchestrator.py**: Main pipeline entry point using Prefect
- **gtfs_scrapper.py**: Downloads MTA GTFS data
- **load_to_duckdb.py**: Bronze layer data loading
- **load_to_snowflake.py**: Loads data to Snowflake raw_data schema
- **transformation.py**: Creates star schema in Snowflake
- **dbt_nyc_transit/**: DBT project for Silver layer transformations


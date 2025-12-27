import subprocess
import sys
from pathlib import Path
from datetime import timedelta
from prefect import flow, task

# Get project root directory (3 levels up from this file: src/pipeline/orchestrator.py)
PROJECT_ROOT = Path(__file__).parent.parent.parent
SCRIPTS_DIR = Path(__file__).parent


@task(name="Run GTFS Scrapper")
def run_script_01():
    script_path = SCRIPTS_DIR / "ingestion" / "gtfs_scrapper.py"
    subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(PROJECT_ROOT))


@task(name="Load to DuckDB")
def run_script_02():
    script_path = SCRIPTS_DIR / "bronze" / "load_to_duckdb.py"
    subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(PROJECT_ROOT))


@task(name="Load to Snowflake")
def run_script_03():
    script_path = SCRIPTS_DIR / "gold" / "load_to_snowflake.py"
    subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(PROJECT_ROOT))


@task(name="Run dbt")
def run_dbt():
    # Run dbt and capture output (dbt has a logging bug that causes exit code 1 even on success)
    dbt_dir = SCRIPTS_DIR / "silver" / "dbt_nyc_transit"
    result = subprocess.run(
        ["dbt", "run"], 
        cwd=str(dbt_dir), 
        capture_output=True, 
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    # Check if dbt actually succeeded (look for success message, not exit code)
    if "Completed successfully" not in result.stdout and result.returncode != 0:
        raise RuntimeError(f"dbt run failed with exit code {result.returncode}")


@task(name="Python Transformation")
def run_script_04():
    script_path = SCRIPTS_DIR / "gold" / "transformation.py"
    subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(PROJECT_ROOT))


@flow(name="NYC Transit Pipeline", log_prints=True)
def nyc_transit_pipeline():
    run_script_01()
    run_script_02()
    run_script_03()
    run_dbt()
    run_script_04()


if __name__ == "__main__":
    from prefect.client.schemas.schedules import IntervalSchedule
    
    # Run immediately on startup
    print("🚀 Running pipeline immediately...")
    nyc_transit_pipeline()
    
    # Then serve with 10-day schedule
    print("📅 Starting scheduler (every 10 days)...")
    nyc_transit_pipeline.serve(
        name="nyc-transit-pipeline",
        schedule=IntervalSchedule(interval=timedelta(days=10))
    )

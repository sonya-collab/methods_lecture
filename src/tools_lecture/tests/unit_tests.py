import os
import pandas as pd
from src.tools_lecture.data import generate_data
from src.tools_lecture.analysis import analyse_data
import os.path

# This will produce the path to the test data on any OS and machine,
# if run inside unit_tests.py

# Strictly needed
TEST_DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", 'tests', 'test_data')
)

def test_data_generator():
    generated_data = generate_data()

    raw_data_path = os.path.join(TEST_DATA_DIR, 'raw_data.parquet')
    saved_raw_data = pd.read_parquet(raw_data_path)

    if not generated_data.equals(saved_raw_data):
        raise ValueError("Generated data does not match the saved raw_data.parquet")
    
def test_analyse_data():
    raw_data_path = os.path.join(TEST_DATA_DIR, 'raw_data.parquet')
    raw_data = pd.read_parquet(raw_data_path)

    fit_results = analyse_data(raw_data=raw_data)

    fit_results_path = os.path.join(TEST_DATA_DIR, 'fit_results.parquet')
    expected_fit_results = pd.read_parquet(fit_results_path)

    if not fit_results.equals(expected_fit_results):
        raise ValueError("Analyzed data does not match the expected fit_results.parquet")
    
def test_full_analysis():
    test_data_generator()
    test_analyse_data()

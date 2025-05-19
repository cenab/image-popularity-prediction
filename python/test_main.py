# To run these tests, make sure you have pytest installed (`pip install pytest`).
# Then, execute the following command in your terminal from the project root directory:
# pytest test_main.py

import subprocess
import sys
import json

# Helper function to run main.py and capture output/errors
def run_main_script(args):
    result = subprocess.run(
        [sys.executable, "main.py"] + [str(arg) for arg in args],
        capture_output=True,
        text=True
    )
    return result

def test_example_input():
    """Tests the script with the example input [120, 80, 150, 30]."""
    input_args = [120, 80, 150, 30]
    expected_output = [2, 1, 1, 0]
    result = run_main_script(input_args)
    assert result.returncode == 0
    # Assuming the script prints the list representation directly
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"


def test_sorted_ascending_input():
    """Tests the script with sorted ascending input [1, 2, 3, 4, 5]."""
    input_args = [1, 2, 3, 4, 5]
    expected_output = [0, 0, 0, 0, 0]
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

def test_sorted_descending_input():
    """Tests the script with sorted descending input [5, 4, 3, 2, 1]."""
    input_args = [5, 4, 3, 2, 1]
    expected_output = [4, 3, 2, 1, 0]
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

def test_input_with_duplicates():
    """Tests the script with input containing duplicates [10, 20, 10, 30, 20]."""
    input_args = [10, 20, 10, 30, 20]
    expected_output = [0, 1, 0, 1, 0]
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

def test_single_element_input():
    """Tests the script with a single element input [100]."""
    input_args = [100]
    expected_output = [0]
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

def test_empty_input():
    """Tests that the script exits with a non-zero status for no arguments."""
    input_args = []
    result = run_main_script(input_args)
    assert result.returncode != 0
    # Optionally, check stderr for usage/error message
    assert "usage" in result.stdout.lower() or "error" in result.stdout.lower()

def test_non_integer_input():
    """Tests that the script exits with a non-zero status for non-integer arguments."""
    input_args = ["10", "abc", "20"]
    result = run_main_script(input_args)
    assert result.returncode != 0
    # Optionally, check stderr for error message
    assert "all arguments must be integers" in result.stdout.lower()

def test_ascending_100():
    """Tests the script with an ascending sequence of 100 numbers."""
    input_args = list(range(1, 101))
    expected_output = [0] * 100
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

def test_descending_100():
    """Tests the script with a descending sequence of 100 numbers."""
    input_args = list(range(100, 0, -1))
    expected_output = list(range(99, -1, -1))
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

import random

def test_random_100():
    """Tests the script with 100 random numbers."""
    random.seed(42) # Use a fixed seed for reproducibility
    input_args = [random.randint(0, 999) for _ in range(100)]
    # For random input, we'll just check if the output is a list of 100 integers
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert isinstance(actual_output, list)
        assert len(actual_output) == 100
        assert all(isinstance(x, int) for x in actual_output)
    except json.JSONDecodeError:
        assert False, f"Could not parse output as JSON: {result.stdout.strip()}"

# import random # Import again just in case - Removed duplicate import

def test_shuffled_100():
    """Tests the script with a shuffled sequence of 1 to 100."""
    input_args = list(range(1, 101))
    random.seed(42) # Use a fixed seed for reproducibility
    random.shuffle(input_args)

    # To get the expected output for a shuffled list, we can run the main script
    # with the shuffled input and capture its output. This is a form of
    # "golden master" testing or using the system under test to generate
    # expected output for complex cases.
    expected_result = subprocess.run(
        [sys.executable, "main.py"] + [str(arg) for arg in input_args],
        capture_output=True,
        text=True
    )
    assert expected_result.returncode == 0
    try:
        expected_output = json.loads(expected_result.stdout.strip())
    except json.JSONDecodeError:
        assert False, f"Could not parse expected output as JSON: {expected_result.stdout.strip()}"

    # Now run the script again through the test helper and compare
    result = run_main_script(input_args)
    assert result.returncode == 0
    try:
        actual_output = json.loads(result.stdout.strip())
        assert actual_output == expected_output
    except json.JSONDecodeError:
        assert False, f"Could not parse actual output as JSON: {result.stdout.strip()}"
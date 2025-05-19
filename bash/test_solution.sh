#!/bin/bash

# Test script for solution.sh

# Usage: ./test_solution.sh

# Function to run a test case
run_test() {
  local input=("$@")
  local expected_output="${input[-2]}"
  local test_name="${input[-2]}"
  local input_args=("${input[@]:0:${#input[@]}-2}")
  local actual_output
  local exit_status

  echo "Running test: $test_name"
  # Run the solution script with the provided input arguments
  actual_output=$(bash bash/solution.sh "${input_args[@]}")
  exit_status=$?

  # Compare actual output with expected output
  if [ "$exit_status" -eq 0 ] && [ "$actual_output" = "$expected_output" ]; then
    echo "Test Passed"
  else
    echo "Test Failed"
    echo "  Input: ${input_args[@]}"
    echo "  Expected Output: $expected_output"
    echo "  Actual Output: $actual_output"
    echo "  Exit Status: $exit_status"
  fi
  echo ""
}

# Function to run a test case expecting an error
run_error_test() {
  local input=("$@")
  local expected_output_regex="${input[-1]}"
  local test_name="${input[-2]}"
  local input_args=("${input[@]:0:${#input[@]}-2}")
  local actual_output
  local exit_status

  echo "Running error test: $test_name"
  # Run the solution script with the provided input arguments
  actual_output=$(bash bash/solution.sh "${input_args[@]}" 2>&1) # Capture stderr as well
  exit_status=$?

  # Check for non-zero exit status and expected output pattern
  if [ "$exit_status" -ne 0 ] && [[ "$actual_output" =~ $expected_output_regex ]]; then
    echo "Error Test Passed: $test_name"
  else
    echo "Error Test Failed: $test_name"
    echo "  Input: ${input_args[@]}"
    echo "  Expected Exit Status: Non-zero"
    echo "  Actual Exit Status: $exit_status"
    echo "  Expected Output (regex): $expected_output_regex"
    echo "  Actual Output: $actual_output"
  fi
  echo ""
}

# Make solution.sh executable
chmod +x solution.sh

# Test Cases

# Example input
run_test 120 80 150 30 "2 1 1 0" "Example Input"

# Sorted ascending input
run_test 1 2 3 4 5 "0 0 0 0 0" "Sorted Ascending"

# Sorted descending input
run_test 5 4 3 2 1 "4 3 2 1 0" "Sorted Descending"

# Input with duplicates
run_test 10 20 10 30 20 "1 1 0 0 0" "Input with Duplicates"

# Single element input
run_test 100 "0" "Single Element"

# Empty input (expect error)
run_error_test "" "Usage: ./solution.sh" "Empty Input"

# Non-integer input (expect error)
run_error_test 10 20 abc 30 "Error: All arguments must be non-negative integers." "Non-integer Input"

# Test cases for 100 elements

# 100 elements - Ascending
ascending_100=()
expected_ascending_100=()
for i in {1..100}; do
  ascending_100+=("$i")
  expected_ascending_100+=("0")
done
run_test "${ascending_100[@]}" "${expected_ascending_100[*]}" "100 Elements - Ascending"

# 100 elements - Descending
descending_100=()
expected_descending_100=()
for i in {100..1}; do
  descending_100+=("$i")
  expected_descending_100+=("$((i - 1))")
done
run_test "${descending_100[@]}" "${expected_descending_100[*]}" "100 Elements - Descending"

# 100 elements - Random (simple random generation)
random_100=()
for i in {1..100}; do
  random_100+=("$((RANDOM % 200))") # Random numbers between 0 and 199
done
# Calculate expected output for random_100 (O(n) calculation using a stack)
expected_random_100=()
n_random=${#random_100[@]}
stack=() # Stack to store elements in increasing order

# Iterate from right to left
for ((i=n_random-1; i>=0; i--)); do
  current_score=${random_100[i]}
  
  # Pop elements from stack that are greater than or equal to the current element
  while [ ${#stack[@]} -gt 0 ] && [ ${stack[-1]} -ge $current_score ]; do
    stack=("${stack[@]:0:${#stack[@]}-1}") # Pop last element
  done
  
  # The number of elements remaining in the stack are smaller than the current element
  expected_random_100[i]=${#stack[@]}
  
  # Push the current element onto the stack
  stack+=("$current_score")
done
run_test "${random_100[@]}" "${expected_random_100[*]}" "100 Elements - Random"

# 100 elements - Shuffled (simple shuffle of ascending)
shuffled_100=($(shuf -e "${ascending_100[@]}"))
# Calculate expected output for shuffled_100 (O(n) calculation using a stack)
expected_shuffled_100=()
n_shuffled=${#shuffled_100[@]}
stack=() # Stack to store elements in increasing order

# Iterate from right to left
for ((i=n_shuffled-1; i>=0; i--)); do
  current_score=${shuffled_100[i]}
  
  # Pop elements from stack that are greater than or equal to the current element
  while [ ${#stack[@]} -gt 0 ] && [ ${stack[-1]} -ge $current_score ]; do
    stack=("${stack[@]:0:${#stack[@]}-1}") # Pop last element
  done
  
  # The number of elements remaining in the stack are smaller than the current element
  expected_shuffled_100[i]=${#stack[@]}
  
  # Push the current element onto the stack
  stack+=("$current_score")
done
run_test "${shuffled_100[@]}" "${expected_shuffled_100[*]}" "100 Elements - Shuffled"

echo "All tests finished."
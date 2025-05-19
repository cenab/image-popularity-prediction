#!/bin/bash

# Image Popularity Prediction Problem
# Given an array of engagement scores, return an array where each element
# tells how many future images had a lower score.

# Usage: ./solution.sh [score1] [score2] ...
# Example: ./solution.sh 120 80 150 30

# Check if any arguments are provided
if [ "$#" -eq 0 ]; then
  echo "Usage: $0 [score1] [score2] ..."
  echo "Example: $0 120 80 150 30"
  exit 1
fi

# Validate input: ensure all arguments are integers
for score in "$@"; do
  if ! [[ "$score" =~ ^[0-9]+$ ]]; then
    echo "Error: All arguments must be non-negative integers."
    echo "Usage: $0 [score1] [score2] ..."
    exit 1
  fi
done

scores=("$@")
n=${#scores[@]}
result=()

# Implement the logic (O(n) in Bash using a stack)
result=()
stack=() # Stack to store elements in increasing order

# Iterate from right to left
for ((i=n-1; i>=0; i--)); do
  current_score=${scores[i]}
  
  # Pop elements from stack that are greater than or equal to the current element
  while [ ${#stack[@]} -gt 0 ] && [ ${stack[-1]} -ge $current_score ]; do
    stack=("${stack[@]:0:${#stack[@]}-1}") # Pop last element
  done
  
  # The number of elements remaining in the stack are smaller than the current element
  result[i]=${#stack[@]}
  
  # Push the current element onto the stack
  stack+=("$current_score")
done

# Print the result array (space-separated)
echo "${result[@]}"
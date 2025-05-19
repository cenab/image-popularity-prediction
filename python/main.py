#!/usr/bin/env python3
"""
Image Popularity Prediction (O(n) solution)
Usage: python main.py 120 80 150 30
Output: [2, 1, 1, 0]

Given an array of engagement scores for a user's images ordered by creation time,
return an array where each element tells how many future images had a lower score.
This implementation uses an O(n) time complexity approach with a stack.

Pass any number of integer arguments representing engagement scores in order of creation.
"""
import sys

if len(sys.argv) == 1:
    print(f"Usage: python {sys.argv[0]} <int1> <int2> ... <intN>")
    sys.exit(1)

try:
    arr = [int(x) for x in sys.argv[1:]]
except ValueError:
    print("All arguments must be integers.")
    sys.exit(1)

n = len(arr)
result = [0] * n
stack = [] # Stack to store elements in increasing order

# Iterate from right to left
for i in range(n - 1, -1, -1):
    # Pop elements from stack that are greater than or equal to the current element
    while stack and stack[-1] >= arr[i]:
        stack.pop()

    # The number of elements remaining in the stack are smaller than the current element
    result[i] = len(stack)

    # Push the current element onto the stack
    stack.append(arr[i])

print(result)
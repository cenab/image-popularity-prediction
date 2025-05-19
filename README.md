# Image Popularity Prediction

This repository contains solutions to the Image Popularity Prediction problem, where for a given array of image engagement scores ordered by creation time, we need to return an array where each element indicates how many future images had a lower engagement score.

## Problem Description

Given an array of engagement scores for a user's images ordered by creation time, return an array where each element tells how many later images in their portfolio performed worse (i.e., had a lower engagement score). This helps spot declining trends or highlights when quality started to drop.

Example:
Input: `[120, 80, 150, 30]`
Output: `[2, 1, 1, 0]`

## Tests

Extensive tests have been written for both the Bash and Python solutions to ensure their correctness.

**How to Run Tests:**

1. Navigate to the root directory of the repository in your terminal.

2. To run the Bash tests:

   ```bash
   bash bash/test_solution.sh
   ```

3. To run the Python tests:

   ```bash
   python python/test_main.py
   ```

## Solutions

Two solutions are provided: one in Bash and one in Python. Both solutions accept an arbitrary array of integers as input arguments from the command line and output the result as an array.

### Bash Solution

The Bash solution is implemented in [`bash/solution.sh`](bash/solution.sh). It uses a stack-based approach to achieve optimal time complexity.

**Prerequisites:**
- A Bash-compatible environment.

**How to Run:**

1. Navigate to the root directory of the repository in your terminal.
2. Execute the script with the desired engagement scores as arguments:

   ```bash
   bash bash/solution.sh 120 80 150 30
   ```

**Example:**

```bash
$ bash bash/solution.sh 120 80 150 30
2 1 1 0
```

### Python Solution

The Python solution is implemented in [`python/main.py`](python/main.py). It also uses a stack-based approach for optimal time complexity.

**Prerequisites:**
- Python 3 installed.

**How to Run:**

1. Navigate to the root directory of the repository in your terminal.
2. Execute the script with the desired engagement scores as arguments:

   ```bash
   python python/main.py 120 80 150 30
   ```

**Example:**

```bash
$ python python/main.py 120 80 150 30
[2, 1, 1, 0]
```

## Notes on Complexity

Both the Bash and Python solutions provided have a time complexity of **O(n)**, where 'n' is the number of images (elements in the input array). This is achieved by using a stack-based approach that processes each element of the input array a constant number of times.

The space complexity for both solutions is **O(n)**, primarily due to storing the input array and the resulting output array, both of which scale linearly with the number of input elements. The stack used in the O(n) implementations also has a maximum size of O(n) in the worst case.
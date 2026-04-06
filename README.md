# COP4533 Programming Assignment: Highest Value Longest Common Subsequence

## Student Information

Name: Imaan Edhi
UFID: 28443010

## Overview

This project solves the Highest Value Longest Common Subsequence (HVLCS) problem.

Given a fixed alphabet where each character has a nonnegative integer value, and two input strings A and B, the program computes:

1. the maximum value of a common subsequence of A and B
2. one optimal common subsequence achieving that value

## Repository Structure

```text
src/
  hvlcs.py
  benchmark.py
data/
  example.in
  example.out
  test1.in ... test10.in
results/
  runtime_results.csv
  runtime_plot.png
README.md
requirements.txt
.gitignore
```

## Setup

This project uses Python 3.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Main Program

```bash
python src/hvlcs.py data/example.in
```

## Example Input

```
3
a 2
b 4
c 5
aacb
caab
```

## Expected Example Output

```
9
cb
```

## How to Run the Benchmark

```bash
python src/benchmark.py
```

This generates:

* results/runtime_results.csv
* results/runtime_plot.png

## Assumptions

Input format is:

* integer K
* K lines of character-value pairs
* string A
* string B

Characters in A and B are part of the given alphabet.
Character values are nonnegative integers.

---

## Question 1: Empirical Comparison

I used 10 nontrivial input files, each with strings of length at least 25. I measured runtime by running the program multiple times on each file and averaging the results. The runtime graph is shown in `results/runtime_plot.png`.

The observed runtime increases with input size and aligns with the expected dynamic programming complexity. Since the algorithm fills a 2D table of size n × m, the empirical results support an overall time complexity of O(nm).

---

## Question 2: Recurrence Equation

Let OPT(i, j) be the maximum value of a common subsequence of the prefixes A[1..i] and B[1..j].

### Base Cases

* OPT(i, 0) = 0 for all i
* OPT(0, j) = 0 for all j

### Recurrence

* If A[i] = B[j], then:
    OPT(i, j) = OPT(i-1, j-1) + v(A[i])

* Otherwise:
    OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1))

### Explanation

If the current characters match, we include that character and add its value to the optimal solution of the smaller subproblem. If they do not match, we consider skipping one character from either string and take the better result. This works due to optimal substructure and overlapping subproblems.

---

## Question 3: Pseudocode and Big-Oh

### Pseudocode

```
HVLCS(A, B, values):
    n = length(A)
    m = length(B)
    create dp[0..n][0..m]

    for i = 0 to n:
        dp[i][0] = 0
    for j = 0 to m:
        dp[0][j] = 0

    for i = 1 to n:
        for j = 1 to m:
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + values[A[i-1]]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    reconstruct one optimal subsequence by tracing backward

    return dp[n][m]
```

### Runtime

The algorithm fills a table of size (n+1) × (m+1), and each entry is computed in constant time. Therefore, the time complexity is O(nm). The space complexity is also O(nm).

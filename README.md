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

## Setup

This project uses Python 3.

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

How to Run the Main Program:
python src/hvlcs.py data/example.in

Example Input:
data/example.in
3
a 2
b 4
c 5
aacb
caab

Expected Example Output:
data/example.out
9
cb

How to Run the Benchmark:
python src/benchmark.py

This generates:

results/runtime_results.csv
results/runtime_plot.png

Assumptions
Input format is:
- integer K
- K lines of character-value pairs
- string A
- string B
Characters in A and B are part of the given alphabet.
Character values are nonnegative integers.
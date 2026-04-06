import os
import time
import csv
import subprocess
import matplotlib.pyplot as plt


TEST_FILES = [
    "data/test1.in",
    "data/test2.in",
    "data/test3.in",
    "data/test4.in",
    "data/test5.in",
    "data/test6.in",
    "data/test7.in",
    "data/test8.in",
    "data/test9.in",
    "data/test10.in",
]


def get_input_sizes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    k = int(lines[0])
    a = lines[k + 1]
    b = lines[k + 2]
    return len(a), len(b)


def benchmark():
    os.makedirs("results", exist_ok=True)
    rows = []

    for test_file in TEST_FILES:
        # run a few times and average
        times = []
        for _ in range(5):
            start = time.perf_counter()
            subprocess.run(
                ["python3", "src/hvlcs.py", test_file],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
            end = time.perf_counter()
            times.append(end - start)

        avg_time = sum(times) / len(times)
        len_a, len_b = get_input_sizes(test_file)
        rows.append([test_file, len_a, len_b, avg_time])

    with open("results/runtime_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "len_a", "len_b", "avg_runtime_seconds"])
        writer.writerows(rows)

    x = list(range(1, len(rows) + 1))
    y = [row[3] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker="o")
    plt.xlabel("Test File Number")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("HVLCS Runtime on 10 Input Files")
    plt.xticks(x)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/runtime_plot.png")


if __name__ == "__main__":
    benchmark()
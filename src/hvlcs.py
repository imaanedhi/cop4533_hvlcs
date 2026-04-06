import sys


def read_input(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        ch, val = lines[i].split()
        values[ch] = int(val)

    a = lines[k + 1]
    b = lines[k + 2]

    return values, a, b


def hvlcs(values, a, b):
    n = len(a)
    m = len(b)

    # dp[i][j] = maximum value of a common subsequence of a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[a[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # reconstruct one optimal subsequence
    i, j = n, m
    subseq = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + values[a[i - 1]]:
            subseq.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subseq.reverse()
    return dp[n][m], "".join(subseq)


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/hvlcs.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    values, a, b = read_input(input_file)
    max_value, subsequence = hvlcs(values, a, b)

    print(max_value)
    print(subsequence)


if __name__ == "__main__":
    main()
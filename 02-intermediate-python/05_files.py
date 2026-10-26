"""Files.

Why this exists: CSVs, logs, and notes live on disk.
Run: python 02-intermediate-python/05_files.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SAMPLE = ROOT / "_sample_returns.csv"


def demo() -> None:
    SAMPLE.write_text("date,ret\n2024-01-02,0.01\n2024-01-03,-0.004\n", encoding="utf-8")
    text = SAMPLE.read_text(encoding="utf-8")
    print(text)

    rows = []
    with SAMPLE.open(encoding="utf-8") as handle:
        header = handle.readline().strip().split(",")
        for line in handle:
            date, ret = line.strip().split(",")
            rows.append({header[0]: date, header[1]: float(ret)})
    print(rows)


def your_turn() -> None:
    # Append one more date/return row, then print the average return.
    pass


if __name__ == "__main__":
    demo()
    your_turn()


import csv
import sys
from datetime import datetime
from typing import List

DATE_FORMATS = [
    "%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y",
    "%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%dT%H:%M:%S",
]

def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except Exception:
        return False

def is_float(s: str) -> bool:
    try:
        float(s)
        # exclude values that are valid ints (so int preferred)
        return not is_int(s)
    except Exception:
        return False

def is_bool(s: str) -> bool:
    return s.lower() in {"true", "false", "yes", "no", "0", "1"}

def is_date(s: str) -> bool:
    for fmt in DATE_FORMATS:
        try:
            datetime.strptime(s, fmt)
            return True
        except Exception:
            continue
    return False

def infer_type(values: List[str]) -> str:
    counts = {"int":0, "float":0, "bool":0, "date":0, "string":0}
    total = 0
    for v in values:
        v = v.strip()
        if v == "":
            continue
        total += 1
        if is_bool(v):
            counts["bool"] += 1
        elif is_int(v):
            counts["int"] += 1
        elif is_float(v):
            counts["float"] += 1
        elif is_date(v):
            counts["date"] += 1
        else:
            counts["string"] += 1
    if total == 0:
        return "empty"
    # determine best match
    best = max(counts.items(), key=lambda x: x[1])
    best_type, best_count = best
    if best_count / total >= 0.8:
        return best_type
    # if numbers mixed int+float, prefer float if sum majority
    if (counts["int"] + counts["float"]) / total >= 0.8:
        return "float" if counts["float"] > 0 else "int"
    return "mixed/string"

def sample_column(csv_path: str, col: str, max_rows: int = 500) -> List[str]:
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return []
        # determine index
        try:
            idx = int(col) if col.isdigit() else header.index(col)
        except ValueError:
            print(f"Column name '{col}' not found in header.")
            sys.exit(1)
        except Exception:
            print("Invalid column identifier.")
            sys.exit(1)
        values = []
        for row in reader:
            if idx < len(row):
                values.append(row[idx])
            if len(values) >= max_rows:
                break
        return values

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_data_type.py <csv_file> <column_name_or_index>")
        sys.exit(1)
    csv_file = sys.argv[1]
    col = sys.argv[2]
    values = sample_column(csv_file, col)
    inferred = infer_type(values)
    print(f"Inferred type for column '{col}': {inferred}")

if __name__ == "__main__":
    main()
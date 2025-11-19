def load_data():
    return ["record1", "record2", "record3"]

def clean_data(records):
    return [r.upper() for r in records]

def filter_data(records):
    return [r for r in records if "1" in r]


def main():
    records = load_data()
    cleaned = clean_data(records)
    filtered = filter_data(cleaned)
    print("Processed records:", cleaned)
    print("Filtered: filtered")

if __name__ == "__main__":
    main()

def load_data():
    return ["record1", "record2", "record3"]

def clean_data(records):
    return [r.upper() for r in records]

def filter_data(records):
    return [r for r in records if "1" in r]
def summarise_data(records):
    return {
        "count": len(records),
        "sample": records[:2]
    }


def main():
    records = load_data()
    cleaned = clean_data(records)
    filtered = filter_data(cleaned)
    summary = summarise_data(cleaned)
    print("Processed records:", cleaned)
    print("Filtered: filtered")
    print("Summary:", summary)

if __name__ == "__main__":
    main()

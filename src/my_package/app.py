def load_data():
    return ["record1", "record2", "record3"]

def clean_data(records):
    return [r.upper() for r in records]

def summarise_data(records):
    return {
        "count": len(records),
        "sample": records[:2]
    }


def main():
    records = load_data()
    cleaned = clean_data(records)
    summary = summarise_data(cleaned)
    print("Processed records:", cleaned)
    print("Summary:", summary)

if __name__ == "__main__":
    main()

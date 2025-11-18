def load_data():
    return ["record1", "record2", "record3"]

def clean_data(records):
    return [r.upper() for r in records]

def main():
    records = load_data()
    cleaned = clean_data(records)
    print("Processed records:", cleaned)

if __name__ == "__main__":
    main()

'''Write a generator for paginated DB results'''
def paginated(records, page_size):
    """Return employee records page by page"""
    for i in range(0, len(records), page_size):
        yield records[i:i + page_size]
def main():
    """Display employee records in pages"""
    employees = [
        {"id": 101, "name": "nasha"},
        {"id": 102, "name": "rinsha"},
        {"id": 103, "name": "anfas"},
        {"id": 104, "name": "kavya"},
        {"id": 105, "name": "aksa"}
    ]
    print("Employee Records:\n")
    for page_no, page in enumerate(paginated(employees, 2), start=1):
        print(f"Page {page_no}:")
        print(page)
        print()
main()

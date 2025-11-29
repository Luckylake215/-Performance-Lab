import sys
import json

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка {file_path}: {e}")
        sys.exit(1)

def write_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка {file_path}: {e}")
        sys.exit(1)

def fill_values(tests, values_map):
    for test in tests:
        if 'id' in test and test['id'] in values_map:
            test['value'] = values_map[test['id']]
        if 'values' in test:
            fill_values(test['values'], values_map)

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    values_data = read_json(values_file)
    tests_data = read_json(tests_file)
    values_map = {item['id']: item['value'] for item in values_data['values']}
    tests_structure = tests_data.get("tests", [])
    fill_values(tests_data['tests'], values_map)
    report_data = {"report": tests_structure}
    write_json(report_file, report_data)

if __name__ == "__main__":
    main()
import json
from utils import get_date, filter_five_by_executed, bill, print_descroption

with open("operations.json", 'r') as f:
    file = json.load(f)

filter_by_date = get_date(file)
five_by_executed = filter_five_by_executed(filter_by_date)
print_description = print_descroption(five_by_executed)

print(print_description)


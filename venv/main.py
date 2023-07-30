import json
from utils import get_date, filter_five_by_executed, bill

with open("operations.json", 'r') as f:
    file = json.load(f)

filter_by_date = get_date(file)
five_by_executed = filter_five_by_executed(filter_by_date)




for operation in five_by_executed:

    date = operation["date"]
    date_operation = date[0:10]
    my_date = date_operation.split("-")
    correct_date = ".".join(reversed(my_date))
    description = operation["description"]

    card_bill = ""
    line_bill = ""
    if "from" in operation:
        card_bill += operation["from"]
        line_bill += bill(card_bill)
    bill_to = bill(operation["to"])

    amount = operation["operationAmount"]["amount"]
    currency_name = operation["operationAmount"]["currency"]["name"]


    print(f"""
    {correct_date} {description}
    {line_bill} -> {bill_to}
    {amount} {currency_name}""")




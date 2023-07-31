
def get_date(operations):
    operations_date_validate = []
    for operation in operations:
        if not operation:
            continue
        elif not 'date' in operation:
            continue
        operations_date_validate.append(operation)
    sorted_date = sorted(operations_date_validate, key=lambda operation_date: operation_date['date'], reverse=True)
    return sorted_date


def filter_five_by_executed(operetions):
    executed_operetions = []
    for operetion in operetions:
        if operetion['state'] == 'EXECUTED':
            executed_operetions.append(operetion)
        if len(executed_operetions) == 5:
            break
    return executed_operetions


def bill(bill_info):
    card_info = bill_info.split()
    number = card_info[-1]

    if bill_info.lower().startswith("счет"):
        masked_number = f"**{number[-4:]}"
        card_info[-1] = masked_number
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        card_info[-1] = masked_number
    return " ".join(card_info)


def print_descroption(five_executed):
    print_descroptions = ""
    for operation in five_executed:
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
        print_descroptions += f"""
{correct_date} {description}
{line_bill} -> {bill_to}
{amount} {currency_name}
"""

    return print_descroptions






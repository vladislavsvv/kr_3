from utils import get_date, filter_five_by_executed, bill, print_descroption

data = [{
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
},
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
    },
    {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
    }]
date_resalt = [{
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
},
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
    },
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
    }]


def tests_get_date():
    assert get_date(data) == date_resalt


data_executed = [{
    "id": 594226727,
    "state": "CANCELED",
},
    {
        "id": 615064591,
        "state": "CANCELED",
    },
    {
        "id": 147815167,
        "state": "EXECUTED",
    },
    {
        "id": 518707726,
        "state": "EXECUTED",

    },
    {
        "id": 649467725,
        "state": "EXECUTED",
    },
    {
        "id": 782295999,
        "state": "EXECUTED",
    },
    {
        "id": 542678139,
        "state": "EXECUTED",
    },
    {
        "id": 558167602,
        "state": "EXECUTED",
    },
    {
        "id": 407169720,
        "state": "EXECUTED",
    }]

data_filtered = [{
    "id": 147815167,
    "state": "EXECUTED",
},
    {
        "id": 518707726,
        "state": "EXECUTED",

    },
    {
        "id": 649467725,
        "state": "EXECUTED",
    },
    {
        "id": 782295999,
        "state": "EXECUTED",
    },
    {
        "id": 542678139,
        "state": "EXECUTED",
    }]


def tests_filter_five_by_executed():
    assert filter_five_by_executed(data_executed) == data_filtered


date_bill = ["Счет 73222753239048295679", "Visa Gold 7756673469642839"]

date_bill_resalt = ["Счет **5679", "Visa Gold 7756 67** **** 2839"]


def tests_bill():
    assert bill(date_bill[0]) == date_bill_resalt[0]
    assert bill(date_bill[1]) == date_bill_resalt[1]


data_print_1 = [{
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
        "amount": "30153.72",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
}]
date_print_2 = [{
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
        "amount": "30153.72",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "to": "Счет 43241152692663622869"
}]


def tests_print_print_descroption():
    assert print_descroption(
        data_print_1) == "\n19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n"
    assert print_descroption(date_print_2) == "\n19.11.2019 Перевод организации\n -> Счет **2869\n30153.72 руб.\n"

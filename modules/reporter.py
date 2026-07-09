import json


def save_json_report(data):

    with open(
        "reports/report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
from random import randrange


def generate_dashboard_data():
    items = []

    datasetids = [
        "INVESTMENT",
        "EXPORT",
        "GDP",
        "CONSUMPTION",
        "UNEMPLOYMENT",
        "HOUSEHOLD",
        "HOUSEHOLD",
        "GDP"
    ]
    filters = ["Scenario 1", "Scenario 2",
               "Scenario 3", "Scenario 4", "Scenario 5"]

    for datesetid in datasetids:
        for filter in filters:
            item = {
                "datasetid": datesetid,
                "filters": [
                    {
                        "name": "scenario",
                        "value": filter,
                    }
                ],
                "value": randrange(1, 101),
            }
            items.append(item)

    return items

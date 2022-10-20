from datetime import datetime
from random import randrange
import pandas as pd
import numpy as np


def generate_time_serieses():
    items = []

    datasetids = list(range(50))

    filters = ["Scenario 1", "Scenario 2",
               "Scenario 3", "Scenario 4", "Scenario 5"]

    timestamps = pd.date_range(
        start="01/01/2022", end="09/30/2024")
    data = np.random.randint(1, 101, len(timestamps))
    df = pd.DataFrame({str(i): data for i in range(50)})
    df['timestamp'] = timestamps

    for filter in filters:
        df['filters'] = [[{"name": "scenario",
                           "value": filter}]] * len(timestamps)

        for datasetid in datasetids:
            df['datasetid'] = datasetid

        items.extend(df.to_dict(orient='records'))

    return items

from datetime import datetime
from pprint import pprint
import pandas as pd
import numpy as np


def generate_time_serieses():
    items = []

    datasetids = list(range(20))
 
    filters = ["Scenario 1", "Scenario 2",
               "Scenario 3", "Scenario 4", "Scenario 5"]

    timestamps = pd.date_range(
        start="01/01/2022", end="09/30/2024")
    data = np.random.randint(1, 101, len(timestamps))
    df = pd.DataFrame({str(i): data for i in datasetids})
    df['timestamp'] = timestamps
    df['value'] = None

    for filter in filters:
        df['filters'] = [[{"name": "scenario",
                           "value": filter}]] * len(timestamps)

        for datasetid in datasetids:
            df['datasetid'] = str(datasetid)

            df[['datasetid', 'timestamp', 'filters', str(datasetid)]
               ].rename(columns={str(datasetid): 'value'})

            items.extend(df[['datasetid', 'timestamp', 'filters', str(datasetid)]
                            ].rename(columns={str(datasetid): 'value'}).to_dict(orient='records'))
    print(f'{5 * 50 * len(timestamps)} - {len(items)}')
    pprint(items[1])
    return items

from elasticsearch import Elasticsearch
from generate_time_serieses import generate_time_serieses
from generate_dashboard_data import generate_dashboard_data
from pprint import pprint
from time import time


client = Elasticsearch(
    hosts="https://db9d4a6fa7cd4393bffab8572a4119c5.centralus.azure.elastic-cloud.com:443", http_auth=("quantum", "i6Q8sbWO%v1c"))


def insert_time_series_data(index, data):
    bulkOperation = {"index": {"_index": index}}

    bulkItems = []
    for item in data:
        bulkItems.append(bulkOperation)
        bulkItems.append(item)

    client.bulk(body=bulkItems)


def main():
    t = time()
    time_series = generate_time_serieses()
    insert_time_series_data("chart-data", time_series)
    print(f'time {time() - t}')
    dashboard_data = generate_dashboard_data()
    insert_time_series_data("dashboard-data", dashboard_data)


if __name__ == '__main__':
    main()

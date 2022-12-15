# Seed ES index script


# Website 

https://quantumkibana.azurewebsites.lnet/

davoud_taghawi
%Sl!j%14*eIT


## Files
### generateItems:
Contains one function to generate array of items
### dbSeed (main file):
Take items from generateItems and push to Elasticsearch.

This data is used in the FOCN dashboards.

``` python
Example datapoint pushed
{
    
    # Unique Dataset Id to use to map data to the UI
    "datasetid": datesetid,
    # Filters that will be applicable on the dataset
    "filters": [
        {
            "name": "scenario",
            "value": filter,
        }
    ],
    # Randomizes the data for testing purposes
    "value": randrange(1, 101),
    # For time-series data this can be used to map a sequence otherwise the latest of this datasetid will be used
    "timestamp": timestamp
}
```

Indexes used
|Index Name|Description|
|-|-|
|chart-data|Data that will be used in aggregations (value is mapped to type number)|
|dashboard-data|Data that will be used in single value dashboard UI elements (data is mapped to string|
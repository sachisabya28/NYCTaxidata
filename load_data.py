# Imports
import dask.dataframe as dd
import dask.bag as db
import pandas as pd
import dask_mongo

'''
dask dataframe used to read CSV
dask provides parallel and distributed computing 
with minimal coordination/resources
'''
print('data load started ....')
daskframe = dd.read_csv('https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv', 
                 assume_missing=True)

pd_dataframe = db.from_delayed(daskframe.map_partitions(pd.DataFrame.to_dict, 
                                        orient='records').to_delayed())

# Write to a Mongo database
dask_mongo.to_mongo(
    pd_dataframe,
    database="taxidata",
    collection="nyctaxidata",
    connection_kwargs={"host": "localhost", "port": 27017},
)
print('data load completed.')
## Problem statement
## _TLC Trip Record Data_
The goal for this task is to analyse the NYC taxi trip data. Please choose a database (or database like) system of your choice. 
This can run locally on your laptop or be a hosted version on the cloud. 
Please sent us all the ressources you used while creating your data store. 
This includes schemas, setup scripts, data loading scripts and of course the queries themselves.
To help you better decide, here are some requirements:

Will be used by analysts to create charts and by data scientists as in input for their model generation
The schema of the data might change over time


1. Download the dataset from taxi_rides. Load the data set into your system.
2. Now it is time to run some queries on your newly created data set. 
Please share with us the queries for the following questions, as well as their execution times.

    - Count the number of trips where the total amount is less than 5$.
    - At what hour of the day do people spent the most money on taxi rides?
    - What is average percentage of the tip?

- Refer to mongoqueries.txt
3. Lets increase the the amount of data. For this just rerun your import script for 10 times. 
Rerun your queries and share their execution time with us.


## API
Since other teams inside our company are interested in the data, we want to give them programmtic access through an API. 
Please write your solution in python, you are free to use as many libraries as you want:

1. Return the number of trips, where to the total amount is less than N. N is a parameter, 
which can be passed by the consumer of the API.


## Solution 
*** 
- Pull the latest version from GIT
- Install Mongodb https://docs.mongodb.com/manual/installation/ 
- Make sure Mongo is running on PORT 27017
***

###### Install the devDependencies and start the server. ######

```bash
sh setup.sh
sh load_data.sh 
sh start_app.sh
```

Verify the deployment by navigating to your server address in
your preferred browser.

```bash
localhost:8000/
```

```bash
{
    "data": "Welcome to APP refer to APIs to get data",
    "status": 200
}
```

API endpoint (GET)

```bash
http://localhost:8000/api/<amount>
```

Response 

```bash
{
    "Amount": "5",
    "Trips_Count": 46590
}
```

Data not present
```bash
{
    "data": "No data Found",
    "status": 400
}
```

## Technologies
***
A list of technologies used within the project:
- Mongo - Database
- Flask -  Web framework
- flask_pymongo -  Flask extensions for integrating MongoDB
- Dask - to enable parallel computing and loading data to mongo


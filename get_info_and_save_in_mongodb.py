import requests
import json
import pymongo
from pymongo import MongoClient
import os
import time

def getData():
    pages = getPages()
    return appendPages(pages)

def getPages():
    response = requests.get("https://api.instantwebtools.net/v1/passenger?page=0&size=1000").json()
    pages = range(response['totalPages'])
    return pages

def appendPages(pages):
    results = []
    for page in pages:
        response = requests.get(("https://api.instantwebtools.net/v1/passenger?page={0}&size=10").format(str(page)))

        if(response.status_code != 200):
            print("Page {} has returned {}".format(page, response.status_code))
            break

        result = response.json()['data']

        results = results + result

    return results

def insert_mongodb():
    #"mongodb://test:1234@localhost:27017"
    myclient = MongoClient(os.getenv('MONGO_URL'))
    db = myclient.admin
    test = db.test
    test.insert_many(data)
    
   
if __name__ == "__main__":
    data = getData()
    insert_mongodb()
    print("done")

    time.sleep(999999999)

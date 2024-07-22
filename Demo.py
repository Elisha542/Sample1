from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymongo

#It is a backend code

# Define Pydantic model
class DetailsQuery(BaseModel):
    name: str
    start_date: int
    end_date: int

# FastAPI setup
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# MongoDB connection setup
mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)
db = client["TODO"]
collection = db["todo"]

# Endpoint to fetch details
@app.get("/details")
async def getDetails(name: str, start_date: int = Query(...), end_date: int = Query(...)):
    data = all(name, start_date, end_date)
    return {"data": data}

# MongoDB query function
def all(name, start_date, end_date):
    query = {
        "name": name,
        "start_date": { "$gte": start_date },
        "end_date": { "$lte": end_date }
    }
    response = collection.find(query)
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

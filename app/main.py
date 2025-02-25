from fastapi import FastAPI
from app.consumers.kafka_consumer import start_kafka_consumer

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await start_kafka_consumer()
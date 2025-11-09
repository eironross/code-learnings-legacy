import pika

import time
from fastapi import FastAPI

app = FastAPI()



# Configuration (from your environment variables)
HOST = "rabbitmq"
PORT = 5672
USER = "guest"
PASS = "guest"

def get_connection(retries=10, delay=5):
    """Attempts to connect to RabbitMQ with retries."""
    for attempt in range(retries):
        try:
            credentials = pika.PlainCredentials(USER, PASS)
            parameters = pika.ConnectionParameters(
                host=HOST,
                port=PORT,
                credentials=credentials
            )
            print(f"Attempting to connect to RabbitMQ at {HOST}:{PORT} (Attempt {attempt + 1}/{retries})...")
            connection = pika.BlockingConnection(parameters)
            print("Connection successful!")
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            if attempt < retries - 1:
                print(f"Connection failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed to connect to RabbitMQ after {retries} attempts.")
                raise # Re-raise the exception if all retries fail
    
@app.get("/")
def home():
    return { "status": "ok" , "message": "hello, world!"}

@app.post("/send")
def send_message(msg: str):
    conn = get_connection()
    channel = conn.channel()
    channel.queue_declare(queue="tasks")
    channel.basic_publish(exchange="", routing_key="tasks", body=msg)
    conn.close()
    return {"status": "sent", "message": msg}
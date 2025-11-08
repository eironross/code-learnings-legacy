import pika
import time


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



connection = get_connection()
channel = connection.channel()
channel.queue_declare(queue="tasks")

def callback(ch, method, properties, body):
    try:
        print(f"Received: Completed task message is {body.decode()}")
    except Exception as e:
        print(f"Error processing task: {e}")
        # 2. Optionally, negatively acknowledge (NACK) for redelivery
        ch.basic_nack(delivery_tag = method.delivery_tag, requeue=True)

channel.basic_consume(queue="tasks", on_message_callback=callback, auto_ack=False)
print("Worker listening...")
channel.start_consuming() 
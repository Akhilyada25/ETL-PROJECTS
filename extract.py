from kafka import KafkaConsumer
import json

def stream_kafka_data():
    consumer = KafkaConsumer('retail_transactions', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    
    for message in consumer:
        data = json.loads(message.value)
        print(f"Received transaction: {data}")

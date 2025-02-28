from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

products = ["Laptop", "Phone", "Tablet", "Headphones"]
categories = ["Electronics", "Accessories"]
prices = {"Laptop": 1000, "Phone": 500, "Tablet": 300, "Headphones": 100}

while True:
    transaction = {
        "product": random.choice(products),
        "category": random.choice(categories),
        "quantity": random.randint(1, 5),
        "price": prices[random.choice(products)],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    producer.send('retail_transactions', value=transaction)
    print(f"Sent: {transaction}")
    time.sleep(2)

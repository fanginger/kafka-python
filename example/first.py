from kafka import KafkaConsumer,KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:1234')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')


consumer = KafkaConsumer('my_favorite_topic',bootstrap_servers='localhost:1234', group_id='my_favorite_group')
for msg in consumer:
    print (msg)
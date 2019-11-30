import pika

credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明queue队列
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("[x] Received:\n ch: %r;\nmethod: %r;\nproperties: %r;\nbody: %r\n " % (ch, method, properties, body))


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True
                      )
print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
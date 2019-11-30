import pika
import time
credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明queue队列
channel.queue_declare(queue='hello', durable=True)  # 接收端也需要durable

def callback(ch, method, properties, body):
    print("[x] Received: %r\n" % body)
    time.sleep(20)
    print("[x] done...")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动把消费完这个消息的标记确认


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      # auto_ack=True  # False为需要手动确认，在消费者没有确认已经把消息消费完时，队列中的数据不会消失；
                      )
print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
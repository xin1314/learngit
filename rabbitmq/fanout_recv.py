import pika
import time
credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 声明queue
result = channel.queue_declare('', exclusive=True)  # 不指定queue名称，rabbit会随机分配一个排他的名字，exclusive：排他性的,True会在此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)  # 将这个队列绑定到exchange

def callback(ch, method, properties, body):
    print("[x] Received: %r\n" % body)
    time.sleep(1)
    print("[x] done...")


channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True  # False为需要手动确认，在消费者没有确认已经把消息消费完时，队列中的数据不会消失；
                      )
print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
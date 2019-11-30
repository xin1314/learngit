import pika
import time
import sys
credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
# 声明queue
result = channel.queue_declare('', exclusive=True)  # 不指定queue名称，rabbit会随机分配一个排他的名字，exclusive：排他性的,True会在此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue

severies = sys.argv[1:]
if not severies:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
for severity in severies:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)  # 将这个队列绑定到exchange


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
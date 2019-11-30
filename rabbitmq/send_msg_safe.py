import pika

credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明queue队列
channel.queue_declare(queue='hello', durable=True)  # durable=True：开启持久化，保证服务器挂了重启后队列仍存在，但其中的数据会丢失，需要其他地方

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World',
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))  # properties用于消息持久化，确保重启后队列中的数据存在
print("[x] Send 'Hello World!'")
connection.close()
import pika
# fanout 广播模式，错过消息就接收不到了,通过exchange绑定
credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body='Hello World',
)  # properties用于消息持久化，确保重启后队列中的数据存在
print("[x] Send 'Hello World!'")
connection.close()
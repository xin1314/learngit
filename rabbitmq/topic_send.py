import pika
import sys
# topic 主题模式，更细致的分组，收集更细致的数据，通过exchange绑定
credentials = pika.PlainCredentials('xin', 'xin5655')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                     credentials=credentials))

channel = connection.channel()  # 建立了rabbit协议的通道

# 声明exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

severity = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'  # 严重程度，级别
message = ''.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=message,
)  # properties用于消息持久化，确保重启后队列中的数据存在
print("[x] Send %r: %r" % (severity, message))
connection.close()
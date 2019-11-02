from multiprocessing import Queue
# Queue.get([block[,timeout]]):获取队列中的第一条消息，然后将其从队列中移除，block默认值为True
# 如果block使用默认值，且没有设置timeout（单位秒），消息队列为空，此时程序将被阻塞（停在读取状态），直到消息队列读取
# 到消息为止，如果设置了timeout，则会等到timeout秒，
# 如果block值为False，消息队列为空，则会立刻抛出“Queue.Empty”异常。
# Queue.put(item,[block[,timeout]])
if __name__ == "__main__":
    q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
    q.put("message1")
    q.put("message2")
    print(q.full())  # 判断当前队列是否已满，不满返回False
    q.put("message3")
    print(q.full())

    # 因为消息队列已满，下面的try都会抛出异常
    try:  # 第一个try会等待2秒后再抛出异常，第二个try会立刻抛出异常
        q.put("message4", True, 2)
    except:
        print("消息队列已满，现有消息数量：%s" % q.qsize())  # q.qsize()返回当前队列包含的消息数量

    try:
        q.put_nowait("message4")  # 相当于Queue.get(False)
    except:
        print("消息队列已满，现有消息数量：%s" % q.qsize())

    if not q.empty():  # 读取消息时，先判断消息队列是否为空，再读取
        print("---从队列中获取消息")
        for i in range(q.qsize()):
            print(q.get_nowait())

    if not q.full():  # 先判断消息队列是否已满，再写入
        q.put_nowait("message4")
        print("现有消息数量：%s" % q.qsize())
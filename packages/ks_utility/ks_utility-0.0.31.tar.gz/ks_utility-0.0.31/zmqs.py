import zmq
import json

class ZmqPublisher():
    def __init__(self, pub_address):
        super().__init__()

        context = zmq.Context()
        self.context = context

        #  Socket to talk to server
        self.publisher = context.socket(zmq.PUB)
        self.publisher.bind(pub_address)
        
    def send(self, topic, msg):
        self.publisher.send_multipart([topic.encode('utf8'), json.dumps(msg).encode('utf8')])

    def stop(self):
        # 关闭 socket 和 context
        self.publisher.close()
        self.context.term()

class ZmqSubscriber():
    def __init__(self, sub_address: str):
        super().__init__()

        context = zmq.Context()
        self.context = context
        self.running = True

        self.subscriber = context.socket(zmq.SUB)
        self.subscriber.bind(sub_address)

        # topic = get_topic('.vntrader1', ZmqAction.SUB)
        self.subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

    def on_msg(self, topic: str, msg: str):
        pass

    def listen(self):
        while self.running:
            try:
                topic_raw, msg_raw = self.subscriber.recv_multipart()
                topic = topic_raw.decode()
                msg = msg_raw.decode()
                self.on_msg(topic, msg)
            except zmq.Again as e:
                # 没有消息到达，可以继续循环
                pass
            except zmq.ZMQError as e:
                # 处理 ZeroMQ 错误
                # breakpoint() # todo
                print(f"ZMQError: {e}")
                break
            except Exception as e:
                # 处理其他异常
                # breakpoint() # todo
                print(f"Exception: {e}")
                break     

    def send(self, topic: str, msg: dict):
        self.socket.send_multipart([topic.encode('utf8'), json.dumps(msg).encode('utf8')])

    def stop(self):
        self.running = False
        self.subscriber.close()
        self.context.term()



from SendDecorator import Decorator
from Componenent import NotifierComponenent


class SlackSender(Decorator):
    """
       슬랙 전송 데코레이터 클래스
       """
    notifier = NotifierComponenent
    receiver = ""

    def __init__(self, notifier=NotifierComponenent, receiver=str()):
        self.notifier = notifier
        self.receiver = receiver

    def send(self, message):
        self.notifier.send(message)
        print('슬랙 전송: ' + message + "to: " + self.receiver)



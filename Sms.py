from SendDecorator import Decorator
from Componenent import NotifierComponenent

class SmsSender(Decorator):
    """
    핸드폰 메시지 전송 데코레이터 클래스
    """
    notifier = NotifierComponenent
    receiver = ""


    def __init__(self, notifier=NotifierComponenent, receiver=str()):
        self.notifier = notifier
        self.receiver = receiver

    def send(self, message):
        self.notifier.send(message)
        print('sms 전송: '+ message + "to: "+ self.receiver)

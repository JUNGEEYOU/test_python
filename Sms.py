from Decorator import Decorator


class Sms(Decorator):

    def send(self, message):
        super.send()
        print('sms 전송: '+ message)

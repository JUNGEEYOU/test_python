from Decorator import Decorator


class Kakao(Decorator):

    def send(self, message):
        super.send()
        print('Kakao 전송: ' + message)



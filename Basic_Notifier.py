from Notifier import Notifier


class Basic_Notifier(Notifier):

    def send(self, message):
        print("기본 프린트" + message)

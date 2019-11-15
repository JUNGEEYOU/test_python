from Componenent import NotifierComponenent


class BasicNotifier(NotifierComponenent):
    """
    기본 알림 클래스 - log만 진행
    """

    def send(self, message):
        print("기본 로그 출력: " + message)

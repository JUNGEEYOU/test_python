from BasicNotify import BasicNotifier
from Kakao import KakaoSender
from Sms import SmsSender

send_lena = KakaoSender(SmsSender(BasicNotifier(), "lena"), "lena")
send_lena.send("error message")
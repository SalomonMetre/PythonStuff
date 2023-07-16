import requests as rq
import lxml.html as lxht
from time import sleep
import notify2

ICON_PATH = "/home/salomon-metre/Pictures/Icons/notification.png"
NOTIFICATION_TITLE = "Today's Wiki News !!!"

def show_notification(title, message):
    notify2.init("App Name")
    notifier = notify2.Notification(title, message, icon= ICON_PATH)
    notifier.show()

raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
doc = lxht.fromstring(raw_html.content)
news = doc.xpath('//div[@id="mp-itn"]/ul')[0]
news_list = news.xpath('.//li')

for news in news_list:
    show_notification(NOTIFICATION_TITLE, news.text_content())
    sleep(2)

import requests as rq
import lxml.html as lxht
from time import sleep
import notify2

notify2.init("App Name")

def show_notification(title, message, icon):
    notifier = notify2.Notification(title, message, icon= icon)
    notifier.show()

def show_news():
    news_icon = '/home/salomon-metre/Pictures/Icons/live_news.jpg'
    notification_title = "Today's Wiki News !!!"

    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    news = doc.xpath('//div[@id="mp-itn"]/ul')[0]
    news_list = news.xpath('.//li')

    for news in news_list:
        sleep(10)
        show_notification(notification_title, news.text_content(), news_icon)

def show_featured_article():
    title = "Featured Article !"
    featured_article_icon = '/home/salomon-metre/Pictures/Icons/news_article.png'


    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    news = doc.xpath('//div[@id="mp-tfa"]')[0]
    message = news.text_content().split('\n')[0]
    message_parts = message.split(' ')
    num_words = len(message_parts)
    start = 0
    while(start<num_words):
        sleep(10)
        show_notification(title, ' '.join(message_parts[start:start+40]), featured_article_icon)
        start += 40
        

show_news()
show_featured_article()


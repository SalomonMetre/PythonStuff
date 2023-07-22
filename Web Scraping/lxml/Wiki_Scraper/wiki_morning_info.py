import requests as rq
import lxml.html as lxht
from time import sleep
import notify2
import os

with open('/home/salomon-metre/.notification_time.txt') as file_handler:
    notification_time = file_handler.readline()
    notification_time = int(notification_time)

notify2.init("App Name")

def show_notification(title, message, icon):
    """
    This function shows a notification using a title, a message and an icon
    """
    notifier = notify2.Notification(title, message, icon= icon)
    notifier.set_urgency(notify2.URGENCY_CRITICAL)
    notifier.show()

def show_news():
    """
    Shows news
    """
    news_icon = '/home/salomon-metre/Pictures/Icons/live_news.jpg'
    notification_title = "Today's Wiki News !!!"

    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    news = doc.xpath('//div[@id="mp-itn"]/ul')[0]
    news_list = news.xpath('.//li')

    for news in news_list:
        sleep(notification_time)
        show_notification(notification_title, news.text_content(), news_icon)

def show_featured_article():
    """
    Shows featured article
    """
    # Sets the icon and the title
    title = "Featured Article !"
    featured_article_icon = '/home/salomon-metre/Pictures/Icons/news_article.png'

    # Retrieves the html content, and scrapes it using the div tag and the id attribute then splits the text 
    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    try:
       news = doc.xpath('//div[@id="mp-tfa"]/p')[0]
    except:
        news = doc.xpath('//div[@id="mp-tfa"]')[0]
    message = news.text_content().split('\n')[0]
    message_parts = message.split(' ')
    num_words = len(message_parts)

    # Iterates throught the text and displays each portion as a notification
    start = 0
    while(start<num_words):
        sleep(notification_time)
        show_notification(title, ' '.join(message_parts[start:start+40]), featured_article_icon)
        start += 40
        
def show_did_you_know():
    """
    Show curious facts
    """
    title = 'Did You Know !?'
    show_did_you_know_icon = '//home/salomon-metre/Pictures/Icons/did_you_know.png'

    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    container = doc.xpath('//div[@id="mp-dyk" and @class="mp-contains-float"]')[0]
    items = container.xpath('.//ul')[0].xpath('./li')
    
    for item in items:
        sleep(notification_time)
        show_notification(title,item.text_content(), show_did_you_know_icon)

def show_on_this_day():
    """
    Show curious historical events that happened in history on a day like today
    """
    title = 'On This Day !?'
    show_did_you_know_icon = '//home/salomon-metre/Pictures/Icons/on_this_day.png'

    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    container = doc.xpath('//div[@id="mp-otd" and @class="mp-contains-float"]')[0]
    items = container.xpath('.//ul')[0].xpath('./li')
    
    for item in items:
        sleep(notification_time)
        show_notification(title,item.text_content(), show_did_you_know_icon)

def show_featured_element():
    """
    Show the biography of the person featured today
    """
    title = 'Featured Person !'
    featured_person_icon = '//home/salomon-metre/Pictures/Icons/featured_element.png'

    raw_html = rq.get('https://en.wikipedia.org/wiki/Main_Page')
    doc = lxht.fromstring(raw_html.content)
    container = doc.xpath('//div[@id="mp-tfp"]')[0]
    item = container.xpath('.//table/tbody/tr/td/p')[0]

    text_parts = item.text_content().split(' ')
    num_words = len(text_parts)
    start = 0
    while(start<num_words):
        sleep(notification_time)
        show_notification(title, ' '.join(text_parts[start:start+40]), featured_person_icon)
        start += 40

# Call functions that show different types of notifications
show_news()
show_featured_article()
show_did_you_know()
show_on_this_day()
show_featured_element()


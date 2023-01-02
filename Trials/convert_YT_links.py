# Generating Y2Mate Download links from YT links and opening their respective Y2Mate download pages
import webbrowser as wb

def initiate_download(link):
    wb.open(link,1)

def get_y2mate_download_link(yt_link):
    if yt_link.__contains__('youtube.com'):
        return yt_link.replace('youtube.com','youtubepp.com')
    protocol=yt_link.split(':')[0]
    video_id=yt_link.split('//')[1].split('/')[1]
    return f"{protocol}://www.youtubepp.com/watch?v={video_id}"

def open_download_pages(video_links):
    for link in video_links:
        initiate_download(get_y2mate_download_link(link))

links=[]
while(True):
    user_choice=input('Would you like to enter a YouTube link? y/n\n')
    if(user_choice=='y'):
        link=input('Please enter the link : ')
        links.append(link)
    else:
        print('Well noted.')
        break
print('Get ready to download your YouTube videos ...')
open_download_pages(links)






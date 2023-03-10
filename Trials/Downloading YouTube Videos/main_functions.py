# Generating Y2Mate Download links from YT links and opening their respective Y2Mate download pages
import webbrowser as wb

def initiate_download(link):
    wb.open(link,0)

def get_y2mate_download_link(yt_link):
    if yt_link.__contains__('youtube.com'):
        return yt_link.replace('youtube.com','youtubepp.com')
    protocol=yt_link.split(':')[0]
    video_id=yt_link.split('//')[1].split('/')[1]
    return f"{protocol}://www.youtubepp.com/watch?v={video_id}"

def open_download_pages(video_links):
    if len(video_links)!=0:
        print('Get ready to download your YouTube videos ...')
        for link in video_links:
            initiate_download(get_y2mate_download_link(link))
    else:
        print('No video links available. Could not initiate the download process...')

def get_video_links():
    links=[]
    while(True):
        user_choice=input('Would you like to enter a YouTube link? y/n\n')
        if(user_choice=='y'):
            link=input('Please enter the link : ')
            links.append(link)
        else:
            print('Well noted.')
            break
    return links

def download_from_text_file_links(path):
    try:
        with open(path,'r') as file_handler:
            links=file_handler.readlines()
        for link in links:
            initiate_download(get_y2mate_download_link(link.strip()))
    except FileNotFoundError:
        print('File does not exist')
    
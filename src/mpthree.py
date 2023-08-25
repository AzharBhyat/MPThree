from youtubesearchpython import VideosSearch
import yt_dlp

def mpsearch(_query, _reslimit):
    limit = 10

    if _reslimit : limit = _reslimit
    
    videosSearch = VideosSearch(str(_query), limit)
    resultSearch = videosSearch
    return(videosSearch.result()["result"])

def mpdownload(url):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': 'dl_temp/%(title)s.mp3'}) as video:
        info_dict = video.extract_info(url, download = True)
        video_title = info_dict['title']
        print(video_title)
        video.download(url)    
    print("Successfully Downloaded ")
    return(video_title)

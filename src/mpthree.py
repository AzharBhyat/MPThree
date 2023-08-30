from youtubesearchpython import VideosSearch
import yt_dlp

def mpsearch(_query, _reslimit):
    limit = 10

    if _reslimit : limit = _reslimit
    
    videosSearch = VideosSearch(str(_query), limit)
    resultSearch = videosSearch
    return(videosSearch.result()["result"])

def mpdownload(url):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio'}) as video:
        info_dict = video.extract_info(url, download = False)
        song_title = info_dict['title']
        song_url = info_dict['url'] 
    print("Successfully Downloaded ")
    return(song_title, song_url)

from youtubesearchpython import VideosSearch
import yt_dlp

def mpsearch(_query, _reslimit):
    limit = 10

    if _reslimit : limit = _reslimit
    
    videosSearch = VideosSearch(str(_query), limit)
    resultSearch = videosSearch
    return(videosSearch.result()["result"])

def mpdownload(url):
    ydl_opts = {
        'format': 'bestaudio/best[ext=mp3]/bestaudio/best[abr=128]',  # Get the best quality audio format
        'force_generic_extractor': True,  # Use the generic extractor to avoid downloading
        'simulate': True,  # Simulate the download
        'quiet': False,  # Suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            
            with ydl.urlopen(audio_url) as response:
                audio_data = b''  # Initialize an empty bytes object
                while True:
                    chunk = response.read(8192)  # Read in chunks of 8192 bytes
                    if not chunk:
                        break
                    audio_data += chunk
                    
                return audio_data, info_dict['title']
        except yt_dlp.DownloadError as e:
            print("Error:", e)
            return None

import io
from pytubefix import YouTube
import logging

def download_youtube_video_as_bytes(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_bytes = io.BytesIO()
        stream.stream_to_buffer(video_bytes)
        video_bytes.seek(0)
        logging.info("YouTube video downloaded successfully")
        return video_bytes
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {e}")
        return None

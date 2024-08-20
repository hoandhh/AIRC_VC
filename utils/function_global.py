import socket
import re

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(("8.8.8.8", 1))
        IP_CONNECT = s.getsockname()[0]
        s.close()
    except Exception:
        IP_CONNECT = "127.0.0.1"
    return IP_CONNECT

def calculate_delay(frames_per_second):
    if frames_per_second <= 30:
        return 2
    elif frames_per_second <= 60:
        return 3
    else:
        return 4

def is_youtube_url(url):
    return re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/', url) is not None

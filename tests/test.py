from pytube import YouTube

# URL của video bạn muốn tải
video_url = 'https://youtu.be/2lAe1cqCOXo'

# Tạo đối tượng YouTube
yt = YouTube(video_url)

# Lấy stream đầu tiên (thường là chất lượng thấp nhất)
# stream = yt.streams.first().download()

# Lấy stream có chất lượng tốt nhất với định dạng mp4
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Tải video
stream.download()

print("Video đã được tải xuống thành công!")

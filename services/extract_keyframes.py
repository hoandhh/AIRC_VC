import cv2
import os


def extract_key_frames(video_path, output_folder, delay_seconds, session_id):
    # Mở video bằng OpenCV
    cap = cv2.VideoCapture(video_path)
    
    # Kiểm tra xem video có mở được không
    if not cap.isOpened():
        print("Không thể mở video")
        return

    # Lấy frame rate của video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Frame rate: {fps} fps")
    
    # Tính toán số frame tương ứng với khoảng thời gian delay
    frame_interval = int(fps * delay_seconds)
    print(f"Số frame tương ứng với {delay_seconds} giây: {frame_interval} frame")
    
    frame_number = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_number % frame_interval == 0:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            session_folder = os.path.join(output_folder, session_id)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            # Tính toán thời gian của keyframe hiện tại
            timestamp_seconds = frame_number / fps
            # Định dạng thời gian thành chuỗi để dùng làm tên file
            time_str = f"{int(timestamp_seconds // 3600):02d}-{int((timestamp_seconds % 3600) // 60):02d}-{int(timestamp_seconds % 60):02d}"
            
            key_frame_path = f"{output_folder}/{session_id}/{time_str}.jpg"
            cv2.imwrite(key_frame_path, frame)

            # os.remove(key_frame_path)

        frame_number += 1

    # Giải phóng video capture object
    cap.release()
    print("Hoàn tất trích xuất key frame")

# Đường dẫn đến video và thư mục lưu trữ frame



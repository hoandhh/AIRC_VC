import cv2
import os
import sys




def extract_key_frames(video_path, output_folder, delay_seconds, session_id, optional):
    # Mở video bằng OpenCV
    cap = cv2.VideoCapture(video_path)
    
    # Kiểm tra xem video có mở được không
    if not cap.isOpened():
        print("Không thể mở video")
        return
    
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules/module_ex/self_services/', optional)))
    import get_caption_RN50x4

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
            
        
            if optional == "tooth_captioning":
                # from modules.module_ex.self_services.tooth_captioning import get_caption_RN50x4
                
                print (get_caption_RN50x4.get_single_caption(key_frame_path))
            elif optional == "action_captioning":
                # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules/self_services/action_captioning')))
                # import get_caption_RN50x4
                # return get_caption_RN50x4.get_caption(key_frame_path)
                return None
            elif optional == "classroom_captioning":
                # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules/self_services/classroom_captioning')))
                # import get_caption_RN50x4
                # return get_caption_RN50x4.get_caption(key_frame_path)
                return None
            else:
                return None

            # os.remove(key_frame_path)

        frame_number += 1

    # Giải phóng video capture object
    cap.release()
    print("Hoàn tất trích xuất key frame")

# Đường dẫn đến video và thư mục lưu trữ frame
# extract_key_frames("C:/Users/ASUS/Documents/AIRC_VC/services/test2.mp4", "output", 2, "test1", "tooth_captioning")
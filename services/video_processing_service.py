import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../"))

import cv2
import logging
from utils.function_global import calculate_delay
from flask import current_app as app
# from modules.get_captions.services.temp import get_single_caption
from utils.global_vars import sessions
from caption_image_yolo_llm import caption_image

def extract_key_frames_from_url(app, video_url, output_folder, session_id):
    cap = cv2.VideoCapture(video_url)
    
    if not cap.isOpened():
        logging.error("Cannot open video from URL")
        return

    frames_per_second = cap.get(cv2.CAP_PROP_FPS)
    delay_seconds = calculate_delay(frames_per_second)
    frame_interval = int(frames_per_second * delay_seconds)

    frame_number = 0
    key_frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_number % frame_interval == 0:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                
            key_frame_path = f"{output_folder}/key_frame_{key_frame_number}.jpg"
            cv2.imwrite(key_frame_path, frame)
            caption = caption_image(key_frame_path)
            with app.app_context():
                sessions[session_id]["captions"].put(caption)
            logging.info(f"Generated caption for session {session_id}: {caption}") 
            key_frame_number += 1
        
        frame_number += 1

    cap.release()
    logging.info(f"Finished extracting key frames for session {session_id}")
    sessions[session_id]["captions"].put("[DONE]")

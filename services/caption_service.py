import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../"))

import cv2
import logging
from utils.function_global import calculate_delay
from flask import current_app as app
from modules.get_captions.services.service import get_single_caption
from utils.global_vars import sessions


def extract_key_frames(application, video_path, output_folder, session_id):
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        logging.error("Cannot open video")
        return

    frames_per_second = video_capture.get(cv2.CAP_PROP_FPS)
    delay_seconds = calculate_delay(frames_per_second)
    frame_interval = int(frames_per_second * delay_seconds)
    
    frame_number = 0
    key_frame_number = 0
    
    while video_capture.isOpened():
        return_value, frame = video_capture.read()
        if not return_value:
            break
        
        if frame_number % frame_interval == 0:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                
            key_frame_path = f"{output_folder}/key_frame_{key_frame_number}.jpg"
            cv2.imwrite(key_frame_path, frame)
            caption = get_single_caption(key_frame_path)
            with application.app_context():
                sessions[session_id]["captions"].put(caption)
            logging.info(f"Generated caption for session {session_id}: {caption}") 
            key_frame_number += 1
        
        frame_number += 1

    video_capture.release()
    logging.info(f"Finished extracting key frames for session {session_id}")
    sessions[session_id]["captions"].put("[DONE]")
